from logging import raiseExceptions
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.sites import csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.views.generic.edit import CreateView

from tfidf_text_processor.logic import main
# from django.core.urlsol
from .forms import UploadFileForm
from .models import InputTextFile 




@cache_page(60 * 15)
@csrf_protect
def show_home(request):
    return render(request=request, template_name='home.html')



@cache_page(60 * 15)
@csrf_protect
def file_handling(request, context):
    uploaded_file = request.FILES.get('file')
    new_file = InputTextFile(file = uploaded_file) 
    new_file.file
    new_file.save()
    f = new_file.file.open('r')
    context['form']= UploadFileForm
    print("New file uploaded!", new_file.file)
    outp = main([f])
    context['outp'] = outp
    return render(request, 'home.html', context=context)


@cache_page(60 * 15)
@csrf_protect
def library_handling(request, context):
    return render(request, 'home.html', context=context)



@cache_page(60 * 15)
@csrf_protect
def main_view(request, library_id = None):
    context = {}
    context['library_id_show'] = 123
    context['form']= UploadFileForm
    context['library'] = {}
    if request.method == 'POST' and request.FILES:
        return file_handling(request, context)
    elif request.method == 'POST' and 'library_choice' in request.POST:
        return library_handling(request, context)
    else:
        return render(request, 'home.html', context=context)


