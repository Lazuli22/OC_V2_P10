from rest_framework.viewsets import ModelViewSet
from issue.models import Issues
from issue.serializers import IssuesSerializer
from .serializers import AllProjectsSerializer, UsersSerializer
from .models import Projects, Users


class AdminUsersViewset(ModelViewSet):

    serializer_class = UsersSerializer
   
    def get_queryset(self):
        return Users.objects.all()


class ProjectsViewset(ModelViewSet):

    serializer_class = AllProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all()


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issues.objects.all()
