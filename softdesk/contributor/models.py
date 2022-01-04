from django.db import models
from django.db.models.deletion import CASCADE
from core.models import Projects, Users


# Create your models here.
class Contributors(models.Model):
    """
    A class to represent a person that fills in a issue
    user_id : int
        A key to user
    project_id :
        A key to a project
    permission :
        A choice to define a kind of permission
    role :
    """
    CHOICES_ROLES = (('ad', 'admin'), ('te', 'technicien'), ('cu', 'customer'))
    CHOICES_PERM = (('R', 'read'), ('RW', 'Read_Write'), ('RWD', 'Read_Write_Delete'))
    user = models.ForeignKey(to=Users, on_delete=CASCADE)
    project = models.ForeignKey(to=Projects, on_delete=CASCADE)
    permission = models.CharField(max_length=50, choices=CHOICES_PERM)
    role = models.CharField(max_length=20,  choices=CHOICES_ROLES)

    def __str__(self) -> str:
        return self.user

