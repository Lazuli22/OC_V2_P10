from rest_framework.serializers import ModelSerializer
from core.serializers import ProjectDetailSerializer
from .models import Contributor
from core.serializers import UserSerializer


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'permission', 'role']


class ContributorDetailSerialiser(ModelSerializer):

    user = UserSerializer()
    project = ProjectDetailSerializer()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'permission', 'role']

