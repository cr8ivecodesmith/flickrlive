# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb
import unittest

from app import app


class TestCase(unittest.TestCase):

    def setup(self):
        # TODO: Initialize the app and selenium here.
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        # TODO: Stop the app and selenium here.
        pass

    def test_homepage_shows_initial_flickr_feed(self):
        """ The homepage should be able to display an initial
            set of public feed from Flickr as well as a search box.

        """
        return self.fail('Write your test here.')

    def test_homepage_able_to_search_flickr_feed_via_tags(self):
        """ The homepage search box should be able to search Flickr's
            public feed via their tags and display the images.

        """
        return self.fail('Write your test here.')


if __name__ == '__main__':
    unittest.main()
