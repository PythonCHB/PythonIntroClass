import isi.gconfig as gconfig
import isi.hw.hal as hal
import isi.hw.version as hwver

import isi.hw.check.lib.mfg as mfg
import isi.hw.check.lib.misc as misc

#----------------------------------------------------------------------
# Nodeburn constants
#----------------------------------------------------------------------

# CTO: The following comments are pre-CTO, original.
#      In fact, for 6.5.2 CTO release 'long' = 6hour, not 8hour,
#      and later releases will need to support arbitarily specified
#      test time duration. TBD.
# 'full' is unique to diskscrub -- untimed test, 2-pass nodeburn
# 'long' is meant to be ~8hrs on 500GB disks
# 'short' is meant to be ~2hrs
# 'quick' is meant to be ~5min
_valid_keys = [ 'full', 'long', 'short', 'quick' ]
_default_key = 'long'

# Note we really shouldnt be running nodeburn unless in one of the
# isi_mfg_check modes (or isi_hw_check -m), but handle all cases.
# For FUT+HW+OVT (i.e. non-mfg), default to quick.
_key_lookup = {
    'mfg': 'long',
    'fut': 'quick',
    'hwc': 'quick',
    'ovt': 'quick',
    }
_script_keys = {
    'isi_mfg_check': 'long',
    'isi_ovt_check': 'quick',
    'isi_hw_check': 'quick',
    }

def get_consts_key(key=None, mode=None):
    # Ref misc._valid_modes for all possible global modes
    # Always returns a valid nodeburn consts key for mode
    # First see if given key is valid ("check" function)
    # NOTE this is the "usual use case", ref diskscrub or safe.net
    # If not, see if valid mode supplied
    # If not, try global mode
    # Try a mode-to-nodeburn-consts-key mapping lookup
    # If not, try valid known script type lookup
    # If not, use default
    if not key is None and key in _valid_keys:
        return key
    if mode is None or not misc.valid_mode(mode):
        mode = misc.get_mode()
    if mode in _key_lookup:
        key = _key_lookup[mode]
    if not key in _valid_keys:
        for script in _script_keys:
            if misc.script_is(script):
                key = _script_keys[script]
                break
    if not key in _valid_keys:
        key = _default_key
    return key

# Network Test
# IB:
# - 150 IB intranode ttcp iterations is ~4hours
# - 900 IB+GigE intranode nettest iterations is ~4hours
# GigE:
# - 3500 GigE intranode nettest iterations ~8hours
# Note that safe.ttcp will not actually run intranode non-IB ttcp
# Reduce these numbers by some 10-20% to avoid 8hour timeouts
def net():
    if not hal.supportsCto():
        if hwver.netiface_hasIB:
            consts = {
                'long'  : {'mode'            : 'intranode',
                           'nett_iterations' : 800, # was 900     # jcc was 800
                           'ttcp_iterations' : 125, # was 150
                           },
                'short' : {'mode'            : 'intranode',
                           'nett_iterations' : 20, 
                           'ttcp_iterations' : 100, # was 150
                           },
                'quick' : {'mode'            : 'intranode',
                           'nett_iterations' : 1,
                           'ttcp_iterations' : 2, 
                           },
                }
        else:
            consts = {
                'long'  : {'mode'            : 'intranode',
                           'nett_iterations' : 3000, # was 3500
                           'ttcp_iterations' : 0,
                           },
                'short' : {'mode'            : 'intranode',
                           'nett_iterations' : 500,  # was 0
                           'ttcp_iterations' : 0,
                           },
                'quick' : {'mode'            : 'intranode',
                           'nett_iterations' : 5,
                           'ttcp_iterations' : 0, 
                           },
                }
    else: # CTO
        # See bug 76718, bug 76868; For now, just scale pre-CTO values
        # by a factor of 2: If pre-CTO is 8h, 8h/2 = 4h < 6h
        if hwver.netiface_hasIB:
            consts = {
                'long'  : {'mode'            : 'intranode',
                           'nett_iterations' : 800 // 2,           # jcc was 800
                           'ttcp_iterations' : 125 // 2,
                           },
                'short' : {'mode'            : 'intranode',
                           'nett_iterations' : 20 // 2, 
                           'ttcp_iterations' : 100 // 2,
                           },
                'quick' : {'mode'            : 'intranode',
                           'nett_iterations' : 1,
                           'ttcp_iterations' : 2, 
                           },
                }
        else:
            consts = {
                'long'  : {'mode'            : 'intranode',
                           'nett_iterations' : 3000 // 2,
                           'ttcp_iterations' : 0,
                           },
                'short' : {'mode'            : 'intranode',
                           'nett_iterations' : 500 // 2,
                           'ttcp_iterations' : 0,
                           },
                'quick' : {'mode'            : 'intranode',
                           'nett_iterations' : 5,
                           'ttcp_iterations' : 0, 
                           },
                }
    return consts

