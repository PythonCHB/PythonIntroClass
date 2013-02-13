import tempfile

import isi.hw.check.lib.log as loglib
import isi.hw.check.lib.misc as misc
import isi.hw.check.lib.net as netlib
import isi.hw.check.lib.nettest as nettestlib

# jcc start
import sys
import signal
import time
import isi.hw.check.mfg.consts as consts
start_time = time.time()
abs_starttime = start_time
consts_nett  = consts.net_target_run_time()['long']    # jcc
#import pdb; pdb.set_trace()   #jcc
target_run_time = int ( consts_nett['target_run_time'] )     # jcc
# jcc end


def run(prefix='', mode='cluster', ifaces=None, iterations=10,
        check_only=False, allow_misconfig=False, password=None,
        options=None, logdir=None, nodes=None, nice_kill=False,
        verbose=False, threshold=0):
    """Runs nettest in the given mode on the given interfaces.
       Mode should be 'cluster' or 'intranode'. The interpretation
       of ifaces varies depending upon the mode:
       
       - cluster:   If ifaces is None, the cluster nettest will be
                    run on all configured and enabled interfaces
                    (both external and internal). Otherwise, ifaces
                    should be a list of interfaces to run. Interfaces
                    may be specified as ext1, intA, etc. Number and
                    letters are interchangeable (i.e. ext1 == extA).
                    
       - intranode: If ifaces is None, all interface families will
                    be tested. Otherwise, ifaces should be a list
                    of interface families to test (GigE or IB).

       See docstring for NettestCmdFactory for information on how
       to specify nettest flags via the options dictionary parameter.
       """
    default_options = {
        'bursts'      : 100,
        'packets'     : 10,
        'packet_size' : 1000,
        }
    if options is not None:
        default_options.update(options)
    options = default_options

    classes = {
        'cluster'   : {'tester' : nettestlib.ClusterTester,
                       'config' : netlib.ClusterConfig},
        'intranode' : {'tester' : nettestlib.IntranodeTester,
                       'config' : netlib.IntranodeConfig},
        }

    class Exit:
        pass
    
    log = loglib.push_prefix('%snett: ' % prefix)
    try:
        try:
            try:
                fails = 0
                
                if logdir is None:
                    logdir = tempfile.mkdtemp(prefix='nett-',
                                              dir=log.local_logdir())

                if not check_only:
                    log.out('Logdir      : %s' % logdir)
                    log.out('Iterations  : %s' % iterations)
                    log.out('Options:')
                    width = reduce(max, [len(x) for x in options.keys()])
                    for (key, val) in options.items():
                        log.out('- %-*s = %s' % (width, key, val))
    
                try:
                    ConfigClass = classes[mode]['config']
                    TesterClass = classes[mode]['tester']
                except KeyError:
                    log.fail('Invalid mode: %s' % mode, 0)
                    return # hard fail
    
                start_fails = log.fail_count()
                config = ConfigClass(ifaces, password, allow_misconfig,
                                     nodes).config()
                fails += log.fail_count()-start_fails
                if (fails > 0 and not allow_misconfig) or check_only:
                    raise Exit
    
                tester = TesterClass(config, options, password, logdir,
                                     nice_kill, verbose, threshold)

		# jcc start
		running_time = 0
		time_left_to_run = target_run_time
		#log.out("jcc nett :'" + str(consts_nett) + "' seconds")
		log.out('[nett] start: target_run_time=%s seconds' % (target_run_time))
		log.out('[nett]      : iterations=%s             ' % (iterations))
         	while ( running_time < time_left_to_run ):     
			#print "jcc nett batch run start_time '" + str( time.time() ) + "' seconds"
		        time_start = time.time()

                        #import pdb; pdb.set_trace()   #jcc
			#fails += tester.run(1)
			fails += tester.run(iterations)

			#print "jcc nett batch run finish_time '" + str( time.time() ) + "' seconds"
			# Adjust running_time, time_left_to_run , no 2nd batch run if not enought time is left.
                        time_finish = time.time()
			running_time = time_finish - time_start
			log.out('[nett]: current batch run time is=%s seconds' % ( running_time ))
			#log.out('jcc nett current batch run time is: %.1f seconds' % (running_time))
			time_left_to_run = time_left_to_run - running_time
			#log.out('jcc nett time_left for additional run is: %.1f seconds' % (time_left_to_run))
			log.out('[nett]: time_left for additional run is=%.1f seconds' % (time_left_to_run))
			log.out('[nett]: iterations=%s               ' % ( iterations ))

		return fails
		# jcc end   



            except misc.InfoException, e:
                fails += 1
                log.fail(e, 0)
                for line in e.info():
                    log.out('- %s' % line)
        finally:
            loglib.pop_prefix()
    except Exit:
        pass

    return fails
