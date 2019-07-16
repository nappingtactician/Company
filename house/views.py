from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import asset,work,worker,allocatework
from .serializers import assetSerializer,workSerializer,workerSerializer,allocateworkSerializer



class AssetList(APIView):

    def get(self,request, format=None):
        Asset = asset.objects.all()
        serializer_asset = assetSerializer(Asset, many=True)
        return Response(serializer_asset.data)

    def post(self,request, format=None):
        serializer_asset = assetSerializer(data=request.data)
        if serializer_asset.is_valid():
            serializer_asset.save()
            return Response(serializer_asset.data,status=status.HTTP_201_CREATED)
        return Response(serializer_asset.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkList(APIView):
    def get(self,request,format=None):
        Work = work.objects.all()
        serializer_work = workSerializer(Work, many=True)
        return Response(serializer_work.data)

    def post(self,request, format=None):
        serializer_work = workSerializer(data=request.data)
        if serializer_work.is_valid():
            serializer_work.save()
            return Response(serializer_work.data,status=status.HTTP_201_CREATED)
        return Response(serializer_work.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerList(APIView):
    def get(self,request,format=None):
        Worker = worker.objects.all()
        serializer_worker = workerSerializer(Worker, many=True)
        return Response(serializer_worker.data)


    def post(self,request, format=None):
        serializer_worker = workerSerializer(data=request.data)
        if serializer_worker.is_valid():
            serializer_worker.save()
            return Response(serializer_worker.data,status=status.HTTP_201_CREATED)
        return Response(serializer_worker.errors, status=status.HTTP_400_BAD_REQUEST)

class AllocateworkList(APIView):
    def get(self,request,format=None):
        Allocatework = allocatework.objects.all()
        serializer_allocatework = allocateworkSerializer(Allocatework, many=true)
        return Response(serializer_allocatework.data)

    def post(self,request, format=None):
        serializer_allocatework = allocateworkSerializer(data=request.data)
        if serializer_allocatework.is_valid():
            serializer_allocatework.save()
            return Response(serializer_allocatework.data,status=status.HTTP_201_CREATED)
        return Response(serializer_allocatework.errors,status=status.HTTP_400_BAD_REQUEST)









