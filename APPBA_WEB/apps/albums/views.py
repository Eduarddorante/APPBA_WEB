from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext

from .forms import UploadImageForm

@@login_required

class upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()
          return render_to_response('albums/upload.html', locals(), context_instance=RequestContext(request))


 class home_view(request):
    return render_to_response('base3.html')


