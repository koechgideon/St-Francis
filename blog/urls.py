from django.urls import path
# from . import views
from .views import PostView,ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    # path('blog/', views.blog, name="blog"),
    path('blog/', PostView.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
]
