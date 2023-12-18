from DAO.implementation import DbConnection

class User(DbConnection):
    def __init__(self):
        self.UserID=''
        self.Username=''
        self.Password=''
        self.Email=''
        self.FirstName=''
        self.LastName=''
        self.DateofBirth=''
        self.ProfilePicture=''

    def create(self):
        create_str='''create  table  if not exists User
        (
        UserID INT PRIMARY KEY,
        Username VARCHAR(200),
        Password VARCHAR(200),
        Email VARCHAR(200),
        FirstName VARCHAR(200),
        LastName VARCHAR(200),
        DateOfBirth DATE,
        ProfilePicture VARCHAR(200)
        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Table created successfully------:')
obj=User()
obj.create()