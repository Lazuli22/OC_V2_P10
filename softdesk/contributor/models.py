from django.db import models
from django.db.models.deletion import CASCADE

from softdesk.core.models import Projects, Users


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
    user_id = models.ForeignKey(to=Users, on_delete=CASCADE)
    project_id = models.ForeignKey(to=Projects, on_delete=CASCADE)
    permission = models.ChoiceField()
    role = models.CharField(max_length=20)
