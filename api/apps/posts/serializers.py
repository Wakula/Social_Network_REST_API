from rest_framework import serializers

from api.apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        read_only_fields = ['author']

    def save(self, *, author_profile):
        post = Post(
            **self.validated_data,
            author=author_profile
        )
        post.save()
        return post


class LikeAnalyticsSerializer(serializers.Serializer):
    date_liked = serializers.DateField()
    likes_amount = serializers.IntegerField()
