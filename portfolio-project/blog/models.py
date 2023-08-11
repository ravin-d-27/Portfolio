from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=15000)
    image = models.ImageField(upload_to='images/')
    class Meta:
        ordering = ['-pub_date']