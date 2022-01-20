from rest_framework.viewsets import ModelViewSet
from .models import Contributor
from .serializers import ContributorDetailSerialiser


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorDetailSerialiser

    def get_queryset(self):
        return Contributor.objects.all()
