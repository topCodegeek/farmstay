from django.db import models

class Location(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField(max_length=200)
     thumbnail = models.URLField(null=False)

     def __str__(self):
          return self.name