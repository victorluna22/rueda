# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, b'Cadastro'), (2, b'Atualiza\xc3\xa7\xc3\xa3o'), (3, b'Dele\xc3\xa7\xc3\xa3o')]),
            preserve_default=True,
        ),
    ]
