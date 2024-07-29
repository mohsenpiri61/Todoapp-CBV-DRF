from celery import shared_task
from time import sleep
from .models import Task

@shared_task
def erasetasks():
    task_objs = Task.objects.all()
    task_objs.delete()
    sleep(10)
    print("Tasks removing done")