import pdb
import unittest

from app import app as flickrlive_app


class FlickrLiveTestCase(unittest.TestCase):

    def setUp(self):
        flickrlive_app.config['TESTING'] = True
        self.app = flickrlive_app.test_client()

    def test_homepage_shows_initial_flickr_feed(self):
        """ The homepage should be able to display an initial
            set of public feed from Flickr as well as a search box.

        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        # Check if there are feed items are the page.
        self.assertIn('class="item"', response.data)

        # Check if the query search box in the page.
        self.assertIn('name="q"', response.data)

    def test_homepage_able_to_search_flickr_feed_via_tags(self):
        """ The homepage search box should be able to search Flickr's
            public feed via their tags and display the images.

        """
        search_term = 'dogs'

        # Check if we're able to perform a search.
        response = self.app.get('/?q=' + search_term)
        self.assertEqual(response.status_code, 200)

        # Check if there are feed items are the page.
        self.assertIn('class="result-item"', response.data)

        # Check if the search term is on the page.
        self.assertIn(search_term, response.data)


if __name__ == '__main__':
    unittest.main()
