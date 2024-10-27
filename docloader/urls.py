from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # For rendering the main HTML page
    path('api/documents/', views.list_documents, name='list_documents'),  # For listing documents
    path('api/documents/add/', views.add_document, name='add_document'),  # For adding a new document
    path('api/documents/<int:doc_id>/delete/', views.delete_document, name='delete_document'),  # For deleting a document
    path('api/documents/filter/', views.filter_documents_by_user, name='filter_documents_by_user'),  # For filtering documents
]
