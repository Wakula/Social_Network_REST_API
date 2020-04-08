from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics


from api.apps.posts import serializers
from api.apps.posts.models import Post, Like


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    @method_decorator(login_required)
    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author_profile=request.user.profile)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class PostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def _create_response(self, message, error_message):
        if not error_message:
            data = {'like': message}
            return Response(data, status.HTTP_201_CREATED)
        if error_message == 'post does not exist':
            status_code = status.HTTP_404_NOT_FOUND
        else:
            status_code = status.HTTP_200_OK
        return Response({'like': error_message}, status_code)

    def post(self, request, pk):
        user_profile = request.user.profile
        error_message = user_profile.like_post_or_get_error_message(pk)
        return self._create_response('post liked', error_message)

    def delete(self, request, pk):
        user_profile = request.user.profile
        error_message = user_profile.unlike_post_or_get_error_message(pk)
        return self._create_response('post unliked', error_message)


class LikeAnalyticsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LikeAnalyticsSerializer

    def get_queryset(self):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        user_profile = self.request.user.profile
        return Like.objects.get_analytics(user_profile, date_from, date_to)
