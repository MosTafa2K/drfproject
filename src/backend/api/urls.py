from django.urls import path
from . import views


app_name = "api"
urlpatterns = [
    path(
        "articles/",
        views.ArticleListView.as_view(),
        name="article-list",
    ),
    path(
        "articles/new/",
        views.ArticleCreate.as_view(),
        name="article-create",
    ),
    path(
        "articles/<int:pk>/",
        views.ArticleDetailView.as_view(),
        name="article-detail",
    ),
    path(
        "articles/<int:pk>/delete/",
        views.ArticleDelete.as_view(),
        name="article-delete",
    ),
    path(
        "articles/<int:pk>/update/",
        views.ArticleUpdate.as_view(),
        name="article-update",
    ),
    path(
        "users/me/",
        views.SelfUserDetailView.as_view(),
        name="self-user-detail",
    ),
    path(
        "users/signup/",
        views.UserCreateAPIView.as_view(),
        name="user-signup",
    ),
    path(
        "users/",
        views.UsersList.as_view(),
        name="user-list",
    ),
    path(
        "users/<int:pk>",
        views.UserDetailView.as_view(),
        name="user-detail",
    ),
    # path(
    #     "users/me/delete/",
    #     views.UserDeletelView.as_view(),
    #     name="user-delete",
    # ),
]
