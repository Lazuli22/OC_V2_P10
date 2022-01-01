from rest_framework.serializers import ModelSerializer
from .models import Issues


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issues

        fields = [
            'title', 'desc', 'tag', 'priority',
            'project_id', 'status', 'author_user_id',
            'assignee_user_id']
