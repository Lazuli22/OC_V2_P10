from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Project, User
from issue.serializers import IssuesListSerializer
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class ProjectsListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']


class ProjectDetailSerializer(ModelSerializer):
   
    TYPES = ["projet", "produit", "application"]
    issues = serializers.SerializerMethodField()
    author_user = UserSerializer()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description',
            'type', 'author_user', 'issues'
        ]

    def get_issues(self, instance):
        queryset = instance.issues.filter(project=instance.id)
        serializer = IssuesListSerializer(queryset, many=True)
        return serializer.data

    def validate_title(self, value: str) -> str:
        """
         Verify project exists by its name

        """
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError('Projet déja existant')
        return value

    def validate_type(self, value):
        """ 
        Verify the project's type
        """
        if value not in self.TYPES:
            raise serializers.ValidationError(
                'Le type doit être choisi parmi 3 valeurs : application, produit ou projet')
        return value
