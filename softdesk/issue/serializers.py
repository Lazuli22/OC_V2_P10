from rest_framework.serializers import ModelSerializer
from .models import Comment, Issue


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue

        fields = [
            'id', 'title', 'desc', 'tag', 'priority',
            'project', 'status', 'author_user',
            'assignee_user']


class IssuesListSerializer(ModelSerializer):

    class Meta:
        model = Issue

        fields = [
            'id', 'title', 'priority', 'status', 'project', 'assignee_user', 'author_user']


class CommentsListSerializer(ModelSerializer):

    class Meta:
        model = Comment

        fields = [
            'id', 'description', 'issue', 'author_user']


class CommentDetailSerializer(ModelSerializer):

    class Meta:
        model = Comment

        fields = [
            'id', 'description', 'author_user', 'issue', 'created_time']
