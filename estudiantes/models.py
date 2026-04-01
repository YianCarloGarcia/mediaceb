from django.db import models
from django.utils import timezone

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    
    JORNADA = [
        ('JM', 'Jornada Mañana'),
        ('JT', 'Jornada Tarde'),
    ]
    TIPOS_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('PP', 'Permito de Protección'),
        ('OT', 'Otro'),
    ]
    LINEA_MEDIA = [
        ('AA', 'Asistencia Administrativa'),
        ('ISERC', 'Instalaciones eléctricas'),
        ('TPS', 'Programación de Software'),
        ('COM', 'Comunicación y medios audiovisuales'),
        ('ROB', 'Robótica'),
        ('BIO', 'Biotecnología'),
        ('DIS', 'Diseño multimedia'),
        ('OT', 'Otro'),
    ]
    jornada = models.CharField(max_length=50, choices=JORNADA, verbose_name="Jornada", default='JM')
    tipo = models.CharField(max_length=2,choices=TIPOS_DOCUMENTO, verbose_name="Tipo", default='CC')
    documento = models.CharField(max_length=20, verbose_name="Documento")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    curso = models.CharField(max_length=100, verbose_name="Curso")
    linea = models.CharField(max_length=50,choices=LINEA_MEDIA, verbose_name="Línea", default='OT')
    celular = models.CharField(max_length=20, verbose_name="Celular", null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name="Email", null=True, blank=True)
    acudiente = models.CharField(max_length=100, verbose_name="Acudiente", null=True, blank=True)
    parentesco = models.CharField(max_length=50, verbose_name="Parentesco Acudiente", null=True, blank=True)
    tel_acudiente = models.CharField(max_length=20, verbose_name="Teléfono Acudiente", null=True, blank=True)
    tel2_acudiente = models.CharField(max_length=20, verbose_name="Teléfono 2 Acudiente", null=True, blank=True)
    direccion = models.CharField(max_length=200, verbose_name="Dirección", null=True, blank=True)
    ocupacion_acudiente = models.CharField(max_length=100, verbose_name="Ocupación Acudiente", null=True, blank=True)
    eps = models.CharField(max_length=100, verbose_name="EPS", null=True, blank=True)
    observaciones = models.TextField(verbose_name="Observaciones", null=True, blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    
    # mostrrar datos en el admin
    def __str__(self):
        fila = "Apellido: " + self.apellidos + ", Nombre: " + self.nombres + ", Jornada: " + self.jornada + ", línea: " + self.linea + ", Curso: " + self.curso
        return fila
    #Borrr imagen al eliminar registro
#    def delete(self, using = None, keep_parents = False):
#        self.foto.storage.delete(self.foto.name)
#        super().delete()

    def delete(self, using=None, keep_parents=False):
        if self.foto:
            self.foto.storage.delete(self.foto.name)
        super().delete()

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    TIPO_REGISTRO = [
        ('ALM', 'Almuerzo'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_REGISTRO, default='ALM')

    def __str__(self):
        return f"{self.estudiante} - {self.fecha} - {self.hora}"


    