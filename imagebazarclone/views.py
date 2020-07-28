from django.shortcuts import render
from imagebazarclone.models import *

# Create your views here.
def home(request):

    cat = Categories.objects.all()
    images = Images.objects.all()

    Data = {'images':images , 'Category':cat }
    return render(request, 'imagebazarclone/home.html', Data)



def upload(request):
    if request.method == 'GET':
        return render(request, 'imagebazarclone.upload.html')
    else:
        pass


