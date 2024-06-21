from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('blog/', PostView.as_view(), name='blog'),
    path('comments/', Commentview.as_view(), name='comments')
]