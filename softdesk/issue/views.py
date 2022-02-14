
from ast import Delete
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from core.models import Project
from .serializers import IssueDetailSerializer, IssuesListSerializer, CommentsListSerializer, CommentDetailSerializer
from .models import Issue, Comment
from contributor.models import Contributor


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesListSerializer
    permission_classes = [IsAuthenticated]
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        if self.request.user:
            connected_user = self.request.user.id
        if self.kwargs["projects__pk"] is not None:
            id_project = self.kwargs["projects__pk"]
            the_project = Project.objects.get(id=id_project)
            if connected_user == the_project.author_user.id:
                return Issue.objects.filter(project=id_project)
            else:
                list_contr = Contributor.objects.filter(project=id_project)
                for e in list_contr:
                    if connected_user == e.user.id:
                        return Issue.objects.filter(project=id_project)
                raise ValidationError(detail="You are not allowed to access to issues of this project!")

    def update(self, request, *args, **kwargs):
        if self.request.user:
            connected_user = self.request.user.id
            a_issue = self.get_object()
            if connected_user == a_issue.author_user.id:
                serializer = self.get_serializer(a_issue, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response({'status': 'updated issue'})
            else:
                raise ValidationError(detail="Only the author of issue can update a !")

    def destroy(self, request, *args, **kwargs):
        if self.request.user:
            connected_user = self.request.user.id
            a_issue = self.get_object()
            if connected_user == a_issue.author_user.id:
                comments_del = Comment.objects.filter(id=a_issue.id)
                comments_del.delete()
                a_issue.delete()
                super().destroy(request, *args, **kwargs)
            else:
                raise ValidationError(detail="Seul l'auteur du problème peut supprimer le problème!")

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return self.detail_serializer_class
        return super().get_serializer_class()
        

class CommentsViewset(ModelViewSet):

    serializer_class = CommentsListSerializer
    permission_classes = [IsAuthenticated]

    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        if self.request.user:
            connected_user = self.request.user.id
        if self.kwargs["issues__pk"] is not None:
            id_issue = self.kwargs["issues__pk"] 
        if self.kwargs["projects__pk"] is not None:
            id_project = self.kwargs["projects__pk"]
            the_project = Project.objects.get(id=id_project)
            if connected_user == the_project.author_user.id:
                return Comment.objects.filter(issue=id_issue)
            else:
                list_contr = Contributor.objects.filter(project=id_project)
                for e in list_contr:
                    if connected_user == e.user.id:
                        return Comment.objects.filter(issue=id_issue)
                raise ValidationError(detail="You are not allowed to access to commments of this project!")

    def update(self, request, *args, **kwargs):
        if self.request.user:
            connected_user = self.request.user.id
            a_comment = self.get_object()
            if connected_user == a_comment.author_user.id:
                serializer = self.get_serializer(a_comment, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response({'status': 'updated comment'})
            else:
                raise ValidationError(detail="Only the author of the comment can udapte it !")

    def destroy(self, request, *args, **kwargs):
        if self.request.user:
            connected_user = self.request.user.id
            a_comment = self.get_object()
            if connected_user == a_comment.author_user.id:
                a_comment.delete()
                super().destroy(request, *args, **kwargs)
            else:
                raise ValidationError(detail="Only the author of the comment can delete it!")

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return self.detail_serializer_class
        return super().get_serializer_class()
