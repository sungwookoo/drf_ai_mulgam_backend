from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os


class ArticleGallery1View(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):

        return Response({"message":"성공"}, status=status.HTTP_200_OK)