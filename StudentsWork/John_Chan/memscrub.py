import re

import isi.app.lib.procs as procs

import isi.hw.check.lib.filenames as files
import isi.hw.check.lib.log as loglib
import isi.hw.check.lib.memory as memlib

# jcc start
import sys
import signal
import time
import isi.hw.check.mfg.consts as consts
start_time = time.time()
abs_starttime = start_time
consts_memscrub  = consts.memscrub_target_run_time()['long']    # jcc
#import pdb; pdb.set_trace()   #jcc
target_run_time = int ( consts_memscrub['target_run_time'] )     # jcc
# jcc end


# Scaling factor to account for irregularities from ideal calc
maxtime_scale = 2.0

# memstress -once copies 7812MB of data
memstress_size = 7812

# Note this 'iters' is different from the test arg 'iterations',
# memstress_iters is passed to memstress command (scaling)
memstress_iters = 10

# Do we want to check, fail if we dont meet performance threshold?
memstress_thresh_check = True

def get_thresh():
    memcheck = memlib.get_mem_checker()
    return memcheck and memcheck.get_memscrub_threshold() or None

def maxtime(iterations):
    """Determine the worst case max run time for this module.
       Returns None if no timeout should be expected."""
    # memstress does 7812MB of data per 100 iterations
    # Note get_memscrub_threshold() values are slower than comparable
    # memspeed threshold values, due to CPU-intensive verify.
    # For rainier (pre-supermicro), this is /4 scaling.
    # cheddar (now deprecated) (slowest) expects memspeed 525MB/s, 
    # which is 14.8s/pass
    # * 4 for verify = 59.5s/pass
    # * .1 (only 10 iters instead of 100) = 5.95s/pass
    # * 20 iterations = 119s
    # * 2 for slack = 238s
    # return 238
    thresh = get_thresh()
    if thresh:
        pass
    else:
        return
    duration = float(memstress_size) / thresh * iterations
    # Now scale duration calculated above (equiv to safe.short.memspeed)
    # to memscrub times: Account for
    # memstress_iters vs. default 100 iters:
    # x4 observed "verify" slowdown is already accounted for 
    # in get_memscrub_threshold()
    duration = duration * memstress_iters / 100
    return int(duration * maxtime_scale)

