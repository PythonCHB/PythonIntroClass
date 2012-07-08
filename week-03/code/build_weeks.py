#!/usr/bin/env python

"""
script to build the framework for all the class presentations
"""

import os
import datetime


def make_date_string(week_num):
    if week_num > 2: # skipping July 4th
        week_num += 1
    if week_num > 8: # skipping Aug 22nd
        week_num += 1
    start = datetime.date(2012, 6, 20)
    delta = datetime.timedelta(days=7*(week_num-1))
    date = start + delta
    return date.strftime("%B %d, %Y")

    
def create_dir(week_num):
    dir_name = "week-%02i"%week_num
    try:
        os.mkdir(dir_name)
    except OSError:
        pass # directory already exists
    # create a code dir
    try:
        os.mkdir(os.path.join(dir_name, 'code'))
    except OSError:
        pass # dir already there
    # load the template
    template = file(os.path.join("week-03", "presentation-template.tex"), 'rU' ).read()
    
    #insert the week number
    template = template.replace("the_week_number", `week_num`)
    #insert the date 
    template = template.replace("the_date_string", make_date_string(week_num))
    
    # write it out:
    file_name = "presentation-week%02i.tex"%week_num
    file(os.path.join(dir_name, file_name),'w').write(template)
    
if __name__ == "__main__":
    for week_num in range(4,11):
        create_dir(week_num)    
    
