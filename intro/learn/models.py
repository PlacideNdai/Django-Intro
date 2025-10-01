from django.db import models

# Create your models here.
class Guitar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    number_of_strings = models.IntegerField()
    electric_guitar = models.BooleanField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Owner(models.Model):
    number_of_guitars = models.IntegerField()
    owner_id = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner_id.__str__()