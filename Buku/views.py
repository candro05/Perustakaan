from django.shortcuts import render
from rest_framework import viewsets
from .models import Buku
from .serializers import BukuSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

class BukuView(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def Buku_list(request):
    if request.method == 'GET':
        buku = Buku.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            buku = buku.filter(title__icontains=title)

        buku_serializer = BukuSerializer(buku, many=True)
        return JsonResponse(buku_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        buku_serializer = BukuSerializer(data=tutorial_data)
        if buku_serializer.is_valid():
            buku_serializer.save()
            return JsonResponse(buku_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(buku_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Buku.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def Buku_detail(request, pk):
        try:
            buku = Buku.objects.get(pk=pk)
        except Buku.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = BukuSerializer(buku)
            return JsonResponse(tutorial_serializer.data)

        elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            buku_serializer = BukuSerializer(buku, data=tutorial_data)
            if buku_serializer.is_valid():
                buku_serializer.save()
                return JsonResponse(buku_serializer.data)
            return JsonResponse(buku_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            buku.delete()
            return JsonResponse({'message': 'Buku was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def buku_list_published(request):
        buku = Buku.objects.filter(published=True)

        if request.method == 'GET':
            buku_serializer = BukuSerializer(buku, many=True)
            return JsonResponse(buku_serializer.data, safe=False)