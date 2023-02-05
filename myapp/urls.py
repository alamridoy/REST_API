from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('myapi/', views.api_list),
    # path('api_details/<int:pk>/', views.api_detail),
    #  path('blog/', views.BlogList.as_view()),
    #  path('api_data/<int:pk>/', views.ApiDetail.as_view()),
    
    path('gav/', views.ContactList.as_view(),name='contact-list'),
    path('gavDetails/<int:pk>/', views.ContactDetail.as_view()),
    path('', views.api_root),
    
    
    
])