from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор модели Follow"""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                {"detail": "вы не можете подписаться на себя"}
            )
        return data

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны'
            )
        ]


class GroupSerializers(serializers.ModelSerializer):
    """Сериализатор модели Group"""
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializers(serializers.ModelSerializer):
    """Сериализатор модели Post"""
    author = serializers.StringRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    author_name = serializers.CharField(source='author.username', default='', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date', 'author_name')
        model = Post


class CommentSerializers(serializers.ModelSerializer):
    """Сериализатор модели Comment"""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)
