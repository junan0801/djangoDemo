from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from mysql.serializers import BookInfoModeSerializers
from mysql.models import BookInfo


class BookListAPIView(APIView):

    def get(self, request):
        qs = BookInfo.objects.all()
        serializer = BookInfoModeSerializers(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookInfoModeSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModeSerializers(instance=book)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoModeSerializers(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)


    def delete(self, request, pk):
        # q = BookInfo.objects.get(id=pk)
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

