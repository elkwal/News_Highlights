import urllib.request,json

from .models import Source,Articles

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

api_key=None

base_url_source=None

base_url_articles=None
