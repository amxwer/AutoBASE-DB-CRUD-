from django.db import models



class Cars(models.Model):

    brand = models.CharField(max_length=20)
    model_car = models.CharField(max_length=20)
    type_car = models.CharField(max_length=12,default='sedan')
    horse_power  = models.IntegerField(max_length=4)
    engine_capacity = models.FloatField(max_length=10.0)
    gearbox = models.CharField(max_length=20)
    fuel_grade = models.CharField(max_length=9)
    year_of_release = models.IntegerField(max_length=5)


    def __str__(self):
        return self.brand

    class Meta:
        verbose_name ='Бренд'
        verbose_name_plural = 'Бренды'
# Create your models here.
