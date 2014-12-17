# -*- code: utf-8 -*-
from __future__ import unicode_literals

import ast
import json

import requests


class Flickr(object):
    FLICKR_API = {
        'public_feed': 'https://api.flickr.com/services/feeds/photos_public.gne',
    }
    FLICKR_API_CONFIG = {
        'strip_start': len('jsonFlickrFeed('),
        'strip_end': -1,
    }

    def public_feed(self, params={'format': 'json', 'tagmode': 'all'}):
        response = requests.get(
            self.FLICKR_API.get('public_feed'),
            params=params
        )
        if 'json' in params.get('format', ''):
            return self._to_json(response)
        return response.text

    def _to_json(self, response):
        # NOTE: Flick'r API response is weird because its not in standard
        #       json format, so we have to strip away invalid chars and then
        #       turn the result into a proper json object.
        strip_start = self.FLICKR_API_CONFIG.get('strip_start')
        strip_end = self.FLICKR_API_CONFIG.get('strip_end')
        data = ast.literal_eval(response.text[strip_start:strip_end])
        return json.loads(json.dumps(data))
