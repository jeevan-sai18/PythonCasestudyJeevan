from DAO.implementation import DbConnection

class Artwork(DbConnection):

    def setter(self):
        self.ArtworkID=int(input('Enter ArtworkId:'))
        self.Title=input('Enter Title:')
        self.Description=input('Enter Description')
        self.CreationDate=input('Enter CreationDate:')
        self.Medium=input('Enter Medium:')
        self.ImageURL=input('Enter ImageURL:')
        self.Artist_ID=input('Enter Artist_ID:')
        print(self.ArtworkID,self.Title,self.Description,self.CreationDate,self.Medium,self.ImageURL,self.Artist_ID)
        data=[(self.ArtworkID,self.Title,self.Description,self.CreationDate,self.Medium,self.ImageURL,self.Artist_ID)]
        insert_str='''insert into Artwork(ArtworkID,Title,Description,CreationDate,Medium,ImageURL,Artist_ID) values(%s,%s,%s,%s,%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Records Inserted Successfully..')
        self.close()
        return True

    def getter(self):
        self.open()
        select_str='''select * from artwork'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records In Artwork Table')
        for i in records:
            print(i)
        self.close()

    def update(self):
        self.getter()
        Id=int(input('Input Artwork ID to be Updated'))
        self.Title=input('Enter Title:')
        self.Description=input('Enter Description')
        self.CreationDate=input('Enter CreationDate:')
        self.Medium=input('Enter Medium:')
        self.ImageURL=input('Enter ImageURL:')
        self.Artist_ID=input('Enter Artist_ID:')

        update_str='update artwork set Title=%s,Description=%s,CreationDate=%s,Medium=%s,ImageURL=%s,Artist_ID=%s where ArtworkID=%s'
        self.open()
        data=[(self.Title,self.Description,self.CreationDate,self.Medium,self.ImageURL,self.Artist_ID,Id)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print(update_str,data)
        print('Records updated Successfully..')
        return True

    def delete(self):
        Id=int(input('Enter the Artworkid to be deleted:'))
        delete_str=f'delete from artwork where ArtworkID={Id}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Records Deleted Successfully..')
        return True



