from rest_framework.serializers import ModelSerializer
from .models import Contributors
from core.serializers import AllProjectsSerializer


class ContributorsSerializer(ModelSerializer):

    projet_id = AllProjectsSerializer(many=True)

    class Meta:
        model = Contributors
        fields = ['user_id', 'project_id', 'permission', 'role']

    