from django import urls
from EmployeeAPP import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('department/', views.departmentApi),
    # path('department/<int:id>', views.departmentApi),
    path('department/', views.departmentView.as_view()),
    path('department/<int:id>', views.departmentView.as_view()),
    path('employee/', views.employeeApi),
    path('employee/<int:id>', views.employeeApi),

    #url(r'^SaveFile$', views.SaveFile)   
    path('SaveFile/', views.SaveFile),
    path('auth/', obtain_auth_token),
]
    
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


# user vinhtran pass Welcome12345