from django.db import models

# Create your models here.
class Location(models.Model):
    country=models.CharField(max_length=50)
    def __str__(self):
         return self.country
    # def save_location(self):
    #     self.save()
    # def delete_location(self):
    #     self.delete()
    # @classmethod 
    # def update (cls,id,name):
    #     location = Location.objects.filter(id=id)
    #     location.update(country=name)
    #     return location
