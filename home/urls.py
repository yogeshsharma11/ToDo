from django.contrib import admin
from django.urls import path, include
from home.views import home , login , signup , add_todo , signout,delete_todo, change_todo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/',login, name='login'),
    path('signup/',signup, name='signup'),
    path('add-todo/',add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo),
    path('logout/', signout),





]