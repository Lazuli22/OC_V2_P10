from django import contrib
from django.contrib.auth.models import Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Contributors
from .serializers import ContributorsSerializer


class ContributorsList(APIView):

    def get(self, request, id):
        cont = Contributors.objects.filter(project_id=id)
        serializer = ContributorsSerializer(cont, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = ContributorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorDetail(APIView):

    def get_object(self, pk):
        try:
            return Contributors.objects.get(pk=pk)
        except Contributors.DoesNotExist:
            raise Http404

    def get(self, request, id, pk):
        contr = Contributors.objects.get(id=pk)
        serializer = ContributorsSerializer(contr)
        return Response(serializer.data)

    def put(self, request, id, pk, format=None):
        the_contr = self.get_object(pk)
        serializer = ContributorsSerializer(the_contr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, format=None):
        cont = self.get_object(pk)
        cont.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
