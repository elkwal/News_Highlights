import unittest
from .models import Source


class SourcesTest(unittest.TestCase):
    """
    Test case to test the behavior of the Sources class
    """

    def setUp(self):
        """
        Setup function that will run before every test
        """
        self.new_source = Sources('newsbyelkwal', 'My News')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_to_check_instance_variables(self):
        """
        Test function to check instance variables
        """
        self.assertEquals(self.new_source.id, 'newsbyelkwal')
        self.assertEquals(self.new_source.name, 'My News')
    
