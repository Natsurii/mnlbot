#!/usr/bin/python
import time
from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python tweeter.py')  
job.setall('22 * * * *')

cron.write()

'''import schedule
import time
import os

os.system('python tweeter.py') #For script boot run

def job(): #for scheduled run
    os.system('python tweeter.py')
    print('Process ran succesfully.')

schedule.every().hour.do(job)
    
while 1:
    schedule.run_pending()
    time.sleep(1)'''