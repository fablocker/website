import os
import sys
path = '/home/bogdanvarlamov/test-app'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'test-app.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()