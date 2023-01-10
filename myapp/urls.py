from django.urls import path
from myapp import views

urlpatterns = [
    # path('myapi/', views.api_list),
    # path('api_details/<int:pk>/', views.api_detail),
    #  path('blog/', views.BlogList.as_view()),
    #  path('api_data/<int:pk>/', views.ApiDetail.as_view()),
    
    path('gav/', views.ContactList.as_view()),
    path('gavDetails/<int:pk>/', views.ContactDetail.as_view()),
    
    
    
]