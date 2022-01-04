from rest_framework.serializers import ModelSerializer
from .models import Contributors
from core.serializers import UsersSerializer


class ContributorsSerializer(ModelSerializer):

    user = UsersSerializer()

    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project', 'permission', 'role']
