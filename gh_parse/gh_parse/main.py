#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Usage: gh_parse <start> <end>

Examples:
  gh_parse datetime1 datetime2

Options:
    -h --help     Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
from gh_parse import __version__
from termcolor import cprint
import calendar
# def parse(start,end):
# for i, line in enumerate(lines):


def start():
    version = ".".join(str(x) for x in __version__)
    arguments = docopt(__doc__, version=version)
    ## actually should parse the start month
    ## parse the end month, and get the range of months between to loop over
    start = arguments.get('<start>', None)
    end = arguments.get('<end>', None)
    BASE = "http://data.githubarchive.org/"
    #set date ints
    start_year = int(start[0:4])
    end_year = int(end[0:4])
    start_month = int(start[5:7])
    end_month = int(end[5:7])
    # parse the months and give range(startmonth, endmonth+1) --> range not inclusive
    if (start_year!=end_year):
        cprint("start and end years must match", 'red')
        return
    year = start_year
    if(start_month>end_month):
        cprint("start month must be less than end month")
        return
    months = range(start_month,end_month+1)
    months_length = len(months)
    
    for month_index, month in enumerate(months, start=1):
        month = str(month) if month > 9 else "0" + str(month)

        if (months_length == month_index):
            # have range go to last day
            days = int(end[8:10])
        else:
        # else have range to to full days in month
            days = calendar.monthrange(year,int(month))[1]

        for day in range(1, days+1):
            day_str = str(day) if day > 9 else "0" + str(day)
            for hour in range(0, 24):
                cprint(str(BASE) + str(year) + "-" + month + "-" + day_str + "-" + str(hour) + ".json.gz")
    # cprint(arguments.get('<start>'), 'blue')
    # cprint(arguments.get('<end>'),'red')
