from django.db import models
from django.utils import timezone
import datetime
from unidecode import unidecode
import re

# Create your models here.
class Post(models.Model):
    title    = models.CharField(max_length = 200)
    body     = models.TextField()
    pub_date = models.DateTimeField('date published')

    permalink = models.CharField(max_length = 200)

    def save(self):
      self.create_permalink()
      self.pub_date = timezone.now()

      super(Post, self).save()


    def create_permalink(self):
      if self.permalink == '':
        self.permalink = re.sub(r'\s+', '-', re.sub(r'[^\da-z]', ' ', unidecode(self.title).lower())).strip('-')


