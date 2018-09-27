from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#





class Noticia (models.Model) :
    emcabezado = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=100)
    id_user = models.ForeignKey( User , models.SET_NULL,
    blank=True,
    null=True,)
    fecha = models.DateField(auto_now=True)
    imagen = models.CharField(max_length=250, blank=True)
    imagenUrl = models.TextField(blank=True)

    def __str__(self):
        return str(self.emcabezado)


class Image(models.Model):
    img = models.ImageField(upload_to='uploads/{0}'.format("%d-%m-%y/%H_%M_%S"), default='static/f1.png')

    def __str__(self):
        return str(self.img)


class Aspirante (models.Model) :
    id_aspirante = models.AutoField(primary_key=True)
    nombre_aspirante = models.CharField(max_length=20)
    apellido_aspirante = models.CharField(max_length=20)
    contrasena_aspirante = models.CharField(max_length=10)
    dui = models.CharField(max_length=9)
    genero = models.CharField(max_length=9)
    fechas_nac = models.DateField()
    t_fijo = models.CharField(max_length=10)
    t_movil = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    titulo_pre = models.CharField(max_length=30)
    institucion = models.CharField(max_length=30)
    f_expedicion = models.DateField()
    municipio = models.CharField(max_length=50)
    lugar_trab = models.CharField(max_length=50)
    programa = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, )
    id_val = models.ForeignKey('validacion', models.SET_NULL, blank=True, null=True, )

    def __str__(self):
                return str(self.nombre_aspirante)


class Validacion (models.Model):
    id_codigo=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=250)
    vigencia= models.DateField()
    activo= models.BooleanField(default=True)
    impreso= models.BooleanField(default=False)

    def __str__(self):
                return str(self.codigo)

class Procedimiento (models.Model):
    id_procedimiento=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250)

    def __str__(self):
                return str(self.nombre)

class Pasos (models.Model):
    id_paso=models.AutoField(primary_key=True)
    id_procedimiento=models.ForeignKey(Procedimiento, models.SET_NULL, blank=True, null=True, )
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    orden=models.IntegerField()

    def __str__(self):
                return str(self.nombre)

class Docente (models.Model):
    id_docente=models.AutoField(primary_key=True)
    id_user_con = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, )
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    contrasena=models.CharField(max_length=10)
    dui = models.CharField(max_length=9)
    genero = models.CharField(max_length=9)
    fechas_nac = models.DateField()
    t_fijo = models.CharField(max_length=10)
    t_movil = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    titulo_pre = models.CharField(max_length=30)
    formacion_aca = models.CharField(max_length=30)

    def __str__(self):
                return str(self.dui)

class Cita (models.Model):
    id_cita=models.AutoField(primary_key=True)
    id_user_para = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, )
    id_user_con = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='user2')
    titulo=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=1024)
    fecha_hora_inicio=models.DateTimeField()
    fecha_hora_fin=models.DateTimeField()
    lugar=models.CharField(max_length=150,blank=True,)
    nombre_para=models.CharField(max_length=150,blank=True,)
    nombre_con=models.CharField(max_length=150,blank=True,)
    cancelado=models.BooleanField()
    dia_completo=models.BooleanField()
