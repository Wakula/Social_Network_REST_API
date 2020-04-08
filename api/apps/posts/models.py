from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from api.apps.posts import managers


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def is_owner(self, post):
        return self == post.author

    def _get_post_or_error_message(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None, 'post does not exist'
        if self.is_owner(post):
            return None, 'can not like|unlike own posts'
        return post, None

    def like_post_or_get_error_message(self, post_id):
        post, message = self._get_post_or_error_message(post_id)
        if message:
            return message
        if self in post.likes.all():
            return 'post was already liked'
        post.likes.add(self)

    def unlike_post_or_get_error_message(self, post_id):
        post, message = self._get_post_or_error_message(post_id)
        if message:
            return message
        if self not in post.likes.all():
            return 'post was not liked'
        post.likes.remove(self)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(Profile, through='Like', related_name='likes')

    def __str__(self):
        return self.title


class Like(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateField(auto_now_add=True)

    objects = managers.LikeManager()
