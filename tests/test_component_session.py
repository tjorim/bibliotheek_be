import unittest
import requests
import logging
# from "../custom_components/bibliotheek_be/utils" import .
import sys
sys.path.append('../custom_components/bibliotheek_be/')
from utils import ComponentSession
from secret import USERNAME, PASSWORD

_LOGGER = logging.getLogger(__name__)

#run this test on command line with: python -m unittest test_component_session

logging.basicConfig(level=logging.INFO)
class TestComponentSession(unittest.TestCase):
    def setUp(self):
        self.session = ComponentSession()

    def test_login(self):
        # Test successful login
        self.session.login(USERNAME, PASSWORD)
        self.assertIsNotNone(self.session.userdetails)
        # _LOGGER.debug(f"userdetails: {self.session.userdetails}")
        
        for id, userdetail in self.session.userdetails.items():
            # _LOGGER.info(f"userdetail: {userdetail}")
            url = userdetail.get('loans').get('url')
            _LOGGER.info(f"url: {url}")
            
            if url:
                _LOGGER.info(f"calling loan details")
                loandetails = self.session.loan_details(url)
                self.assertIsNotNone(loandetails)
                
        # Test login failure
        self.session = ComponentSession()
        try:
            self.session.s = requests.Session() # reset session object
            self.assertEqual(self.session.userdetails,{})
        except AssertionError:
            self.assertEqual(self.session.userdetails,{})
if __name__ == '__main__':
    unittest.main()