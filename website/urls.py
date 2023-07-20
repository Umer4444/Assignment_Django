from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('howitworks/', views.howitworks, name='howitworks'),
    path('reviews/', views.reviews, name='reviews'),
    path('blog/', views.blog, name='blog'),
    path('homeworkanswer/', views.homeworkanswer, name='homeworkanswer'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('economics/', views.economics, name='economics'),
    path('engineering/', views.engineering, name='engineering'),
    path('mathematics/', views.mathematics, name='mathematics'),
    path('physics/', views.physics, name='physics'),
    path('programming/', views.programming, name='programming'),
    path('orders/', views.orders, name='orders'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('submit/', views.submit, name='submit'),

]
