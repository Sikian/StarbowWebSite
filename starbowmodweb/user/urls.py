from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Wrap our patterns in /site/ to match our deployment environment
urlpatterns = patterns('starbowmodweb.user.views',
    url(r'^home', 'user_home', name='user_home'),
    url(r'^activate', 'user_activate', name='user_activate'),

    # Registration and authorization paths
    url(r'^register', 'user_register', name='user_register'),
    url(r'^not_found', TemplateView.as_view(template_name='not_found.html')),
    url(r'^login_required', TemplateView.as_view(template_name='login_required.html')),
    # This defines ^login and ^logout
    url(r'', include('django_browserid.urls'))
)