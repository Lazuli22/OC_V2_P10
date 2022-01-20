from rest_framework.viewsets import ModelViewSet
from issue.models import Issue
from .serializers import ProjectsListSerializer, UserSerializer, ProjectDetailSerializer
from .models import Project, User


class AdminUsersViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsListSerializer

    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def destroy(self, request, pk=None):
        project = self.get_object()
        issues_del = Issue.objects.filter(project_id=project.id)
        issues_del.delete()
        project.delete()
        return super().destroy(request, pk=None)
