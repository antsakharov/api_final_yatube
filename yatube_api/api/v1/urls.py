from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.v1.views import CommentViewSet, FollowViewSet, GroupViewSet, \
    PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                'comments')
router.register('follow', FollowViewSet,
                'follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
