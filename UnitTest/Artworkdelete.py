import unittest
from DAO.Artwork import Artwork

class TestArtworkDAODelete(unittest.TestCase):
    def setUp(self):
        self.gallery_dao=Artwork()

    def test_update_gallery(self):
        result=self.gallery_dao.delete()
        self.assertTrue(result,True)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
