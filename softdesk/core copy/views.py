from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from contributor import serializers
from issue.models import Issue
from contributor.serializers import ContributorSerializer
from .serializers import ProjectsListSerializer, UserSerializer, ProjectDetailSerializer
from .models import Project, User
from contributor.models import Contributor


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

    @csrf_exempt
    @action(detail=True, methods=['GET', 'POST'], url_path='contributors')
    def contributors(self, request, *args, **kwargs):
        """ Get or create Contributors """
        instance = self.get_object()
        contr = None
        if request.method == 'GET':
            contr = Contributor.objects.filter(project__pk=instance.id)
            serializer = serializers.ContributorSerializer(contr, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'POST':
            print(request.data)
            # la création d'un contributeur devrait s'accompagner de la saisie
            # du projet.
            serializer = ContributorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        project = self.get_object()
        issues_del = Issue.objects.filter(project_id=project.id)
        issues_del.delete()
        project.delete()
        return super().destroy(request, pk=None)