def run(iterations = 20, fixed = True, random = False):
    log = loglib.get_logger()

    # Set thresholds based on hardware family
    if memstress_thresh_check:
        thresh = get_thresh()
    else:
        thresh = None

    if thresh != None:
        thresh_str = '%d  MB/s' % thresh
    else:
        thresh_str = None

    # Bust out some tests
    mem_reg = re.compile('^Standard memcpy Speed:\s+(?P<speed>\d+(\.\d+)?)',
                         re.IGNORECASE)

    memstress_tests_all = [
        ('fixed', 'prewalk', fixed),
        ('random', 'prerand', random),
        ]
    info = dict([(t[0],t[1:]) for t in memstress_tests_all])
    memstress_opt = lambda t: t in info and info[t][0] or ''
    # XXX Pychecker: memstress_enb not used (verified).
    # Investigate (validate) before final code deletion.
    # memstress_enb = lambda t: t in info and info[t][1]

    # Order in tests matters: run prewalk before prerand
    memstress_tests = []
    for (test, opt, enb) in memstress_tests_all:
        if enb:
            memstress_tests.append(test)
    results = dict(zip(memstress_tests,  [{
        'values':[], 'fail_count':0, 'test_iterations':0,
        } for test in memstress_tests]))

    def speed_average(values):
        if values:
            count = len(values)
            speed = reduce(lambda x, y: x + y, values)
            speed /= count
            speed = int(speed)
        else:
            speed = 0
        return speed
    def speed_minimum(values):
        if values:
            speed = min(values)
        else:
            speed = 0
        return speed
    def speed_maximum(values):
        if values:
            speed = max(values)
        else:
            speed = 0
        return speed
    def speed_threshold(values):
        return thresh_str
    speed_types = [
        ('minimum', speed_minimum),
        ('maximum', speed_maximum),
        ('average', speed_average),
        ('threshold', speed_threshold),
        ]
    def below_threshold_count(values, threshold):
        return len(filter(lambda s: s < threshold, values))

    # Get formatting widths and funcs (pretty print alignments)

    test_width = memstress_tests and max(map(len, info)) or 0
    iter_width = len(str(iterations))
    speed_type_width = max(map(len, zip(*speed_types)[0]))

    def format_test_info(test, width):
        return ('%-*s pattern test' % (width, test.capitalize()))
    def format_iter_info():
        return ('Iterations per test')
    def format_perf_info():
        return ('Performance target')
    def format_header(test, width, iteration, iterations):
        return ('%-*s Iteration %*d of %d' % (width, test.capitalize(),
                                              iter_width, iteration+1,
                                              iterations))
    def format_speed_result(test, width, speed_type):
        return ('%-*s %s speed' % (width, test.capitalize(),
                                   speed_type.capitalize()))
    def format_thresh_result(test, width):
        return ('%-*s Below Threshold Count' % (width, test.capitalize()))
    
    info_width = max(map(len, [
        format_test_info('test', test_width),
        format_iter_info(),
        format_perf_info(),
        ]))
    header_width = len(format_header('x', test_width, 0, iterations))
    result_width = max(map(len, [
        format_speed_result('x', test_width, 'x'*speed_type_width),
        format_thresh_result('x', test_width),
        ]))
    format_width = max(info_width, header_width, result_width)
    # Re-set all specific widths that we wish aligned (info?)
    info_width = header_width = result_width = format_width

    # Log test info
    for (test, opt, enb) in memstress_tests_all:
        log.out('%-*s:  %s' % (info_width,
                               format_test_info(test, test_width),
                               enb and 'True' or 'False'))
    log.out('%-*s:  %d' % (info_width, format_iter_info(), iterations))
    if thresh:
        log.out('%-*s:  %s' % (info_width, format_perf_info(), thresh_str))
    else:
        log.out('%-*s:  %s' % (info_width, format_perf_info(),
                               'No performance target.'))
    log.out('')

    log.out('[memscrub] start : target_run_time is=%s seconds' % ( target_run_time ))
    for test in memstress_tests:
        opt = memstress_opt(test)
        test_iterations = iterations
        # If both fixed and random pattern tests are used,
        # only run a single iteration of the fixed pattern.
        if test == 'fixed' and random:
            test_iterations = 1
        results[test]['test_iterations'] = test_iterations
        log.out('Running %s pattern memscrub with %s' % (test, opt))
        #print "jcc memscrub: start_time     '" + str( time.time() ) + "' seconds"
        for i in xrange(test_iterations):
            
            # jcc start
	    time_now    = time.time() - abs_starttime
	    time_remain = target_run_time - time_now
	    if ( time_now < target_run_time ):
                pass
            else:
		    #print "        : jcc memscrub: remaining_time '" + str( time_remain ) + "' seconds"
		log.out('[memscrub] end: target_run_time=%s seconds is reached, exited' % ( target_run_time ))
                break
            # jcc end  


            (error, output) = procs.get_cmd_output('/%s -once -verify -%s '
                                                   '-iters %d' %
                                                  (files.commands['memstress'],
                                                   opt, memstress_iters))
            header = format_header(test, test_width, i, test_iterations)

            if not error and len(output) > 0:
                speed = None

                for line in output:
                    match = mem_reg.match(line)
                    if match:
                        speed = float(match.group('speed'))
                        break

                try:
                    speed = int(speed)
                except (ValueError, TypeError):
                    speed = None

                if speed != None:
                    # Note fail is optional, depending on thresh
                    fail = thresh != None and speed < thresh
                    results[test]['values'].append(speed)
                    log.out('%-*s: %s%d%s MB/s' %
                           (header_width, header, (fail and '(' or ' '), speed,
                           (fail and ')' or ' ')))
                else:
                    log.out('%-*s: error' % (header_width, header))
                    log.fail('Unable to extract speed info from memstress '
                             'output: %s' % output, 0)
                    results[test]['fail_count'] += 1
                
            else:
                log.out('%-*s: error' % (header_width, header))
                log.fail('Error running memstress command (error %d)' % error, 0)
                results[test]['fail_count'] += 1

    fail_count = 0
    for test in memstress_tests:
        values = results[test]['values']
        fail_count += results[test]['fail_count']
        speed_data = dict([(t, f(values)) for (t, f) in speed_types])
        speed_width = max(map(len, map(str, filter(lambda v:isinstance(v, int),
                                                   speed_data.values()))))
        log.out('')
        for speed_type in zip(*speed_types)[0]:
            if not thresh and speed_type == 'threshold':
                continue
            speed = speed_data.get(speed_type)
            if isinstance(speed, int):
                speed = '%*d  MB/s' % (speed_width, speed)
            log.out('%-*s:  %s' % (
                result_width,
                format_speed_result(test, test_width, speed_type), speed))
        # Note use of len(values): if we have errors, with no valid speed,
        # then we will correctly report total count len(values) < iterations.
        log.out('%-*s:  %d of %d' % (
            result_width,
            format_thresh_result(test, test_width),
            below_threshold_count(values, thresh), len(values)))

        if results[test]['fail_count'] > 0:
            log.fail('%d of %d %s memscrub iterations failed to execute properly' %
                     (results[test]['fail_count'],
                      results[test]['test_iterations'],
                      test), 0)

        speed = speed_data.get('average')
        if thresh and speed and speed < thresh:
            # Save this failure indicator globally in fail_count,
            # so we do not report 'Test passed' at end.
            fail_count += 1
            log.fail('%-*s Memory speed is %d MB/s, expected at least %d MB/s'
                     % (test_width, test.capitalize(), speed, thresh), 0)

    if fail_count == 0:
        log.out('Test passed')
    return fail_count
