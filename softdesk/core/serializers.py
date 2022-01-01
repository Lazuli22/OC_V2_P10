from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Projects, Users
from issue.serializers import IssuesSerializer
from django.contrib.auth.hashers import make_password


class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class AllProjectsSerializer(ModelSerializer):

    TYPES = ["projet", "produit", "application"]
    issues = serializers.SerializerMethodField()
    author_user_id = UsersSerializer()

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type', "issues", "author_user_id"]

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssuesSerializer(queryset, many=True)
        return serializer.data

    def validate_title(self, value: str) -> str:
        """
         Verify project exists by its name

        """
        if Projects.objects.filter(title=value).exists():
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
