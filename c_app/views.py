from django.shortcuts import render
from django.http import HttpResponse
import zlib
import os

def home(request):
    return render(request, 'home.html')

def compress_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        compression_level = int(request.POST.get('compression_level', 6))

        data = file.read()
        compressed_data = zlib.compress(data, level=compression_level)

        response = HttpResponse(compressed_data, content_type='application/gzip')
        response['Content-Disposition'] = f'attachment; filename={os.path.splitext(file.name)[0]}_compressed.gz'
        return response

    return HttpResponse('Invalid request', status=400)
