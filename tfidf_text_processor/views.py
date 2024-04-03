from logging import raiseExceptions
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.sites import csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.views.generic.edit import CreateView
# from django.core.urlsol
from .forms import UploadFileForm
from .models import InputTextFile 

@cache_page(60 * 15)
@csrf_protect
def show_home(request):
    return render(request=request, template_name='home.html')





@cache_page(60 * 15)
@csrf_protect
# def main_view(request):
def examp_func(request):
    context = {}
    if request.method == "POST":
        print(request.FILES)
        form = UploadFileForm(data=request.POST, files=request.FILES)
        # if form.is_valid():
        print('valid')
        new_file = InputTextFile(file = request.FILES['textfile']) 
        new_file.save()
            # return HttpResponse(reverse('tfidf_text_processor.views.main_view'))
    else:
        form =  UploadFileForm()
    file_list = InputTextFile.objects.all()
    return render(request,
                            "home.html",
                              {'file_list': file_list,"form": form},
                              )

@cache_page(60 * 15)
@csrf_protect
def main_view(request):
    context = {}
    context['form']= UploadFileForm
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES.get('file')
        new_file = InputTextFile(file = uploaded_file) 
        new_file.file
        new_file.save()

        context['form']= UploadFileForm
        print("New file uploaded!", new_file.file)
        return render(request, 'home.html', context=context)
    # elif request.method == "GET":
    else:
        return render(request, 'home.html', context=context)
    # else:
    #     raise Exception()


