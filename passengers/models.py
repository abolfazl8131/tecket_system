from django.db import models


# Create your models here.


class Passenger(models.Model):
    
    class GenderType(models.TextChoices):
        Male = 'M','Male'
        Femail = 'F','Femail'

    ID = models.BigIntegerField(unique=True , primary_key=True,null=False)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1 ,choices=GenderType.choices)
    is_deleted = models.BooleanField(default=False)

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class SimpleUser(Passenger):
    phone_number = models.BigIntegerField()
