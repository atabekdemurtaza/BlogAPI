from django.urls import path
"""from posts.views import PostViewSet
from posts.views import PostDetail
from posts.views import UserViewSet
from posts.views import UserDetail"""
from rest_framework.routers import SimpleRouter
from posts.views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls


"""urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list'),
]"""