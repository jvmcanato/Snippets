# Method to get time and date in the form: ['y-m-d', 'h-m-s']
# @author: João Vitor Mussel Canato

import datetime

def dateTimeNow():
    return datetime.datetime.now().isoformat().split('.')[0].split('T')

print(dateTimeNow())
