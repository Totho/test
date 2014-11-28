# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141127_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='precio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('precio', models.IntegerField()),
                ('destino', models.ForeignKey(verbose_name='usuario', to='main.Destino')),
                ('vehiculo', models.ForeignKey(verbose_name='usuario', to='main.Vehiculo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
