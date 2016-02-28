#coding:utf-8
from __future__ import unicode_literals
# from  PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import Slugify, CYRILLIC
slugify_ru = Slugify(pretranslate=CYRILLIC)
# @receiver(post_save, sender=User)
# def handle_user_save(sender, instance, created, **kwargs):
#   if created:
#     Client.objects.create(user=instance)

class Client(models.Model):
    # user = models.OneToOneField(User)
    client_first_name = models.CharField(max_length=255, verbose_name='Ім’я', blank=True)
    client_last_name = models.CharField(max_length=255, verbose_name='Прізвище', blank=True)
    client_image = models.ImageField(upload_to='client/photos/', blank=True)
    client_description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)


    def save(self, *args):
        print slugify_ru(self.client_first_name)
        self.slug = slugify_ru('%s-%s'%(self.client_first_name, self.client_last_name))
        super(Client, self).save(*args)

    def __unicode__(self):
        return '%s - %s'%(self.client_first_name, self.client_last_name)

    def get_full_name(self):
        return "%s %s"%(self.client_first_name, self.client_last_name)



class Documents(models.Model):
    documents_link = models.ForeignKey(Client, related_name='docs')
    documents_file = models.ImageField(upload_to='client/documents/')
