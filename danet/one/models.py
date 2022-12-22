
from django.db import models
from datetime import datetime

# Create your models here.


# Create your models here.




class Owner(models.Model):
    first = models.CharField(max_length=64, default="Null")
    middle = models.CharField(max_length=64, default="Null")
    last = models.CharField(max_length=64, default="Null")
    position = models.CharField(max_length=64, default="Null")
    address = models.CharField(max_length=200, default="Null")
    email = models.CharField(max_length=100,  default="Null")
    email2 = models.CharField(max_length=100, default="Null")
    tel = models.CharField(max_length=64, default="Null")
    tel2 = models.CharField(max_length=64, default="Null")
    

    def __str__(self):
        return f"{self.first}{self.position}"
    
class Client(models.Model):
    first = models.CharField(max_length=64, default="Null")
    middle = models.CharField(max_length=64, default="Null")
    last = models.CharField(max_length=64, default="Null")
    tel = models.CharField(max_length=64, default="Null")
    tel2 = models.CharField(max_length=64, default="Null")
    address = models.CharField(max_length=200, default="Null")
    email = models.CharField(max_length=100, default="Null")
    email2 = models.CharField(max_length=100, default="Null")
    website = models.CharField(max_length=64, default="Null")
   
    def __str__(self):
        return f"{self.first}{self.middle}{self.last}"

    
#Content type could be project, about us, vision, ...
class ContentType(models.Model):
    content_type = models.CharField(max_length=100)
    #log = models.ManyToManyField(Log, blank=True, related_name="log")
    
    def __str__(self):
        return f"{self.content_type} "


class Content(models.Model):
    content_title = models.CharField(max_length=100)
    content_description = models.CharField(max_length = 200)
    content_t = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="contenttype")
     
    
    def __str__(self):
        return f"{self.content_title} {self.content_description} {self.content_t}"
    
class ContentImage(models.Model):
    imageTitle = models.CharField(max_length=64)
    imageDescription = models.CharField(max_length=64)
    #videofile= models.FileField(upload_to='images/', null=True, verbose_name="")
    #image_url = models.CharField(max_length=100)
    img_owner = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_image")

    def __str__(self):
        return f"{self.imageTitle}  {self.img_owner})"

class Project(models.Model):
    title = models.CharField(max_length=100, default="Null")
    description = models.CharField(max_length = 250, default="Null")
    projectClient = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_project")
    startingDate = models.DateField()
    finishingDate = models.DateField(default="Null")

    def __str__(self):
        return f"{self.title} {self.description}"    
class ProjectImage(models.Model):
    imageTile = models.CharField(max_length=64, default="Null")
    description = models.CharField(max_length=200, default="Null")
    image = models.ImageField(upload_to='images/', default="Null")
    project_image = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="proImages")

    def __str__(self):
        return f"{self.image}  {self.description}"
        
