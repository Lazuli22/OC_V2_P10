from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Contributor
from .serializers import ContributorDetailSerialiser, ContributorSerializer


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    detail_serializer_class = ContributorDetailSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Find the id project
        if self.kwargs["projects__pk"] is not None:
            id_project = self.kwargs["projects__pk"]
        return Contributor.objects.filter(project=id_project)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
