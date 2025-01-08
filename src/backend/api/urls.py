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
        "articles/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="article-detail",
    ),
    path(
        "articles/<slug:slug>/delete/",
        views.ArticleDelete.as_view(),
        name="article-delete",
    ),
    path(
        "articles/<slug:slug>/update/",
        views.ArticleUpdate.as_view(),
        name="article-update",
    ),
    path(
        "users/me/",
        views.UserDetailView.as_view(),
        name="user-detail",
    ),
    path(
        "users/signup/",
        views.UserCreateAPIView.as_view(),
        name="user-signup",
    ),
    # path(
    #     "users/me/delete/",
    #     views.UserDeletelView.as_view(),
    #     name="user-delete",
    # ),
]
