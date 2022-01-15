from rest_framework.serializers import ModelSerializer
from .models import Issue


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue

        fields = [
            'id', 'title', 'desc', 'tag', 'priority',
            'project_id', 'status', 'author_user_id',
            'assignee_user_id']


class IssuesListSerializer(ModelSerializer):

    class Meta:
        model = Issue

        fields = [
            'id', 'title', 'priority', 'status']
