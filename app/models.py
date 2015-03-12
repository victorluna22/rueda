#coding: utf-8

from django.db import models
from django.db.models.signals import post_save, post_delete
from .signals import post_save_person, post_delete_person

class Person(models.Model):
	number = models.IntegerField(u'Número')
	text = models.CharField(u'Texto', max_length=255, db_index=True)

	def __unicode__(self):
		return "%s - %s" % (self.number, self.text)


CREATE = 1; EDIT = 2; DELETE = 3;
ACTION_TYPES = (
    (CREATE, "Cadastro"),
    (EDIT, "Atualização"),
    (DELETE, "Deleção"),
    )

class Log(models.Model):
	text = models.CharField('Log', max_length=255)
	type = models.IntegerField(choices=ACTION_TYPES, default=CREATE)

	class Meta:
		ordering = ["-id"]

	def __unicode__(self):
		return self.text

	def get_type(self):
		return dict(ACTION_TYPES)[self.type]



post_save.connect(post_save_person, sender=Person, dispatch_uid='person.post_save')
post_delete.connect(post_delete_person, sender=Person, dispatch_uid='person.post_delete')