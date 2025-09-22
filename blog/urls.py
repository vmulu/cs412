from django.urls import path
from . views import ArticleView, ShowAllView, RandomArticleView
urlpatterns = [
    path('', RandomArticleView.as_view(), name="random"),
    path('show_all', ShowAllView.as_view(), name="show_all"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),

]