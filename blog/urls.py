from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('new_post/', views.add_blog, name='add_blog'),
    path('logout/', views.user_logout, name='user_logout'),
    path('<int:id>/', views.detail_view, name='detail_view' ),
    path('category/<str:cat>', views.category_view, name='category_view')
]
