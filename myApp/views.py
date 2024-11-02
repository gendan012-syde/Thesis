from django.shortcuts import render
import cloudinary
from django.http import JsonResponse
from cloudinary import CloudinaryImage

def delete_file(request):
    if request.method == 'POST':
        try:
            public_id = request.POST.get('public_id')  # Get the public ID from the request
            CloudinaryImage(public_id).delete()  # Delete the file from Cloudinary
            return JsonResponse({'result': 'ok'})  # Successful deletion response
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)  # Handle errors
    return JsonResponse({'error': 'Invalid request'}, status=400)  # Handle non-POST requests


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def upload_media(request):
    return render(request, 'upload_media.html')