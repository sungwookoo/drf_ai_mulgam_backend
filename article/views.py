from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os


class ArticleView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        a = 'style_transfer data/12.jpg data/content.jpg'
        os.system(a)
        return Response({"message":"성공"}, status=status.HTTP_200_OK)