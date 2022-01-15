
# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import IssueDetailSerializer, IssuesListSerializer
from .models import Issue


# class IssuesViewset(ModelViewSet):

#     serializer_class = IssuesSerializer()

#     def get_queryset(self):
#         return Issues.objects.all()


class IssuesList(APIView):

    def get(self, request, id):
        list_issues = Issue.objects.filter(project=id)
        serializer = IssuesListSerializer(list_issues, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = IssueDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueDetail(APIView):

    def get(self, request, id, pk):
        the_issue = Issue.objects.get(id=pk)
        serializer = IssueDetailSerializer(the_issue)
        return Response(serializer.data)

    def put(self, request, id, pk, format=None):
        the_issue = Issue.objects.get(id=pk)
        serializer = IssueDetailSerializer(the_issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, format=None):
        cont = self.get_object(pk)
        cont.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
