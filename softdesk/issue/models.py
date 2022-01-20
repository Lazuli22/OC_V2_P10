from django.db import models
from django.db.models.deletion import CASCADE
from core.models import Project, User


class Issue(models.Model):
    """
    A class to represent a issue
    """
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project = models.ForeignKey(to=Project, on_delete=CASCADE, related_name="issues")
    status = models.CharField(max_length=50)
    author_user = models.ForeignKey(to=User, related_name="author_issue", on_delete=CASCADE, blank=True)
    assignee_user = models.ForeignKey(to=User, related_name="assignee", on_delete=CASCADE, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """
    A class to represent a comment in a project or for a issue
    """
    description = models.CharField(max_length=250)
    author_user = models.ForeignKey(to=User, related_name="author_comment", on_delete=CASCADE, blank=True)
    issue = models.ForeignKey(to=Issue, related_name="issue", on_delete=CASCADE, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
