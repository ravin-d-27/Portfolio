from django.db import models

class Skill(models.Model):
    image = models.ImageField(null=True, upload_to='images/') 
    summary = models.CharField(max_length=200)
    tech = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.summary

class Endorse(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    endorsement = models.TextField()

    def __str__(self):
        return self.name
    
class Achievements(models.Model):
    image = models.ImageField(null=True, upload_to='images/') 
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=3000, null=True)
    url = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.title
