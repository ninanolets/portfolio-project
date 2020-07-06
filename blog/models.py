from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')





# Create a blog models
    # title
    # pub_date
    # body
    # image
# Add the blog app to the settings
# Create a migration
# Migrate
# Add to the admin