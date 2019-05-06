#!/usr/bin/python
import schedule
import time
import os
from datetime import datetime

def job(): #for scheduled run
    os.system('python tweeter.py')
    print(f'Process ran succesfully. \n Time: {str(datetime.now())}')

schedule.every().hour.do(job).at(':25') # run every xx:25:xx / 25 * * * * on cron 
    
while 1:
    schedule.run_pending()
    time.sleep(1)
    #print(str(schedule.Scheduler.next_run), 'scheduled to run') #??? working 