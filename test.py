try:
    from app import app
    import unittest
except Exception as e:
    print("some modules are missing{}".format(e))

class Flasktest(unittest.TestCase):
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("/fo")
        statuscode=response.status_code
        self.assertEqual(response.status_code,200)
    def test_page_load(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertFalse(b'URL Shortener' in response.data)
    def test_req_link(self):
        tester=app.test_client(self)
        response=tester.get('/',follow_redirects=True)
        self.assertTrue(b'' in response.data)
    def test_shorturl(self):
        tester=app.test_client(self)
        response=tester.get('/',follow_redirects=True)
        self.assertTrue(b'' in response.data)

if __name__=="__main__":
    unittest.main()
