from django.urls import path, include
from dictionary.views import DictView, DictDetailView, Search, create, DictUpdateView, DictDeleteView

app_name = 'dictionary'


urlpatterns = [
    path('', DictView.as_view(), name='dict'),
    path('<int:pk>/', DictDetailView.as_view(), name='dict_detail'),
    path('search/', Search.as_view(), name='search'),
    path('create/', create, name='create'),
    path('<int:pk>/update', DictUpdateView.as_view(), name='dict_update'),
    path('<int:pk>/delete', DictDeleteView.as_view(), name='dict_delete'),
]
