from django.db import models

# Create your models here.

class HoodiesImages(models.Model):
    product_name = models.CharField(max_length=255)
    download_link = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)

    class Meta:
        db_table = 'dzhempery_i_svitery'
