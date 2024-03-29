from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os
import glob
import copy
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import shutil
from .models import Article
from .models import Comment as CommentModel
from .serializers import ArticleSerializer
from gallery1.main import mix

from article.serializers import CommentSerializer



class ArticleGallery1View(APIView):

    def get(self, request):
        articles = Article.objects.filter(category_id=1)
        articles = ArticleSerializer(articles, many=True).data
        return Response(articles, status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get("title", "")
        file = request.data.get("file")
        user = request.data.get("user", "")
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
        img_url = os.path.abspath(latest_file)

        article = {'user': user, 'title': title, 'img_url': img_url, 'category': 1}
        article_serializer = ArticleSerializer(data=article)
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)

        else:
            os.remove(latest_file)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            print(article)
        except Article.DoesNotExist:
            return Response({"error": "존재하지 않는 게시물입니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        article_serializer = ArticleSerializer(article, data=request.data, partial=True)
        print(request.data)
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, article_id):
        user = request.user.id
        print(user)
        article = Article.objects.filter(id=article_id)
        if user == article[0].user_id:
            try:
                os.remove(article[0].img_url)
            except:
                article.delete()
            article.delete()

            return Response({"message": "게시물이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "실패."}, status=status.HTTP_400_BAD_REQUEST)


class ArticleGallery2View(APIView):
    def get(self, request):
        articles = Article.objects.filter(category_id=2)
        articles = ArticleSerializer(articles, many=True).data
        return Response(articles, status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get("title", "")
        file1 = request.data.get("file1")
        file2 = request.data.get("file2")
        user = request.data.get("user")
        default_storage.save('tmp/content.jpg', ContentFile(file1.read()))
        default_storage.save('tmp/content2.jpg', ContentFile(file2.read()))

        order_text ='style_transfer tmp/content.jpg tmp/content2.jpg'

        os.system(order_text)

        shutil.rmtree('tmp/')

        list_of_files = glob.glob('data/*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        img_url= os.path.abspath(latest_file)
        article = {'user': user, 'title': title, 'img_url': img_url, 'category': 2}
        article_serializer = ArticleSerializer(data=article)
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)

        else:
            os.remove(latest_file)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response({"error": "존재하지 않는 게시물입니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        article_serializer = ArticleSerializer(article, data=request.data, partial=True)

        if article_serializer.is_valid(raise_exception=True):
            article_serializer.save()
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        user = self.request.user.id
        print(user)
        article = Article.objects.filter(id=article_id)
        if user == article[0].user_id:
            try:
                os.remove(article[0].img_url)
            except:
                article.delete()
            article.delete()

            return Response({"message": "게시물이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "실패."}, status=status.HTTP_400_BAD_REQUEST)




class CommentView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self,request,article_id):
        comment = CommentModel.objects.filter(article=article_id)
        serialized_data = CommentSerializer(comment, many=True).data   #queryset
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self,request,article_id):
        data = copy.deepcopy(request.data)
        data["user"] = request.user.id
        data["article"] = article_id
        data["content"] = request.data.get("content","")
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response({"result":"댓글 작성 완료!"},status=status.HTTP_200_OK)
        else:
            return Response({"result":"댓글 작성 실패!"},status=status.HTTP_400_BAD_REQUEST)

    #업데이트
    def put(self,request,comment_id):
        content = CommentModel.objects.get(id=comment_id)
        comment_serializer = CommentSerializer(content, data=request.data, partial=True)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_200_OK)

        return Response(comment_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    #삭제
    def delete(self,request,comment_id):
        user = request.user.id
        comment = CommentModel.objects.get(id=comment_id)
        if user == comment.user_id:
            comment.delete()
            return Response({"message": "댓글 삭제 완료."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "댓글 삭제 실패."},status=status.HTTP_400_BAD_REQUEST)
        # comment = CommentModel.objects.get(id=comment_id)
        # print(comment)
        # comment.delete()
        # return Response(status=status.HTTP_200_OK)




class ArticleMyGalleryView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user.id
        articles = Article.objects.filter(user_id=user)
        articles = ArticleSerializer(articles, many=True).data

        return Response(articles, status=status.HTTP_200_OK)

    def delete(self, request, article_id):
        user = request.user.id
        article = Article.objects.filter(id=article_id)
        if user == article[0].user_id:
            try:
                os.remove(article[0].img_url)
            except:
                article.delete()
            article.delete()
            return Response({"message": "게시물이 삭제되었습니다."}, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
