from rest_framework.serializers import ModelSerializer
from mysql.models import BookInfo


class BookInfoModeSerializers(ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
