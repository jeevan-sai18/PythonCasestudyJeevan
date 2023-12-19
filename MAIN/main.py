from DAO.Artist import Artist
from DAO.Artwork import Artwork
from DAO.User import User
from DAO.Galllery import Gallery

def main_art_entities():
    while True:
        print("Select an option:")
        print("1.Artist")
        print("2.Artwork")
        print("3.User")
        print("4.Gallery")
        print("5.Exit")

        choice=input("Enter your choice: ")

        if choice == '1':
            obj=Artist()
        elif choice == '2':
            obj=Artwork()
        elif choice == '3':
            obj=User()
        elif choice == '4':
            obj=Gallery()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        obj.getter()
        print("............................")
        operation_choice=input("Do you want to perform additional operations? (Y/N): ").upper()
        if operation_choice!='Y':
            break

        print("Select an operation:")
        print("1.Setter")
        print("2.Update")
        print("3.Delete")
        operation=input("Enter your operation choice: ")

        if operation == '1':
            obj.setter()
        elif operation == '2':
            obj.update()
        elif operation == '3':
            obj.delete()
        else:
            print("Invalid operation choice. Returning to the main menu.")

if __name__ == "__main__":
    main_art_entities()

