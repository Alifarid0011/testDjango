from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serilizers import TopicSerializer


# Create your views here.
def product(request):
    pass


@api_view(["POST"])
def topic(request):
    if request.method == "POST":
        print(request.data)
        serilizer = TopicSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
