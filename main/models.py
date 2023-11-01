from django.db import models

class Cars(models.Model):
    id = models.IntegerField(primary_key=True,default='Unknown Brand')
    brand = models.CharField(64)

    def __str__(self):
        return self.brand


class Models(models.Model):
    model_car = models.CharField(max_length=15)
    horse_power = models.IntegerField(max_length=1000)
    engine_capacity = models.FloatField(max_length=4)
    gearbox = models.CharField(max_length=6)
    year_release = models.IntegerField(max_length=5)
    type_car = models.CharField(max_length=15)
    fuel_grade = models.CharField(max_length=10)
    cars_id = models.ForeignKey(Cars,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model_car}- {self.type_car}- {self.fuel_grade} - {self.year_release} - {self.engine_capacity}- {self.gearbox} - {self.horse_power}'
