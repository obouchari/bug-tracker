from unittest import TestCase

from app import app


class AppEndPointsTestCase(TestCase):
    """
    This is where we test all of our app's endpoints
    """

    def test_sample(self):
        """
        This is testing our root endpoint,
        """
        with app.test_client() as client:
            res = client.get('/')
            text = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Welcome to Flask!', text)
