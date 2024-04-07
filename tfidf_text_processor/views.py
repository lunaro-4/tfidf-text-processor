import json
from logging import raiseExceptions
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.sites import csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.serializers import serialize

from tfidf_text_processor.logic import main
# from django.core.urlsol
from .forms import UploadFileForm
from .models import InputTextFile 


LIST_MEM = []


@cache_page(60 * 15)
@csrf_protect
def show_home(request):
    return render(request=request, template_name='home.html')


@cache_page(60 * 15)
@csrf_protect
def file_handling_w_list(request, context, file_id):
    f = InputTextFile.objects.get(pk = file_id).file.open('r')
    outp = main([f] )
    context['outp'] = outp
    

    return render(request, 'home.html', context=context)


@cache_page(60 * 15)
@csrf_protect
def file_handling(request, context):
    uploaded_file = request.FILES.get('file')
    library_id = request.POST.get('library_id')
    new_file = InputTextFile(file = uploaded_file, library_id = library_id)
    new_file.save()
    f = new_file.file.open('r')
    context['form']= UploadFileForm
    outp = main([f])
    context['outp'] = outp
    print("New file uploaded!", new_file.file)
    return render(request, 'home.html', context=context)

def serializer(query):
    jsoned = serialize("json", query)
    jsoned = json.loads(jsoned)
    return jsoned
    
@cache_page(60 * 15)
@csrf_protect
def library_handling(request, context, library_id):
    file_list = InputTextFile.objects.filter(library_id=library_id).only('file', 'id')
    file_list = serializer(file_list)
    for file in file_list:
        file['fields']['file'] = file['fields']['file'].replace(')', '').replace("'",'').replace('(','').replace(',','')
    context['file_list'] = file_list
    request.session['file_list'] = file_list
    return render(request, 'home.html', context=context)

@cache_page(60 * 15)
@csrf_protect
def library_handling_1(request, context, library_id):
    file_list = InputTextFile.objects.filter(library_id=library_id).values_list('file')
    file_list = [ str(file).replace(')', '').replace("'",'').replace('(','').replace(',','') for file in file_list]
    context['file_list'] = file_list
    request.session['file_list'] = file_list
    return render(request, 'home.html', context=context)


@cache_page(60 * 15)
@csrf_protect
def main_view(request, file_list = None):
    context = {}
    context['file_list'] =request.session.get('file_list', '')
    context['library_id_show'] = 123
    context['form']= UploadFileForm
    context['library'] = {}
    if request.method == 'POST' and request.FILES:
        return file_handling(request, context)
    elif request.method == 'POST' and 'library_choice' in request.POST:
        return library_handling(request, context, request.POST.get('library_id_show'))
    elif request.method == 'GET':
        return file_handling_w_list(request, context, request.GET.get('file'))
    return render(request, 'home.html', context=context)


