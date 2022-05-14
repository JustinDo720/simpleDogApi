from django.shortcuts import render
from rest_framework import serializers
from .models import Dog
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = [
            'dog_name',
            'photo',
            'owner_name'
        ]
class DogAPI(APIView):

    def get(self,request):
        dog = Dog.objects.all()
        serializer = DogSerializer(dog, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)