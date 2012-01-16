from registration.backends.default.urls import *
from registration.views import register

from .forms import RecaptchaRegistrationForm

urlpatterns = patterns('',
    url(r'^register/$', register,
        {'form_class': RecaptchaRegistrationForm,
		'backend': 'registration.backends.default.DefaultBackend'},
        name='registration.views.register'),
    (r'', include('registration.backends.default.urls')),
)