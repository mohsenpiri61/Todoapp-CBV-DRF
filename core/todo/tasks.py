from celery import shared_task
from time import sleep


@shared_task
def erasetasks():
    sleep(600)
    print("Tasks removing done")