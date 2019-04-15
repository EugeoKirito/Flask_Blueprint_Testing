import json
import unittest
from manage import app

class   LoginTest(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()


    def test_empty_username_password(self):

        # client=app.test_client()
        # ret=client.post('/login',data={})
        ret=self.client.post('/login',data={})



        ret=ret.data
        print(ret)
        resp=json.loads(ret)
        self.assertIn('code',resp)
        self.assertEqual(resp['code'],1)


if __name__ == '__main__':
    unittest.main()