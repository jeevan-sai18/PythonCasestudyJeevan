from DAO.implementation import DbConnection

class Artist(DbConnection):
    def __init__(self):
        self.ArtistID=''
        self.Name=''
        self.Biography=''
        self.BirthDate=''
        self.Nationality=''
        self.Website=''
        self.ContactInformation=''

    def create(self):
        create_str='''create  table  if not exists Artist
        (
        ArtistID INT PRIMARY KEY,
        Name VARCHAR(200),
        Biography TEXT,
        BirthDate DATE,
        Nationality VARCHAR(200),
        Website VARCHAR(200),
        ContactInformation VARCHAR(200)
        )'''
        self.open()
        self.s.execute(create_str)
        print('Table created successfully------:')
        self.s.close()
obj=Artist()
obj.create()
