import time
import datetime

def get_timestamp(string, date_format):
    '''Docstring para get_timestamp'''
    return time.mktime(datetime.datetime.strptime(string, date_format))
