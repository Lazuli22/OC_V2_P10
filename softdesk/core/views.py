from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from issue.models import Issue
from contributor.models import Contributor
from .serializers import ProjectsListSerializer, UserSerializer, ProjectDetailSerializer
from .models import Project, User


class AdminUsersViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsListSerializer

    detail_serializer_class = ProjectDetailSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ Check if  the user is a contributor """
        if self.request.user:
            list_id = [self.request.user.id]
            list_contr = Contributor.objects.filter(user=self.request.user)
            for e in list_contr:
                list_id.append(e.project.id)
            return Project.objects.filter(pk__in=list_id)

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
