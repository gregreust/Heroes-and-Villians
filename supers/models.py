from django.db import models
from super_types.models import SuperType

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=60)
    alter_ego = models.CharField(max_length=60)
    primary_ability = models.CharField(max_length=60)
    secondary_ability = models.CharField(max_length=60)
    catchphrase = models.CharField(max_length=150)
    super_type = models.ForeignKey(SuperType, on_delete=models.SET_NULL, null = True)

