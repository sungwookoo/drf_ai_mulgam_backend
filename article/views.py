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
from .models import Comment as CommentModel
# from gallery1.main import mix

from article.serializers import CommentSerializer



class ArticleGallery1View(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get("title", "")
        file = request.data.get("file")
        num = request.data.get("num", "")
        default_storage.save('gallery1/input/input_img.jpg', ContentFile(file.read()))

        model = ['gallery1/models/composition_vii.t7',
                 'gallery1/models/la_muse.t7',
                 'gallery1/models/starry_night.t7',
                 'gallery1/models/the_wave.t7',
                 'gallery1/models/candy.t7',
                 'gallery1/models/feathers.t7',
                 'gallery1/models/mosaic.t7',
                 'gallery1/models/the_scream.t7',
                 'gallery1/models/udnie.t7'
                 ]

        model_num = model[int(num)]
        mix(model_num)

        shutil.rmtree('gallery1/input/')

        list_of_files = glob.glob('gallery1/output/*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)

        data = Article()
        data.title = title
        data.img_url = latest_file
        data.category_id = 1
        data.save()
        return Response({"message": "성공"}, status=status.HTTP_200_OK)

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

        # order_text ='style_transfer tmp/content.jpg tmp/content2.jpg'

        # os.system(order_text)
        shutil.rmtree('tmp/')

        list_of_files = glob.glob('data/*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)

        data=Article()
        data.title = title
        data.img_url = latest_file
        data.category_id=2
        data.save()
        return Response({"message": "성공"}, status=status.HTTP_200_OK)

class CommentView(APIView):
    # 작성자가 로그인한 경우에만 댓글 작성 할 수 있도록 권한 설정 
    # permission_classes = [permissions.IsAuthenticated]

    def get(self,request,comment_id):
        comment = CommentModel.objects.get(id=comment_id)
        serialized_data = CommentSerializer(comment, many=True).data   #queryset
        return Response(serialized_data, status=status.HTTP_200_OK)

    #댓글 작성
    def post(self,request):
        request.data["user"] = request.user.id # 로그인한 사용자
        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(comment_serializer.data,status=status.HTTP_400_BAD_REQUEST)

    #업데이트
    def put(self,request):
        return Response({"message":"업데이트 완료!"},status=status.HTTP_200_OK)

    #삭제
    def delete(self,request,comment_id):
        comment = CommentModel.objects.get(id=comment_id)
        comment.delete()
        return Response(status=status.HTTP_200_OK)
