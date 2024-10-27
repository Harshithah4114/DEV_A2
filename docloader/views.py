from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Document
import json

def index(request):
    return render(request, 'index.html')  # Render the HTML template

def list_documents(request):
    documents = Document.objects.all().values('id', 'name', 'createdDate', 'createdBy', 'fileUrl')
    return JsonResponse(list(documents), safe=False)

@csrf_exempt
def add_document(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        created_date = request.POST.get('createdDate')
        created_by = request.POST.get('createdBy')
        
        file = request.FILES.get('file')
        
        # Save the file
        if file:
            file_url = default_storage.save(file.name, ContentFile(file.read()))
            file_url = default_storage.url(file_url)
        else:
            file_url = None
        
        # Create the document instance
        document = Document.objects.create(
            name=name,
            createdDate=created_date,
            createdBy=created_by,
            fileUrl=file_url
        )
        
        response_data = {
            'id': document.id,
            'name': document.name,
            'createdDate': document.createdDate.isoformat(),
            'createdBy': document.createdBy,
            'fileUrl': document.fileUrl
        }
        
        return JsonResponse(response_data)

@csrf_exempt
def delete_document(request, doc_id):
    if request.method == 'DELETE':
        document = get_object_or_404(Document, id=doc_id)
        if document.fileUrl:
            default_storage.delete(document.fileUrl)
        document.delete()
        return JsonResponse({'status': 'success'})

def filter_documents_by_user(request):
    filter_by_user = request.GET.get('filterByUser', '')
    documents = Document.objects.filter(createdBy__icontains=filter_by_user).values('id', 'name', 'createdDate', 'createdBy', 'fileUrl')
    return JsonResponse(list(documents), safe=False)
