from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User


POST_CHOICES = ('public', 'private', 'friends')



class Post(models.Model):

    POST_CHOICES =( ('public','public'),
                ('private','private'),
                ('friends', 'friends'),
                  )

    privacy = models.CharField(max_length=20, choices=POST_CHOICES,default='public',)
    post = models.TextField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    date =models.DateTimeField(auto_now=True)
    msg =models.CharField(max_length=20,default='')



    def __str__(self):
        """A string representation of the model."""
        return self.post



class relation(models.Model):
    connected = models.ForeignKey(User, on_delete=models.CASCADE)
    doc = models.DateTimeField(auto_now=True)
    main=models.CharField(max_length=1000000)
    flag = models.BooleanField(default=False)



    def __str__(self):
        """A string representation of the model."""
        return self.connected.username


class connect(models.Model):

    user1 =models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return  self.date





















