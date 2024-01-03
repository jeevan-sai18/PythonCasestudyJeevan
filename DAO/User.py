from DAO.implementation import DbConnection

class User(DbConnection):
    def setter(self):
        self.UserID=int(input('Enter UserID:'))
        self.Username=input('Enter Username:')
        self.Password=input('Enter Password:')
        self.Email=input('Enter Email:')
        self.FirstName=input('Enter FirstName:')
        self.LastName=input('Enter LastName:')
        self.DateOfBirth=input('Enter DateOfBirth:')
        self.ProfilePicture=input('Enter Profilepicture')

        print(self.UserID,self.Username,self.Password,self.Email,self.FirstName,self.LastName,self.DateOfBirth,self.ProfilePicture)

        data=[(self.UserID,self.Username,self.Password,self.Email,self.FirstName,self.LastName,self.DateOfBirth,self.ProfilePicture)]

        insert_str='''INSERT INTO User(UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Records Inserted Successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''select * from user'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records In user Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        Id=int(input('Input User ID to be Updated'))
        self.Username=input('Enter Username:')
        self.Password=input('Enter Password')
        self.Email=input('Enter Email:')
        self.FirstName=input('EnterFirstName:')
        self.LastName=input('Enter LastName:')
        self.DateOfBirth=input('Enter DateOfBirth:')
        self.ProfilePicture=input('Enter Profilepicture')

        update_str='update user set Username=%s,Password=%s,Email=%s,FirstName=%s,LastName=%s,DateOfBirth=%s,ProfilePicture=%s where UserID=%s'
        self.open()
        data=[(self.Username,self.Password,self.Email,self.FirstName,self.LastName,self.DateOfBirth,self.ProfilePicture,Id)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print(update_str,data)
        print('Records updated Successfully..')

    def delete(self):
        Id=int(input('Enter the UserId to be deleted:'))
        delete_str=f'delete from User where UserId={Id}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Records Deleted Successfully..')

