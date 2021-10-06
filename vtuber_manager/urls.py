from django.urls import path
from . import views

app_name = "VM"
urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('talent/<int:pk>/', views.TalentDetailView.as_view(), name='talentDetail'),
    path('talent_create/', views.TalentCreateView.as_view(), name='TalentCreate'),
    path('talent_update/<int:pk>/', views.TalentUpdateView.as_view(), name='TalentUpdate'),
    path('talent_delete/<int:pk>/', views.TalentDeleteView.as_view(), name='TalentDelete'),
]
