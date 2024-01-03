import unittest
from DAO.Galllery import Gallery

class TestGalleryDAODelete(unittest.TestCase):
    def setUp(self):
        self.gallery_dao=Gallery()

    def test_delete_gallery(self):
        result=self.gallery_dao.delete()
        self.assertTrue(result,True)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