# LCD Test
# (Pre-CTO) 4000 iterations is about 8 hours
# Observed: Bug24933,Bug24981: short600~60-70m; long4000~90%(8h)
def lcd():
    if not hal.supportsCto():
        # Leave legacy alone, unchanged
        consts = {
            'long'  : {'iterations': 4000},
            'short' : {'iterations': 600},
            'quick' : {'iterations': 2},
            }
    else: # CTO
        # Bug 76718 comment 5: CTO: Targeting 6 hour long runtime: 
        # using 3200 iters, scale short iters accordingly: 3200./4000*600=480
        consts = {
            'long'  : {'iterations': 5000},           # jcc was 3200
            'short' : {'iterations': 480},
            'quick' : {'iterations': 2},
            }
    return consts

# For 'long' (nodeburn), only: Changing 12500 to 700 iterations to target
# 20 minutes based on empirical run times of approx 34 iters/minute, and
# desired 20 minutes run time in bug 89237 (see also bug 84688).
# Leaving 'short' 4200 iterations unchanged at this time.
def memscrub():
    consts = {
        'long' : {'iterations' : 700, 'fixed_pattern' : True,
                                       'random_pattern' : True },
        'short': {'iterations' : 4200 },
        'quick': {'iterations' : 5 },
    }
    return consts

