from django.conf import settings
from django.conf.urls.defaults import *
from blog.models import PostsSitemap
from minicms.models import PagesSitemap
from registration.forms import RecaptchaRegistrationForm


handler500 = 'djangotoolbox.errorviews.server_error'

sitemaps = {
    'posts': PostsSitemap,
    'pages': PagesSitemap,
}

urlpatterns = patterns('',
    (r'^admin/', include('urlsadmin')),
    (r'^blog/', include('blog.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    (r'^search$', 'google_cse.views.search'),
    (r'^robots\.txt$', 'robots.views.robots'),
	(r'^accounts/', include('registration.urls')),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^accounts/logout/', 'django.contrib.auth.views.logout_then_login'),
)

if 'djangoappengine' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ) + urlpatterns