from django.db import models

# Create your models here.
class Skill(models.Model):
    #image = models.ImageField(upload_to='images/')
    image = models.ImageField(null=True, upload_to='images/') 
    summary = models.CharField(max_length=200)
    tech = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=500, null=True)

class Endorse(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    endorsement = models.TextField()

    def __str__(self):
        return self.name
