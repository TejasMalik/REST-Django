from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import serializers
import json
from api import models
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class ArticleList(ListAPIView):
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer

class ArticleDetail(RetrieveAPIView):
    queryset = models.Articles.objects.all()
    serializer_class = serializers.ArticleSerializer


class Student():
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


@api_view()
def articleApi(request):
    articles = models.Articles.objects.all()
    response = serializers.ArticleSerializer(articles, many=True)
    return Response(response.data)


@api_view(['POST'])
def createArticleApi(request):
    body = json.loads(request.body)
    response = serializers.ArticleSerializer(data = body)
    if response.is_valid():
        inst = response.save()
        response = serializers.ArticleSerializer(inst)
        return Response(response.data)

    return Response(response.errors)



@api_view()
def usersApi(request):
    student1 = Student("Tejas", 1, 100)
    student2 = Student("Hitesh", 2, 75)
    student3 = Student("Rohan", 3, 50)

    response = serializers.StudentSerializer([
        student1,
        student2,
        student3
    ], many=True)

    return Response(response.data)
