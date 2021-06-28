from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, default="old dojo")

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)