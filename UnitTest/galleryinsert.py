import unittest
from DAO.Galllery import Gallery

class TestGalleryDAOInsert(unittest.TestCase):
    def setUp(self):
        self.gallery_dao=Gallery()

    def test_insert_gallery(self):
        result=self.gallery_dao.setter()
        self.assertTrue(result,True)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
