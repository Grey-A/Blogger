from django.urls import path

from .views import ArticleDetailView, IndexView, CategoryView, CategoryListView, Subscribe


urlpatterns = [
    path('', IndexView.as_view(), name="homepage"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('subscribe/', Subscribe, name="subscribe")
]