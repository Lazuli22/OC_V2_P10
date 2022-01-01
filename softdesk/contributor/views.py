from rest_framework.viewsets import ModelViewSet
from .models import Contributors
from .serializers import ContributorsSerializer
from rest_framework.response import Response


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorsSerializer()
   
    def get_queryset(self):
        proj_id = self.request.get("id")
        contrib = Contributors.objects.create(project_id=proj_id)
        serializer = ContributorsSerializer(contrib)

