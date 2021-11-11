from django.db import models

# Create your models here.
class RememberPlaceFB(models.Model):
    place = models.CharField(verbose_name='Address Facebook', max_length=5000, db_index=True, blank=False, unique=True)
    comment = models.CharField(verbose_name='Comment Facebook', max_length=5000, db_index=True, blank=False,unique=False)

    class Meta:
        verbose_name = 'Remember_Place Facebook-[Autofill]'
        ordering = ['id']


class RememberPlaceVk(models.Model):
