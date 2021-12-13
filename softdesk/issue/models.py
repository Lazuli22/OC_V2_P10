from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.query import Prefetch

from softdesk.core.models import Projects, Users


class Issues(models.Model):
    """
    A class to represente a issue
    """
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    tag = models.CharField(max_length=50)
    priority = models.CharField()
    project_id = models.ForeignKey(to=Projects, on_delete=CASCADE)
    status = models.CharField()
    author_user_id = models.ForeignKey(to=Users, on_delete=CASCADE)
    assignee_user_id = models.ForeignKey(to=Users, on_delete=CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    """
    A class to represente a comment in a project or for a issue
    """
    description = models.CharField(max_length=250)
    author_user_id = models.ForeignKey(to=Users, on_delete=CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
