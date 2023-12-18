class UserNotFoundException(Exception):
    def __init__(self,message="User not found"):
        self.message=message
        super().__init__(self.message)
class User:
    def __init__(self,user_id,name,email,password,contact_number,address):
        self.UserID=user_id
        self.Name=name
        self.Email=email
        self.Password=password
        self.ContactNumber=contact_number
        self.Address=address

def get_user_by_id(user_list, user_id):
    for user in user_list:
        if user.UserID==user_id:
            return user
    raise UserNotFoundException()

user_list=[User(1, "John Doe", "john@example.com", "password123", "1234567890", "123 Main St"),
            User(2, "Jane Smith", "jane@example.com", "pass456", "9876543210", "456 Oak St")]
class UserException:
    def RaiseException(self):
        try:
            user_id_to_find=int(input("Enter user_id:"))
            found_user=get_user_by_id(user_list, user_id_to_find)
            print(f"User found: {found_user.Name} ({found_user.Email})")
        except UserNotFoundException:
            print("User not found. Invalid ID.")
        except Exception as e:
            print(f"Unexpected error: {e}")
