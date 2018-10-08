import urllib.request,json

from .models import Source,Articles

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

api_key=None

base_url_source=None

base_url_articles=None

def configure_request(app):
   global api_key,base_url_source,base_url_articles
   api_key = app.config['NEWS_API_KEY']
   base_url_source= 'https://newsapi.org/v2/sources?apiKey=89fe8fe3d6ee4ea89aa68bfb28eeb543'
   base_url_articles=app.config['ARTICLES_BASE_URL']

def get_sources():
   '''
   Function that gets the json response to our url request
   '''

   get_source_url = base_url_source.format(api_key)
   with urllib.request.urlopen(get_source_url) as url:
       get_source_data = url.read()
       get_source_response = json.loads(get_source_data)

       source_results = None

       if get_source_response['sources']:
           source_results_list = get_source_response['sources']
           source_results = process_results(source_results_list)
           print(source_results)

   return source_results
