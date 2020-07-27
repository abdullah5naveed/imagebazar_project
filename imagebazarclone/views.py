from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'imagebazarclone/home.html')



def upload(request):
    if request.method == 'GET':
        return render(request, 'imagebazarclone.upload.html')
    else:
        pass

