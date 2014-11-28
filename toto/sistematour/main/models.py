from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class MenejadorGenerico(models.Manager):

    def traer_todos_activos(self):
        return self.filter(es_activo=True).order_by('-fecha_modificacion')

    def traer_o_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
        except self.model.MultipleObjectsReturned:
            return None


class PlantillaModel(models.Model):
    # ------ datos para todas las tablas
    es_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    objects = MenejadorGenerico()
    class Meta:
        abstract = True


class Direccion(PlantillaModel):
    direccion = models.CharField(max_length=60, verbose_name=_("direccion"), null=True,blank=True,default="")
    ciudad = models.CharField(max_length=60, verbose_name=_("ciudad"), null=True,blank=True,default="")
    departamento = models.CharField(max_length=60, verbose_name=_("departamento"), null=True,blank=True,default="")    
    barrio = models.CharField(max_length=60, verbose_name=_("barrio"), null=True,blank=True,default="") 
    pais = models.CharField(max_length=60, verbose_name=_("pais"), null=True,blank=True,default="")     
    select = models.BooleanField(default=False)

    def __unicode__(self):
        return self.direccion



class Usuario(PlantillaModel):
    """Extended profile to Django User model"""
    usuario = models.OneToOneField(User, verbose_name=_("usuario") ,null=False)
    celular = models.CharField(max_length=50, verbose_name=_("celular"), null=True,blank=True) 
    cedula = models.CharField(max_length=20,verbose_name=_("cedula"), null=True,blank=True)
    foto = models.ImageField(upload_to='perfil', verbose_name='foto de perfil',blank=True)
    direccion = models.ForeignKey(Direccion,verbose_name=_("Direccion") ,null=False)
    
    def __unicode__(self):
        return self.usuario.username

class Cliente(PlantillaModel):
    usuario = models.OneToOneField(Usuario,verbose_name=_("usuario") ,null=False)
    numeroCuenta = models.IntegerField(max_length=40)
    banco = models.CharField(max_length=20)

    def __unicode__(self):
        return self.usuario.usuario.username



class Conductor(PlantillaModel):
    usuario = models.OneToOneField(Usuario,verbose_name=_("usuario") ,null=False)
    tipoLicencia = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.usuario.usuario.username

class Destino(PlantillaModel):
    lugar = models.CharField(max_length=50)
    picoPlaca = models.BooleanField(default=False)
    requerimiento = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='perfil', verbose_name='foto de perfil',blank=True)  
    def __unicode__(self):
		return self.lugar


class Vehiculo(PlantillaModel):
    codigo  = models.CharField(max_length=50,verbose_name=_("codigo"))
    placa = models.CharField(max_length=10,verbose_name=_("placa"))
    tipo = models.CharField(max_length=20,verbose_name=_("tipo"))
    cupo = models.IntegerField(max_length=3,verbose_name=_("cupo"))
    foto = models.ImageField(upload_to='perfil', verbose_name='foto de perfil',blank=True)
    def __unicode__(self):
		return self.tipo


class precio(PlantillaModel):
    vehiculo = models.ForeignKey(Vehiculo,verbose_name=_("usuario") ,null=False)
    destino = models.ForeignKey(Destino,verbose_name=_("usuario") ,null=False)
    precio = models.IntegerField()
    
    def __unicode__(self):
        return str(self.vehiculo)+" para "+str(self.destino)+" vale :"+str(self.precio)

class Orden(PlantillaModel):
	fechaSalida = models.DateTimeField()
	conductor = models.CharField(max_length=20)
	vehiculoPlaca = models.IntegerField(max_length=10)
	destino = models.CharField(max_length=40)
	cliente = models.ForeignKey(Cliente,verbose_name=_("usuario") ,null=False)
	
	def __unicode__(self):
		return self.id
	

class Pago(PlantillaModel):
	cliente = models.ForeignKey(Cliente,verbose_name=_("usuario") ,null=False)
	monto = models.IntegerField(max_length=20)
	orden = models.ForeignKey(Orden,verbose_name=_("orden") ,null=False)
	saldo = models.IntegerField(max_length=20)
	tipoPago = models.CharField(max_length=10)

	def __unicode__(self):
		return self.cliente