

# FILE NOT IN USE ANYMORE
from django.urls import path

from blog.api_views import post_list, post_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)