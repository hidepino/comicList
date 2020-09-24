from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('comic/', views.comic_list, name='comic_list'),   # 一覧
]
