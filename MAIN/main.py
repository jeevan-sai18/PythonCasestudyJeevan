from DAO.Artist import Artist
from DAO.Artwork import Artwork
from DAO.User import User
from DAO.Galllery import Gallery
from UnitTest.Artworkupdate import *
from UnitTest.ArtworkInsert import *
from UnitTest.Artworkdelete import *
from UnitTest.galleryupdate import *
from UnitTest.gallerydelete import *
from UnitTest.galleryinsert import *

def main_art_entities():
    obj = None

    while True:
        print("Select an option:")
        print("1.Artist")
        print("2.Artwork")
        print("3.User")
        print("4.Gallery")
        print("5.Run Artwork Tests")
        print("6.Run Gallery Tests")
        print("7.Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            obj = Artist()
        elif choice == '2':
            obj = Artwork()
        elif choice == '3':
            obj = User()
        elif choice == '4':
            obj = Gallery()
        elif choice == '5':
            run_artwork_tests()
        elif choice == '6':
            run_gallery_tests()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue
        if obj:
            obj.getter()
            print("............................")
            operation_choice = input("Do you want to perform additional operations? (Y/N): ").upper()
            if operation_choice != 'Y':
                break

            print("Select an operation:")
            print("1.Setter")
            print("2.Update")
            print("3.Delete")
            operation = input("Enter your operation choice: ")

            if operation == '1':
                obj.setter()
            elif operation == '2':
                obj.update()
            elif operation == '3':
                obj.delete()
            else:
                print("Invalid operation choice. Returning to the main menu.")

def run_artwork_tests():
    print("Running artwork tests...")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestArtworkDAOUpdate)
    unittest.TextTestRunner().run(test_suite)
    print("Enter artworkId to be Insert: ")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestArtrworkDAOInsert)
    unittest.TextTestRunner().run(test_suite)
    print("Enter Artwork Id to be deleted: ")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestArtworkDAODelete)
    unittest.TextTestRunner().run(test_suite)
    print("Artwork tests completed.")


def run_gallery_tests():
    print("Running gallery tests...")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGalleryDAOUpdate)
    unittest.TextTestRunner().run(test_suite)
    print("Enter gallery Id to be deleted: ")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGalleryDAODelete)
    unittest.TextTestRunner().run(test_suite)
    print("Enter gallery Id to be Inserted: ")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGalleryDAOInsert)
    unittest.TextTestRunner().run(test_suite)
    print("Gallery tests completed.")


if __name__ == "__main__":
    main_art_entities()
