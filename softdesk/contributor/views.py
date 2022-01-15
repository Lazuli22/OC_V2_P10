from django import contrib
from django.contrib.auth.models import Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Contributor
from .serializers import ContributorDetailSerialiser


# class ContributorsList(APIView):

#     def get(self, request, id):
#         cont = Contributors.objects.filter(project_id=id)
#         serializer = ContributorsSerializer(cont, many=True)
#         return Response(serializer.data)

#     def post(self, request, id):
#         serializer = ContributorsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorDetailSerialiser

    def get_queryset(self):
        return Contributor.objects.all()


class ContributorDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Contributor.objects.get(pk=pk)
        except Contributor.DoesNotExist:
            raise Http404

    def get(self, request, id, pk):
        contr = Contributor.objects.get(id=pk)
        serializer = ContributorDetailSerialiser(contr)
        return Response(serializer.data)

    def put(self, request, id, pk, format=None):
        the_contr = self.get_object(pk)
        serializer = ContributorDetailSerialiser(the_contr, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, format=None):
        cont = self.get_object(pk)
        cont.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
