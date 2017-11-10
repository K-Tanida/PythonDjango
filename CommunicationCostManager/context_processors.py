from django.contrib.staticfiles.storage import staticfiles_storage

def static_dir(request):
    return {'static_dir': staticfiles_storage.url}
