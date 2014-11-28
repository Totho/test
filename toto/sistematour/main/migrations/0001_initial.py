# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('numeroCuenta', models.IntegerField(max_length=40)),
                ('banco', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('tipoLicencia', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('lugar', models.CharField(max_length=50)),
                ('picoPlaca', models.IntegerField(max_length=2)),
                ('requerimiento', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('direccion', models.CharField(default=b'', max_length=60, null=True, verbose_name='direccion', blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=60, null=True, verbose_name='ciudad', blank=True)),
                ('departamento', models.CharField(default=b'', max_length=60, null=True, verbose_name='departamento', blank=True)),
                ('barrio', models.CharField(default=b'', max_length=60, null=True, verbose_name='barrio', blank=True)),
                ('pais', models.CharField(default=b'', max_length=60, null=True, verbose_name='pais', blank=True)),
                ('select', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaSalida', models.DateTimeField()),
                ('conductor', models.CharField(max_length=20)),
                ('vehiculoPlaca', models.IntegerField(max_length=10)),
                ('destino', models.CharField(max_length=40)),
                ('cliente', models.ForeignKey(verbose_name='usuario', to='main.Cliente')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('monto', models.IntegerField(max_length=20)),
                ('saldo', models.IntegerField(max_length=20)),
                ('tipoPago', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(verbose_name='usuario', to='main.Cliente')),
                ('orden', models.ForeignKey(verbose_name='orden', to='main.Orden')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('celular', models.CharField(max_length=50, null=True, verbose_name='celular', blank=True)),
                ('cedula', models.CharField(max_length=20, null=True, verbose_name='cedula', blank=True)),
                ('foto', models.ImageField(upload_to=b'perfil', verbose_name=b'foto de perfil', blank=True)),
                ('direccion', models.ForeignKey(verbose_name='Direccion', to='main.Direccion')),
                ('usuario', models.OneToOneField(verbose_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=50, verbose_name='codigo')),
                ('placa', models.IntegerField(max_length=10, verbose_name='placa')),
                ('tipo', models.CharField(max_length=20, verbose_name='tipo')),
                ('cupo', models.IntegerField(max_length=3, verbose_name='cupo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='destino',
            name='direccion',
            field=models.ForeignKey(verbose_name='Direccion', to='main.Direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conductor',
            name='usuario',
            field=models.OneToOneField(verbose_name='usuario', to='main.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(verbose_name='usuario', to='main.Usuario'),
            preserve_default=True,
        ),
    ]
