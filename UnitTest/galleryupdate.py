import unittest
from DAO.Galllery import Gallery

class TestGalleryDAOUpdate(unittest.TestCase):
    def setUp(self):
        self.gallery_dao=Gallery()

    def test_update_gallery(self):
        result=self.gallery_dao.update()
        self.assertTrue(result,True)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
