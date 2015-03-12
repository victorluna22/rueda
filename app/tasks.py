from __future__ import absolute_import
from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
# from myapp.utils import scrapers
from celery.utils.log import get_task_logger
from datetime import datetime
from celery import shared_task
 
 
logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@task()
def create_person():
	from app.models import Person
	from random import randint
	import urllib2, json
	response = urllib2.urlopen('http://api.randomuser.me/')
	data = json.load(response)
	name = "%s %s" % (data['results'][0]['user']['name']['first'], data['results'][0]['user']['name']['last'])
	Person.objects.create(text=name, number=randint(1,999999))
	logger.info("%s" % name)

 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*/2", day_of_week="*")))
def scraper_example():
	logger.info("Start task")
	for i in range(1000):
		fs = create_person.subtask()
		fs.delay()
	
	logger.info("Task finished")
