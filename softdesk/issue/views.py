from rest_framework.viewsets import ModelViewSet
from .serializers import IssueDetailSerializer, CommentsListSerializer, CommentDetailSerializer
from .models import Issue, Comment


class IssuesViewset(ModelViewSet):

    serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentsViewset(ModelViewSet):

    serializer_class = CommentsListSerializer

    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
