import unittest
from ..models import Source


class SourcesTest(unittest.TestCase):
    """
    Test case to test the behavior of the Sources class
    """

    def setUp(self):
        """
        Setup function that will run before every test
        """
        self.new_source = Sources('newsbyGatetee', 'My News', 'get the latest updates', 'https://google.com', 'general',
                                  'ke')
