from django.db import models

class Empresa(models.Model):
    
    def image_path(self,filename):
        ruta = "setting/%s/%s" % (self.setting_name,str(filename))
        return ruta
    
    empresa = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)    
    my_foto = models.ImageField(upload_to=image_path)
    background = models.ImageField(upload_to=image_path)    
    status = models.BooleanField(default=False)


class Cliente(models.Model):
    
    def image_path(self,filename):
        ruta = "setting/%s/%s" % (self.setting_name,str(filename))
        return ruta
    
    cliente = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)    
    foto = models.ImageField(upload_to=image_path)
    background = models.ImageField(upload_to=image_path)    
    status = models.BooleanField(default=False)