from rest_framework import serializers
from .models import Book
#
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields=['title', 'author', 'price', 'genre']
#
# class BookSerializerForAdmin(serializers.ModelSerializer):
#     class Meta:
#         model=Book
#         fields='__all__'
#
# class BookSerializerForAdmin(BookSerializer):
#     genre_name = serializers.CharField(source="genre.name", read_only=True)
#

#---------------------------------------------


# class BookSerializer(serializers.Serializer):
#     id = serializers.BigIntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=255, default="none")
#     price = serializers.IntegerField(default=0)
#     genre_id = serializers.IntegerField(required=False, allow_null=True)
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance: Book, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.author = validated_data.get("author", instance.author)
#         instance.price = validated_data.get("price", instance.price)
#         instance.genre_id = validated_data.get("genre_id", instance.genre_id)
#
#         instance.save()
#
#         return instance
#
#
# class GenreSerializer(serializers.Serializer):
#     id = serializers.BigIntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)







    # def create(self, validated_data):
    #     return Genre.objects.create(**validated_data)
    #
    # def update(self, instance: Genre, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #
    #     instance.save()
    #
    #     return instance

    #-----------------------------



from rest_framework import serializers

from .models import Book, Genre,Comment

from rest_framework import serializers
from .models import Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def validate_name(self, value):
        genres = Genre.objects.filter(name=value)
        if self.instance:
            genres = genres.exclude(pk=self.instance.pk)
        if genres.exists():
            raise serializers.ValidationError("Bunday nomli genre allaqachon mavjud.")
        return value

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255, default="none")
    price = serializers.IntegerField(default=0, min_value=0, max_value=32767)
    genre_id = serializers.IntegerField(required=False, allow_null=True)

    def validate_genre_id(self, value):
        if value is not None and not Genre.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Bunday genre mavjud emas.")
        return value

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.price = validated_data.get("price", instance.price)
        instance.genre_id = validated_data.get("genre_id", instance.genre_id)
        instance.save()
        return instance


class BookSerializerForAdmin(BookSerializer):
    genre_name = serializers.CharField(
        source="genre.name", read_only=True, allow_null=True
    )

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'book', 'author', 'text', 'created_at']