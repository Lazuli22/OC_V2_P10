
from rest_framework.viewsets import ModelViewSet
from .serializers import IssuesSerializer
from .models import Issues


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer()

    def get_queryset(self):
        return Issues.objects.all()
