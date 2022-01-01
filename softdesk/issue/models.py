from django.db import models
from django.db.models.deletion import CASCADE
from core.models import Projects, Users


class Issues(models.Model):
    """
    A class to represente a issue
    """
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project_id = models.ForeignKey(to=Projects, on_delete=CASCADE, related_name="issues")
    status = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(to=Users, related_name="author", on_delete=CASCADE)
    assignee_user_id = models.ForeignKey(to=Users, related_name="assignee", on_delete=CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """
    A class to represente a comment in a project or for a issue
    """
    description = models.CharField(max_length=250)
    author_user_id = models.ForeignKey(to=Users, on_delete=CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
