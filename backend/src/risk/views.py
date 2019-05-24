from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import RiskType
from .serializers import RiskTypeSerializer

# Create your views here.


@api_view(['GET'])
def rest_framework_prac(request):
    return Response({"msg": "please work."})


class RiskTypeList(APIView):
    """
        List all Risk types in the system or creates a new one.
    """

    def get(self, request, format=None):
        risktypes = RiskType.objects.all()
        serializer = RiskTypeSerializer(risktypes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # print(request.data)
        serializer = RiskTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(APIView):
    """
        Retrieve, update or delete risktypes in the system.
    """

    def get_object(self, pk):
        try:
            return RiskType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        riskType = self.get_object(pk)
        serializer = RiskTypeSerializer(riskType)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        riskType = self.get_object(pk)
        serializer = RiskTypeSerializer(riskType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        riskType = self.get_object(pk)
        riskType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
