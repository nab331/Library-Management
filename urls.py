from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dash/', include('dash.urls')),
    url(r'^about/$', views.about),
    url(r'^$', accounts_view.login_view,name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


<<<<<<< HEAD

#HELLO
=======
#TEST
>>>>>>> 5e1b1f8b0b2a43402f484feb4e4b7b50786c15bd
