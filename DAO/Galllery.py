from DAO.implementation import DbConnection

class Gallery(DbConnection):
    def setter(self):
        self.GalleryID=int(input('Enter GalleryID:'))
        self.Name=input('Enter Name:')
        self.Description=input('Enter Description:')
        self.Location=input('Enter Location:')
        self.Curator=input('Enter Curator:')
        self.OpeningHours=input('Enter OpeningHours:')
        self.ArtistID=input('Enter ArtistID:')

        print(self.GalleryID,self.Name,self.Description,self.Location,self.Curator,self.OpeningHours,self.ArtistID)

        data=[(self.GalleryID,self.Name,self.Description,self.Location,self.Curator,self.OpeningHours,self.ArtistID)]

        insert_str='''INSERT INTO Gallery(GalleryID,Name,Description,Location,Curator,OpeningHours,ArtistID) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''

        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Records Inserted Successfully..')
        self.close()
        return True

    def getter(self):
        self.open()
        select_str = '''select * from Gallery'''
        self.s.execute(select_str)
        records = self.s.fetchall()
        print('')
        print('Records In Gallery Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        Id=int(input('Input Gallery ID to be Updated'))
        self.Name=input('Enter Name:')
        self.Description=input('Enter Description:')
        self.Location=input('Enter Location:')
        self.Curator=input('Enter Curator:')
        self.OpeningHours=input('Enter OpeningHours:')
        self.ArtistID=input('Enter ArtistID:')

        update_str='update Gallery set Name=%s,Description=%s,Location=%s,Curator=%s,OpeningHours=%s,ArtistID=%s  where GalleryID=%s'
        self.open()
        data=[(self.Name,self.Description,self.Location,self.Curator,self.OpeningHours,self.ArtistID,Id)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print(update_str,data)
        print('Records updated Successfully..')
        return True

    def delete(self):
        Id=int(input('Enter the GalleryID to be deleted:'))
        delete_str=f'delete from Gallery where GalleryID={Id}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Records Deleted Successfully..')
        return True
obj4=Gallery()
#obj4.setter()
obj4.getter()
#obj4.update()
#obj4.delete()
