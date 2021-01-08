from django import urls
from EmployeeAPP import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>', views.departmentApi),
    path('employee/', views.employeeApi),
    path('employee/<int:id>', views.employeeApi),

    #url(r'^SaveFile$', views.SaveFile)   
    path('SaveFile/', views.SaveFile),
] 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)