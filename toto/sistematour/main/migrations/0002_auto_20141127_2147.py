# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='direccion',
        ),
        migrations.AddField(
            model_name='destino',
            name='foto',
            field=models.ImageField(default='', upload_to=b'perfil', verbose_name=b'foto de perfil', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='foto',
            field=models.ImageField(default='', upload_to=b'perfil', verbose_name=b'foto de perfil', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destino',
            name='picoPlaca',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
