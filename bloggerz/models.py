from django.db import models


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Register(models.Model):
    username = models.CharField(max_length=20)
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    password = models.CharField(max_length=8 )
    email_id = models.EmailField() 


class Blogcreation(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()
    image = models.URLField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

