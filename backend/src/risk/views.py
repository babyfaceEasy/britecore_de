from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings

from .models import RiskType
from .serializers import RiskTypeSerializer

# Create your views here.


@api_view(['GET'])
def rest_framework_prac(request):
    return Response({"msg": "please work."})


class RiskTypeList(generics.GenericAPIView):
    """
        List all Risk types in the system or creates a new one.
    """

    def get(self, request, format=None):
        '''
        risktypes = RiskType.objects.all()
        serializer = RiskTypeSerializer(risktypes, many=True)
        return Response({"msg": "Available risk types", "data": serializer.data})
        '''

        queryset = RiskType.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = RiskTypeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RiskTypeSerializer(queryset, many=True)
        return Response({"msg": "Available risk types", "data": serializer.data})

    def post(self, request, format=None):
        # print(request.data)
        serializer = RiskTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
class RiskTypeList(APIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
    # cool trick right? :)
    pagination_class = settings.REST_FRAMEWORK.get('DEFAULT_PAGINATION_CLASS')

    # We need to override get method to achieve pagination
    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    # Now add the pagination handlers taken from
    #  django-rest-framework/rest_framework/generics.py

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

'''
'''
class RiskTypeList(generics.ListCreateAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
    paginate_by = 2
'''


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
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

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
