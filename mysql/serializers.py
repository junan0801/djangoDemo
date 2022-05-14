from rest_framework import serializers
from .models import BookInfo

# 继承ModelSerializer，自动序列化

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

# 继承Serializer，手动序列化


# class BookInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     btitle = serializers.CharField(max_length=20, label='名称')
#     bpub_data = serializers.CharField(max_length=20, label='发布日期')
#
#     def create(self, validated_data):
#         book = BookInfo.objects.create(**validated_data)
#         return book
#
#     def update(self, instance, validated_data):
#         instance.btitle = validated_data.get('btitle')
#         instance.bpub_data = validated_data.get('bpub_data')
#         instance.save()
#         return instance