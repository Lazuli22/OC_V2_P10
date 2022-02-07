from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import IssueDetailSerializer, CommentsListSerializer, CommentDetailSerializer
from .models import Issue, Comment


class IssuesViewset(ModelViewSet):

    serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.kwargs["projects__pk"] is not None:
            id_project = self.kwargs["projects__pk"]
        return Issue.objects.filter(project=id_project)


class CommentsViewset(ModelViewSet):

    serializer_class = CommentsListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        if self.kwargs["issues__pk"] is not None:
            id_issue = self.kwargs["issues__pk"]
        return Comment.objects.filter(issue=id_issue)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
