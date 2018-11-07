from cadastroaluno import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url



admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cadastro/$', views.Aluno.as_view(), name='cadastro'),
    url(r'^professor/$', views.Professor.as_view(), name='professor'),
    url(r'^disciplina/$', views.Disciplina.as_view(), name='disciplina'),
	
    #url(r'^admin/', include(admin.site.urls)),
]   

