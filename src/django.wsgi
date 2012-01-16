import os
import sys
path = '/home/bogdanvarlamov/test-app'
if path not in sys.path:
	sys.path.append(path)
app_engine = '/home/bogdanvarlamov/google_appengine'
if app_engine not in sys.path:
	sys.path.append(app_engine)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()