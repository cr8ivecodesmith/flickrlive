# -*- code: utf-8 -*-
from __future__ import unicode_literals

from flask import (
    Flask,
    request,
    render_template,
)

from flickr import Flickr


##### CONFIGURATION
DEBUG = False
SECRET_KEY = 'KeepThisSecretKeySecretOk?'
##### END CONFIGURATION


##### APP MAIN
app = Flask(__name__)
app.config.from_object(__name__)
##### END APP MAIN


##### VIEWS
@app.route('/', methods=['GET'])
def home():
    templates = {
        'home': 'home.html',
        'serp': 'serp.html'
    }
    template = templates.get('home')
    context = {
        'data': {
            'title': '',
            'link': '',
            'description': '',
            'modified': '',
            'generator': '',
            'items': [],
        }
    }
    query = request.args.get('q', '')
    params = {
        'format': 'json',
        'tagmode': 'all'
    }

    if query:
        template = templates.get('serp')
        context['query'] = query
        params['tags'] = query
        params['tagmode'] = 'any'

    context['data'] = Flickr().public_feed(params)
    return render_template(template, **context)

##### END VIEWS


if __name__ == '__main__':
    app.run(host=('0.0.0.0'), port=5011)
