import os
import time

import isi.app.lib.procs as procs
import isi.hw.hal as hal
import isi.hw.version as hwver
import isi.ui.lcd.display as display
from isi.ui.lcd import LCDError

import isi.hw.check.lib.filenames as files
import isi.hw.check.lib.log as loglib

# jcc start
import sys
import signal
import time
import isi.hw.check.mfg.consts as consts
start_time = time.time()
abs_starttime = start_time
consts_lcd  = consts.lcd_target_run_time()['long']    # jcc
#import pdb; pdb.set_trace()   #jcc
target_run_time = int ( consts_lcd['target_run_time'] )     # jcc
# jcc end


def skip():
    return hal.getLcdType() in [ hwver.LCDVER_UNKNOWN ]

def lcd_d_stop():
    kill_cmd = 'killall -KILL %s' % os.path.basename(files.commands['lcd'])
    procs.get_cmd_output(kill_cmd)
    procs.get_cmd_output(kill_cmd)

def lcd_d_start():
    procs.get_cmd_output('%s start' % files.commands['lcd'])

def run(reps = None):
    log = loglib.get_logger()
    
    if reps == None:
        while 1:
            reps_default = 5
            reps = log.prompt('How many iterations would you like ' +
                              'performed? (%d): ' %
                              reps_default)
            try:
                if reps == '':
                    reps = reps_default
                reps = int(reps)
                if reps <= 0:
                    raise ValueError
                log.out('')
                break
            except (ValueError, TypeError):
                log.out('Invalid entry. Please enter a positive integer.')

    log.out('Test iterations: %d' % reps)
    log.out('')

    log.out('Connecting to LCD')
    # Kill isi_lcd_d, no questions asked
    lcd_d_stop()
    time.sleep(10)

    # Attempt to get our LCD object
    try:
        lcd = display.getDisplay()
    except Exception, e:
        log.fail('Unable to initialize LCD object', 0)
        if e:
            log.fail('%s' % e, 0)
        lcd_d_start()
        return
    # in case we don't have an LCD display, or it is unresponsive,
    # try to catch this and fail out gracefully
    import termios
    try:
        lcd.open()
    except (IOError, termios.error):
        log.fail('I/O Failure connecting to LCD')
        return # hard fail
    except LCDError, e:
        if "The display board is not responding" in e.args:
            log.fail(e)
            return # hard fail
        raise
    lcd.clear()

    # build a list of characters to print to the screen
    charlist = []
    for ascii in range(ord('A'), ord('Z')+1):
        charlist.append('%c' % ascii)
    for ascii in range(ord('a'), ord('z')+1):
        charlist.append('%c' % ascii)
    for ascii in range(ord('0'), ord('9')+1):
        charlist.append('%c' % ascii)
    charlist_len = len(charlist)

    log.out('[lcdscrub] start: target_run_time is=%s seconds' % ( target_run_time ))

    for i in range(reps):
        try:
            log.out('Iteration %d of %d' % (i+1, reps))
            char_index = i % charlist_len
            out_str = ''
            for dummy in range(lcd.NUM_COLS):
                out_str += '%s' % charlist[char_index]
            for row in range(lcd.NUM_ROWS):
                lcd.showText(out_str, 0, row)
            lcd.refresh()
            time.sleep(2)
            # clear screen
            lcd.clear()
            lcd.refresh()
            time.sleep(2)
            # turn all pixels on
            lcd.fillRect(0, 0, lcd.NUM_PIXELS_W-1, lcd.NUM_PIXELS_H-1,
                         lcd.COLOR_ON)
            lcd.refresh()
            time.sleep(2)

            # jcc start
            time_now    = time.time() - abs_starttime
	    time_remain = target_run_time - time_now
	    if ( time_now < target_run_time ):
		#print "jcc lcdscrub: remaining_time '" + str( time_remain ) + "' seconds"
		pass
            else:
		log.out('[lcdscrub] end: target_run_time=%s seconds is reached, exited' % ( target_run_time ))
		break
            # jcc end

        except LCDError, e:
            log.fail(e, 0)

    # finish up and restart isi_lcd
    log.out('Disconnecting from LCD')
    lcd.clear()
    lcd.refresh()
    lcd.close()
    lcd_d_start()
    log.out('LCD scrub completed')
