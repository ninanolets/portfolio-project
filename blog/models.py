from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default='')

    def __str__(self):
        return self.title

    def body_summary(self):
        return self.body[:200]

    def custome_pub_date(self):
        return self.pub_date.strftime('%b %e %Y') # strftime (customises date format)





# Create a blog models
    # title
    # pub_date
    # body
    # image
# Add the blog app to the settings
# Create a migration
# Migrate
# Add to the admin