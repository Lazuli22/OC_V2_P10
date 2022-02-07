from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Contributor
from .serializers import ContributorDetailSerialiser


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorDetailSerialiser
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Find the id project
        if self.kwargs["projects__pk"] is not None:
            id_project = self.kwargs["projects__pk"]
        return Contributor.objects.filter(project=id_project)
