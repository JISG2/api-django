from django.shortcuts import render

# Create your views here.
from apps.campeon.models import CampeonM
from apps.campeon.serializers import CampeonSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser

# Create your views here.
class CampeonList(APIView):
    queryset = CampeonM.objects.all()
    def get(self,request,format=None):
       queryset = CampeonM.objects.all()
       serializer = CampeonSerializer(queryset,many=True)
       return Response(serializer.data)

    def post(self, request, format = None):
       serializer = CampeonSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           datas = serializer.data
           response = datas
           return Response(response,status=status.HTTP_201_CREATED)  
       response = serializer.errors
       return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        data = request.data
        campeon = CampeonM.objects.get(id=pk)
        serializer = CampeonSerializer(campeon, data=data)
        if serializer.is_valid():
            campeonUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        # Get object with this pk
        campeon = get_object_or_404(CampeonM.objects.all(), pk=pk)
        campeon.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204) 