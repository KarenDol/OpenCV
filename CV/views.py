from django.shortcuts import render
import os
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def save_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        VideoReport = request.POST['VideoReport'] #Реропт о нарушениях
        print(VideoReport)

        # Define the path to save the video (static/videos/)
        static_videos_path = os.path.join(settings.BASE_DIR, 'CV', 'static', 'videos')
        if not os.path.exists(static_videos_path):
            os.makedirs(static_videos_path)

        # Save the file using Django's FileSystemStorage
        fs = FileSystemStorage(location=static_videos_path)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'recorded_video_{timestamp}.webm'  # Use a meaningful name

        fs = FileSystemStorage(location=static_videos_path)
        saved_filename = fs.save(filename, video_file)

        file_url = os.path.join('static', 'videos', saved_filename)

        return JsonResponse({'message': 'Video saved successfully!', 'video_url': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    return render(request, 'home.html')

def faceapi(request):
    return render(request, 'face-api.html')