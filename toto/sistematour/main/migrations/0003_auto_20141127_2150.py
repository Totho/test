# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141127_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=10, verbose_name='placa'),
            preserve_default=True,
        ),
    ]
