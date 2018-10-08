from flask import render_template
from . import main
from ..models import Source
from ..request import get_sources, get_articles


@main.route('/')
def index():
    sources=get_sources()
    print(sources)
    title = 'Home - Welcome to News-Highlight'
    return render_template('index.html', title=title, sources=sources)
@main.route('/articles/<string:id>')
def source(id):
    articles=get_articles(id)
    print(articles)
    return render_template('articles.html',news=articles, name='News Highlights')
