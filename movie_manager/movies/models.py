from django.db import models


# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)    
    certified_by=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.certified_by



class Director(models.Model):
    name=models.CharField(max_length=300)    
    def __str__(self):
        return self.name

   
class Actor(models.Model):
    name=models.CharField(max_length=300) 

    def __str__(self):
        return self.name
   
   

class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    Censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,null=True,related_name='movies')
    directed_by=models.ForeignKey(Director,null=True,on_delete=models.CASCADE,related_name='directed_movies')
    actors=models.ManyToManyField(Actor,related_name='acted_movies')

    def __str__(self):
        return self.title

