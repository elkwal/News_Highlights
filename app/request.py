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


def process_results(source_list):

   source_results = []
   for source_item in source_list:
       id = source_item.get('id')
       name = source_item.get('name')
       source_object = Source(id,name)
       source_results.append(source_object)
   return source_results
def get_articles(id):
   '''
   Function that gets the json response to our url request
   '''


   get_articles_url = base_url_articles.format(id,api_key)
   with urllib.request.urlopen(get_articles_url) as url:
       get_articles_data = url.read()
       get_articles_response = json.loads(get_articles_data)
       articles_results = None

       if get_articles_response['articles']:
           articles_results_list = get_articles_response['articles']
           articles_results = process_article_results(articles_results_list)

   return articles_results


def process_article_results(articles_list):

   articles_results = []
   for article_item in articles_list:
       source=article_item.get('source')
       author=article_item.get('author')
       title=article_item.get('title')
       description=article_item.get('description')
       url=article_item.get('url')
       urlToImage=article_item.get('urlToImage')
       publishedAt=article_item.get('publishedAt')


       articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
       articles_results.append(articles_object)
   return articles_results
