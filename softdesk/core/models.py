from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# User Model
class User(AbstractUser):
    """
    A class to represent a user
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name


# Project Model
class Project(models.Model):
    """
    A class to represent a project of issues
        title : str
            a name of the project
        description : str
            a description of the project
        type : str
            a type of the project
    """
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=20)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
