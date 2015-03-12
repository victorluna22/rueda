# -*- coding: utf-8 -*-
from django.dispatch.dispatcher import Signal


def post_save_person(sender, instance, created, **kwargs):
	from .models import Log, CREATE, EDIT
	if created:
		Log.objects.create(text='Pessoa de nome "%s" cadastrado. Id: %d' % (instance.text, instance.id), type=CREATE)
	else:
		Log.objects.create(text='Pessoa de nome "%s" atualizado. Id: %d' % (instance.text, instance.id), type=EDIT)



def post_delete_person(sender, instance, **kwargs):
	from .models import Log, DELETE
	Log.objects.create(text='Pessoa de nome "%s" removido. Id: %d' % (instance.text, instance.id), type=DELETE)	

