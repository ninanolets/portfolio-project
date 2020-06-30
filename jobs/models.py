from django.db import models

# Usually only one model per app is created, but you can create more 
# All models for your app are created in this file
# You create models with classes (the params allows this object to be saved on the database)

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200) # cap on the amount of text

# What fields can I have for this particular model?
# Find it on Django Documentation -> google "django model fields"


