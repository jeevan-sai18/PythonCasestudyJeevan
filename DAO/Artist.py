from DAO.implementation import DbConnection

class Artist(DbConnection):

    def setter(self):
        self.ArtistID=int(input('Enter ArtistId:'))
        self.Name=input('Enter Name:')
        self.Biography=input('Enter Biography')
        self.BirthDate=input('Enter date:')
        self.Nationality=input('Enter Nationality:')
        self.Website=input('Enter Website:')
        self.ContactInformation=input('Enter ContactInformation:')
        print(self.ArtistID,self.Name,self.Biography,self.BirthDate,self.Nationality,self.Website,self.ContactInformation)
        data = [(self.ArtistID,self.Name,self.Biography,self.BirthDate,self.Nationality,self.Website,self.ContactInformation)]
        insert_str = '''insert into Artist(ArtistID,Name,Biography,BirthDate,Nationality,Website,ContactInformation) values(%s,%s,%s,%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str, data)
        self.conn.commit()
        print('Records Inserted Successfully..')
        self.close()

    def getter(self):
        self.open()
        select_str='''select * from artist'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records In Artist Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        Id=int(input('Input Artist ID to be Updated'))
        self.Name=input('Enter Name:')
        self.Biography=input('Enter Biography')
        self.BirthDate=input('Enter date:')
        self.Nationality=input('Enter Nationality:')
        self.Website=input('Enter Website:')
        self.ContactInformation=input('Enter ContactInformation:')

        update_str='update artist set Name=%s,Biography=%s,BirthDate=%s,Nationality=%s,Website=%s,ContactInformation=%s where ArtistID=%s'
        self.open()
        data=[(self.Name,self.Biography,self.BirthDate,self.Nationality,self.Website,self.ContactInformation,Id)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print(update_str,data)
        print('Records updated Successfully..')

    def delete(self):
        Id=int(input('Enter the Eid to be deleted:'))
        delete_str=f'delete from artist where ArtistID={Id}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Records Deleted Successfully..')

