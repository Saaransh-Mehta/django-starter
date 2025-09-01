from django.db import models

# Create your models here.
class chaiVariety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images/')
