from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^upload-img/', 'ckeditor.views.upload', {'image': True}, name='ckeditor_upload_image'),
    url(r'^browse-img/', 'ckeditor.views.browse', {'image': True}, name='ckeditor_browse_image'),
    url(r'^upload/', 'ckeditor.views.upload', name='ckeditor_upload'),
    url(r'^browse/', 'ckeditor.views.browse', name='ckeditor_browse'),
)
