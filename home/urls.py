from django.urls import path
from . import views
import debug_toolbar


#urlconfig
urlpatterns = [
    path('home/', views.home,name='home'),
    path('authorized/', views.authorized),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name= 'logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),

]