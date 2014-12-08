from django.db import models

# Create your models here.
class location(models.Model):
    lat = models.DecimalField(decimal_places=7,max_digits=10)
    lng = models.DecimalField(decimal_places=7,max_digits=10)
    height = models.DecimalField(decimal_places=7,max_digits=10)
    
    def __str__(self):
        return ("id: %s lat: %s lng: %s height: %s"%(self.id,self.lat,self.lng,self.height))