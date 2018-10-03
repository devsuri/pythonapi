from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import snappide
from .serializers import snappideSerializer

class snapplist(APIView):

    def get(self, request):
        snapplist1=snappide.objects.all()
        serializer=snappideSerializer(snapplist1, many=True)
        return Response(serializer.data)

    def __pos__(self):
        pass
# Create your views here.