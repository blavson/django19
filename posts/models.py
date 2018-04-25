from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib.auth.models import User


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title=models.CharField(max_length=256)
    slug = models.SlugField(unique=True, default=None)
    image=models.ImageField(upload_to=upload_location,null=True,blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering=["-timestamp", "-updated"]

@receiver(pre_save,sender=Post)
def my_callback(sender, instance, *args, **kwargs):
    instance.slug =slugify(unidecode(instance.title))
