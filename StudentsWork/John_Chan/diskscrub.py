import isi.hw.hal as hal

import isi.hw.check.lib.driveinfo as drivelib
import isi.hw.check.lib.log as loglib
import isi.hw.check.lib.watchdog as watchdog
import isi.hw.check.mfg.consts as consts
import isi.hw.check.unsafe.long.diskscrub as diskscrub

# jcc start
import time
import isi.hw.check.mfg.consts as consts
start_time = time.time()
abs_starttime = start_time
#disk_target = consts.disk_target_run_time()['long']    # jcc
#disk_target_run_time = int ( disk_target['target_run_time'] )     # jcc
#import pdb; pdb.set_trace()   #jcc
# jcc end

def maxtime(const_key,
            pass_count, partition, type, stripe_mult):
    """Determine the worst case max run time for this module.
       Returns None if no timeout should be expected."""
    output_dir = prompt_for_range = None
    return diskscrub.maxtime(const_key,
                             partition, type,
                             pass_count, output_dir,
                             stripe_mult, prompt_for_range)

def get_stripe_mult_info(stripe_mult_consts,
                         runtime=None, pass_count=2):
    log = loglib.get_logger()

    # Get appropriate stripe multiplier override value (from options)
    stripe_mult_override = False
    if log.get_data_value('diskscrub_mult'): # Non-zero, Non-None
        stripe_mult_override = log.get_data_value('diskscrub_mult')
    if log.get_data_value('diskscrub_full'):
        stripe_mult_override = 1 # 100%, full drive testing

    # Get disk devices
    try:
        driveinfo = drivelib.DriveInfo()
    except drivelib.DriveInfoException, e:
        log.fail('Unable to get disk information: %s' % e, 0)
        return # hard fail

    # Get disk-specific stripe_mult values from driveinfo,
    # based on input 'stripe_mult_consts' dictionary
    stripe_mult_info = {}
    
    # DriveInfo Iterative Function
    #################################################################
    def get_stripe_mult_info_iter(location, info):
        if stripe_mult_override:
            stripe_mult = stripe_mult_override
        elif info['model'] in stripe_mult_consts:
            stripe_mult = stripe_mult_consts[info['model']]
            # If we have runtime specified, try to calculate stripe_mult
            if runtime and 'bandwidth' in stripe_mult_consts:
                bandwidth = stripe_mult_consts['bandwidth']
                if info['model'] in bandwidth:
                    bw = bandwidth[info['model']]
                    if bw: # Default gconfig value is 0 for unspecified
                        blks = info['blocks']
                        stripe_mult = consts.stripe_mult_calc(
                            runtime, pass_count, bw, blks)
        else:
            log.fail('Unknown drive model "%s" found in %s' %
                     (info['model'], info['bay_str']), 0)
            stripe_mult = stripe_mult_consts['Default']
        stripe_mult_info[location['bay']] = stripe_mult
    #################################################################

    driveinfo.iter(get_stripe_mult_info_iter)
    if len(stripe_mult_info) == 0:
        log.fail('No valid drive models found for testing.', 0)
        return # hard fail

    return stripe_mult_info

def run(const_key='long',
        pass_count=None, partition=None, type=None,
        stripe_mult=None,
        runtime=None):
    #import pdb; pdb.set_trace()   #jcc
    if None in [pass_count, partition, type, stripe_mult]:
        consts_disk = consts.disk()
        if not const_key in consts_disk:
            log = loglib.get_logger()
            log.fail('Unknown Diskscrub key "%s"' % const_key, 0)
            return 1 # hard fail
        consts_disk = consts_disk[const_key]
        if pass_count is None:
            pass_count = consts_disk['pass_count']
        if partition is None:
            partition = consts_disk['partition']
        if type is None:
            type = consts_disk['type']
        if stripe_mult is None:
            stripe_mult = consts_disk['stripe_mult']

    # For CTO, and eventually everyone (TBD), new stripe_mult method:
    # Rather than hard-coding 'long' and 'short' stripe_mult values
    # that are hand-tuned to specific runtimes (e.g. long=8hour),
    # use a normalized bandwidth factor, per drive, and the desired
    # test runtime to calculate an appropriate stripe_mult value.
    # (However, there may be complications; e.g, normalized BW factor
    # for a given drive may be different for different platforms,
    # such as a 3.5" SATA drive on a Graham vs. Wingfoot. For now,
    # only using this for CTO, we don't have any such problems.)
    # For CTO 6.5.2 release: default long=6hour, not 8hour
    cto_default_runtimes = {'long':6*60*60, 'short':2*60*60}

    # jcc start
    # Hard to put timer, fork() and singal handingly limiter.
    cto_default_runtimes = consts.disk_target_run_time()
    log = loglib.get_logger()
    #import pdb; pdb.set_trace()   #jcc
    # jcc end

    if hal.supportsCto() and const_key in cto_default_runtimes:
        if runtime is None:
            runtime = cto_default_runtimes.get(const_key)

    result = 0
    log.out('[diskscrub] start: target_run_time is %s seconds;' % (runtime)) # jcc 

    # Find an unused diskscrub dir on the remote server
    localdir = loglib.get_logger().get_unused_logdir('diskscrub', create=False)
    if localdir is None:
        return 1 # hard fail

    # Extract disk-specific stripe_mult values
    # Use local copy stripe_mult_info for PyChecker warning
    stripe_mult_info = get_stripe_mult_info(stripe_mult, runtime, pass_count)
    if stripe_mult_info is None:
        return 1 # hard fail

    args = {
        'const_key'        : const_key,
        'partition'        : partition,
        'scrub_type'       : type,
        'pass_count'       : pass_count,
        'output_dir'       : localdir,
        'prompt_for_range' : False,
        }
    # For PyChecker warning: Don't have explanation, but assigning
    # this value in args declaration above causes this warning:
    #  Modifying parameter (stripe_mult) with a default value may have
    #  unexpected consequences
    args['stripe_mult'] = stripe_mult_info

    watcher = watchdog.CPUIdleWatchdog(interval_minutes=10,max_fails=3,
                                       max_cpu=98.0)
    watcher.start('Starting CPU watchdog')
    try:
        result = diskscrub.run(**args)
    finally:
        watcher.stop('Stopping CPU watchdog')

    return result
