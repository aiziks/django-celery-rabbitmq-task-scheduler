from __future__ import absolute_import, unicode_literals

from celery import shared_task

import time


@shared_task
def add(x , y):
    # time.sleep(5)    
    return x + y

@shared_task
def bday():
    # time.sleep(5)    
    return "Today is your birthday; Rejoice with me..."




