from django.db import models

# Create your models here.
class RememberPlaceFB(models.Model):
    place = models.CharField(verbose_name='Address Facebook', max_length=5000, db_index=True, blank=False, unique=True)
    comment = models.CharField(verbose_name='Comment Facebook', max_length=5000, db_index=True, blank=False,unique=False)

    class Meta:
        verbose_name = 'Remember_Place Facebook-[Autofill]'
        ordering = ['id']


class RememberPlaceVk(models.Model):
    place = models.CharField(verbose_name='Address Vk', max_length=5000, db_index=True, blank=False, unique=True)
    comment = models.CharField(verbose_name='Comment Vk', max_length=5000, db_index=True, blank=False, unique=False)

    class Meta:
        verbose_name = 'Remember Vk-[Autofill]'
        ordering = ['id']


class UserLogFB(models.Model):
    user = models.CharField(verbose_name='Fullname Facebook', max_length=1000, db_index=True, unique=True, blank=False)
    releted_place = models.ManyToManyField(RememberPlaceFB, blank=True)

    class Meta:
        verbose_name = 'User Facebook-[Autofill]'
        ordering = ['id']


class UserLogVk(models.Model):
    user = models.CharField(verbose_name='Fullname Facebook', max_length=1000, db_index=True, unique=True, blank=False)
    releted_place = models.ManyToManyField(RememberPlaceVk, blank=True)