# XXX_BUG70925 : NVRAM Test: long/short/quick: need different RF values?
# NVRAM Test
# 500 iterations is ~8hrs
# Observed: Bug24933,Bug24981: short80~100-110m; long500~70%(8h)
# ==> Bug24933 dec 2006 pre-dates Belknap (June 2007), the numbers 
#     above are for MicroMemory NVRAM!
# Observed: Bug75496: Graham/Belknap: long500: 17s ea=2.4h, ~30%(8h)
def nvram():
    if not hal.supportsCto():
        # Arguably this should be fixed for pre-CTO Legacy Cases,
        # Belknap vs. MicroMemory, and for Belknap: dd vs memtest
        # But let's just leave well enough alone, no changes.
        consts = {
            'long'  : {'iterations': 500, 'checkpoint': 500//2},
            'short' : {'iterations': 80, 'checkpoint': 80//2},
            'quick' : {'iterations': 2, 'checkpoint': 2//2},
            }
    else: # CTO
        # Handle Belknap vs Rocketfuel individually
        # ASSUMING ONLY dd-based nvramscrub testing is done, in CTO forward
        # IF we start using isi_memtest again, add code here to distinguish?
        nvram_consts = {
            hwver.NVR_UNKNOWN: {
            'long'  : {'iterations': 0, 'checkpoint': 0},
            'short' : {'iterations': 0, 'checkpoint': 0},
            'quick' : {'iterations': 0, 'checkpoint': 0},
            },
            hwver.NVR_MT25208: {
            # See bug 76718 comment 5
            # With dd, Wingfoot,  500iter=7927s => 6h=1362iter, use 1200
            # With dd, Blueflame, 500iter=7303s => 6h=1385iter, use 1200
            'long'  : {'iterations': 3000, 'checkpoint': 600},           # jcc was 1200
            'short' : {'iterations':  400, 'checkpoint': 200},
            'quick' : {'iterations':    2, 'checkpoint':   1},
            },
            }
        if hal.getNvramType() in nvram_consts:
            consts = nvram_consts.get(hal.getNvramType())
        else:
            # Including NVR_MM5425, NVR_VMWARE, NVR_ROCKETFUEL
            consts = nvram_consts.get(hwver.NVR_UNKNOWN)
    return consts
        
    

# EEPROM Test
# NOTE: we don't have EEPROM scrub in mfg.long.nodeburn at this time.
# If we ever implement lib.eeprom Tester data_multiplier, put that here?
# Also, (alt to mult), for 'quick', we want data_offset/length...
# Remember, test passes also include "restore" rd and wr times (wrappers)
# Some quick single-pattern, single-pass, limted-length test runs:
# Linear scaling, as expected!
# Size: (rd, wr): Total Test Time (incl initial/final restore rd+wr)
#  1KB: ( 2, 20): 2*(2+20)  =  44s
#  4KB: ( 6, 82): 2*(6+82)  = 176s, actual was 174s <-- Approx 3 min
# 16KB: (22,328): 2(*22+328)= 700s ~ 12m
# 64KB: 2*700=1400s ~ 24m
# A single full 64KB single-pattern pass should take about: 24min
#
# 'long'(8h): , 'short'(2h): , 'quick'(5m): x1/~4KB=~
def eeprom():
    if not hal.supportsCto():
        consts = {
            'long'  : {'iterations':  16, 'length':None },
            'short' : {'iterations':   4, 'length':None },
            'quick' : {'iterations':   1, 'length':4*1024 },
            }
    else: # CTO
        # See comments at top; We're not actively using this,
        # so for CTO release just scale (6 hour nodeburn, not 8 hour)
        consts = {
            'long'  : {'iterations':  12, 'length':None },
            'short' : {'iterations':   4, 'length':None },
            'quick' : {'iterations':   1, 'length':4*1024 },
            }
    return consts

# Fork Unit Test (debug only)
# Be careful! Exponential growth of process tree...
def fork_unit():
    consts = {
        'long'  : {'iterations':3,'delay':60,'children':3,'levels':3},
        'short' : {'iterations':3,'delay':30,'children':3,'levels':3},
        'quick' : {'iterations':3,'delay':10,'children':2,'levels':2},
        }
    return consts

# Diskscrub
# 'full' is the a full, 2-pass nodeburn
# 'long' is meant to be ~8hrs on 500GB disks
# 'short' is meant to be ~2hrs
# 'quick' is meant to be ~5min
#
# Note we use a dictionary for the 'stripe_mult' elements, keyed
# off disk type (see driveinfo,'model'), to account for different
# drive size/speeds -- thus different drives can run for approx.
# the same amount of time.
#
# 'Default': Just something reasonable for unrecognized drives
# For 'Default' values, assume typical max size is 2TB
#
# Create a dictionary of the stripe multipliers from the global drive
# configuration tree based on the specified type of diskscrub pass being
# performed. The dictionary that is created uses drive model for a key
# and the stripe multiplier as the value.
#
# Changes for CTO/Choprocks/6.5.2 release, going forward:
# a) Eliminate 'scrub_multipliers' entries for 'full_pass', 'quick_pass'
#    from drive_config.gc, since these are by definition constants
# b) For legacy purposes, leave the 'long_pass', 'short_pass' entries
#    and values, unchanged, for 6.5.2 release
# c) Shortly after 6.5.2 release, audit these long|short multipliers
#    values and actual test time results from logserver data, and
#    re-set these to actual scaled/tuned values that properly achieve
#    test time goals (long=8h, short=2h).
# d) For CTO case, start using new 'scrub_multipliers' value/method:
#    Instead of specific multiplier values that are only tuned for
#    specific run times (e.g. long=8h), use a normalized bandwidth
#    factor that can be used to calculate a required stripe_multiplier
#    for a desired (specified) run time.
# e) Long term, we could similarly use normalized bandwidth factor
#    for legacy (pre-CTO) nodes and drives, TBD.
#
def get_stripe_mult(pass_type=None):
    multipliers = {}
    pass_key = None

    if pass_type in _valid_keys:
        pass_key = '%s_pass' % pass_type
        defaults = {'full':1, 'long':500, 'short':2000, 'quick':10}
        default = defaults[pass_type]
    else:
        print 'unrecognized stripe multiplier pass type: %s' % pass_type
        raise ValueError

    constant_scrub_multipliers = {'full_pass':1, 'quick_pass':10}

    if pass_key is not None:
        multipliers['Default'] = default
        multipliers['bandwidth'] = {}
        ctx = gconfig.open(hal.gcfg_driveconfig).ctx_new()
        dcs = ctx.read('driveconfigs')
        for dc in dcs:
            key = dc.get('model')
            if pass_key in constant_scrub_multipliers:
                scrub_multipliers = constant_scrub_multipliers
            else:
                scrub_multipliers = dc.get('scrub_multipliers')
            if not key or not scrub_multipliers:
                print 'unregognized key and/or scrub_multipliers in drive ' \
                      'configuration'
                raise ValueError
            multipliers[key] = scrub_multipliers[pass_key]
            scrub_bandwidth = scrub_multipliers.get('bandwidth')
            if scrub_bandwidth:
                multipliers['bandwidth'][key] = scrub_bandwidth

    return multipliers


def norm_bw_calc(elapsedtime, pass_count, mult, blks, blksize=512, iorw=2):
    # Size_Bytes / Time_Sec / Mult_Unity = Bytes/Sec
    etime = float(elapsedtime) / pass_count
    bytes = float(blks) * blksize * iorw
    if etime == 0 or etime == 0.0 or mult == 0 or mult == 0.0:
        bw = -1
    else:
        bw = int(round(bytes / etime / mult))
    if bw < 1:
        bw = 1
    return bw

def stripe_mult_calc(targettime, pass_count, bw, blks, blksize=512, iorw=2):
    # Size_Bytes / Time_Sec / BW_BytesPerSec = B/Sec / B/Sec = Unity
    etime = float(targettime) / pass_count
    bytes = float(blks) * blksize * iorw
    if etime == 0 or etime == 0.0 or bw == 0 or bw == 0.0:
        mult = 1 # 1 == effectively no stripe multiplier
    else:
        # Let's try removing round, so we always do floor; minimal mult value
        # This is apropos for e.g. fast SSD drives; instead of round(1.86)=2,
        # we'll get 1, which will better use the available time? hopefully?
        # In fact, let's make this nonlinear. Only use floor for "low" values.
        mult = bytes / etime / bw
        if mult < 3:
            mult = int(mult) # floor
        else:
            mult = int(round(mult))
    if mult < 1:
        mult = 1
    return mult

def estimated_elapsed_time(mult, pass_count, bw, blks, blksize=512, iorw=2):
    # Size_Bytes / Mult_Unity * Pass_Unity / BW_BytesPerSec = B / B/Sec = Sec
    bytes = float(blks) * blksize * iorw
    if mult == 0 or mult == 0.0 or bw == 0 or bw == 0.0:
        etime = -1
    else:
        etime = int(round(bytes / mult * pass_count / bw))
    return etime



# Note for simplicity of diskscrub.maxtime() calculations, we will pass
# the 'default_const_key' argument to diskscrub.run() -- and all nodeburn
# tests -- automatically (Ref mfg.long.nodeburn)
def disk():
    # all disk consts keys use partition = '' except quick
    # all disk consts keys use type = sequential
    # all disk consts keys use pass_count = 2
    default = lambda key: {
        'const_key': key,
        'partition': '',
        'type': 'sequential',
        'pass_count': 2,
        'stripe_mult': get_stripe_mult(key),
        }
    consts = dict([(key, default(key)) for key in _valid_keys])
    consts['quick']['partition'] = mfg.scratch_partition()
    return consts

# Special case args, for Drive Burn-In specific diskscrub menus
# (Burnin, "other" menu, or top-level Drive Burnin menu)
def drive_burnin_multi_pass_args():
    consts = disk()['full']
    return consts

def drive_burnin_single_pass_args():
    consts = disk()['full']
    consts.update({'pass_count': 1})
    return consts

# Note 'full' is untimed, return None == No Timeout handler
max_runtimes = {
    'full':  None,
    'long':  8*60*60, # For CTO 6.5.2, this should actually be 6hour.
    'short': 2*60*60,
    'quick': 5*60,
    }

# This dict consts.extra_runtime specifies a safety margin for nodeburn
# max_runtimes, to prevent tests that run -slightly- longer than goal
# from Timeout FAILUREs.
extra_runtime = {
    'full':  None,
    'long':  15*60,
    'short': 5*60,
    'quick': 30,
    }

# run_type is just the consts_keys above...
def get_max_runtime(run_type):
    maxtime = None
    try:
        maxtime = max_runtimes[run_type]
        # Add any extra buffer time, if specified
        if not maxtime is None:
            maxtime += extra_runtime[run_type]
    except (KeyError, TypeError):
        # KeyError if unspecified run_type
        # TypeError if 'None' is specified (int + NoneType)
        pass
    return maxtime

# Fibre Channel Loopback
def fcloop():
    consts = {
        'long'  : {'target_minutes': 240}, # ~4h
        'short' : {'target_minutes': 5},
        'quick' : {'target_minutes': 2},
        }
    return consts




# jcc start
import sys

nb_time_mult = 1    # default setting, needed.
argv = sys.argv
#print 'argv = %s' % argv 
i = 0
while i < len(argv):
    if argv[i][:12] == 'nb_time_mult':
	    multiplier = argv[i][12:] 
	    #print ' argv[i]      = %s' % (argv[i])
	    #print ' argv[i][:12] = %s' % (argv[i][:12])
	    #print ' multiplier   = %s' % (argv[i][13:])
            nb_time_mult = float(argv[i][13:])
	    #print ' nb_time_mult   = %s' % (nb_time_mult)
	    break
    else:
        i += 1 

#print ' nett time is    = %s' % (2     * nb_time_mult)
#exit

def nvramscrub_target_run_time():
   consts = {
       'long'  : {'target_run_time'     :  23400*nb_time_mult},    # jcc 6.5hr=6.5*60*60=23400
       'short' : {'target_run_time'     :  10800},                 # jcc 3.0hr=3.0*60*60=10800
       'quick' : {'target_run_time'     :   5400},                 # jcc 1.5hr=3.5*60*60=5400 
   }
   return consts


def lcd_target_run_time():                                         # jcc: adjust iterations as needed
   consts = {
       'long'  : {'target_run_time'     :  23400*nb_time_mult},    # jcc 6.5hr=6.5*60*60=23400
       'short' : {'target_run_time'     :  10800},                 # jcc 3.0hr=3.0*60*60=10800
       'quick' : {'target_run_time'     :   5400},                 # jcc 1.5hr=1.5*60*60=5400 
   }
   return consts

def memscrub_target_run_time():                                    # jcc: adjust iterations as needed
   consts = {
       'long'  : {'target_run_time'     :   1500*nb_time_mult},    # jcc 25-min=25*60=1500
       'short' : {'target_run_time'     :    900},                 # jcc 15-min= 15*60=900
       'quick' : {'target_run_time'     :    480},                 # jcc 8-min=8*60=480  
   }
   return consts


def disk_target_run_time():
   consts = {
       'long'  : 21600*nb_time_mult,                               # jcc 6.0hr=6.0*60*60=21600
       'short' : 30                                                # jcc 3.0hr=3.0*60*60=10800
   }
   return consts

def net_target_run_time():                                         # jcc: adjust iterations as needed
   consts = {
       'long'  : {'target_run_time'     :  21600*nb_time_mult},    # jcc 6.0hr=6.0*60*60=21600
       'short' : {'target_run_time'     :  10800},                 # jcc 3.0hr=3.0*60*60=10800
       'quick' : {'target_run_time'     :   5400},                 # jcc 1.5hr=1.5*60*60=5400
   }
   return consts


# jcc end
