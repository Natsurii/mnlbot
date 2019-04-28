#!/usr/bin/python
import schedule
import time
import os

os.system('python poster.py') #For script boot run

def job(): #for scheduled run
    os.system('python poster.py')
    print('Process ran succesfully.')

schedule.every().hour.do(job)
    
while 1:
    schedule.run_pending()
    time.sleep(1)