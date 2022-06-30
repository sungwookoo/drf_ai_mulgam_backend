from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os
import glob
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import shutil
from .models import Article

class ArticleGallery1View(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):

        return Response({"message":"성공"}, status=status.HTTP_200_OK)


class ArticleGallery2View(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get("title", "")
        file1 = request.data.get("file1")
        file2 = request.data.get("file2")
        print(file1)
        default_storage.save('tmp/content.jpg', ContentFile(file1.read()))
        default_storage.save('tmp/content2.jpg', ContentFile(file2.read()))

        order_text ='style_transfer tmp/content.jpg tmp/content2.jpg'

        os.system(order_text)
        shutil.rmtree('tmp/')

        list_of_files = glob.glob('data/*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)

        data=Article()
        data.title = title
        data.img_url = latest_file
        data.category_id=2
        data.save()
        return Response({"message": "성공"}, status=status.HTTP_200_OK)