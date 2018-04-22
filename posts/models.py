from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=256)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
#    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
