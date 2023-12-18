from DAO.implementation import DbConnection

class Artwork(DbConnection):
    def __init__(self):
        self.ArtworkID=''
        self.Title=''
        self.Description=''
        self.CreationDate=''
        self.Medium=''
        self.ImageURL=''
        self.ArtistID=''


    def create(self):
        create_str='''create  table  if not exists Artwork
        (
        ArtworkID INT PRIMARY KEY,
        Title VARCHAR(200),
        Description TEXT,
        CreationDate DATE,
        Medium VARCHAR(200),
        ImageURL VARCHAR(200),
        Artist_ID INT,
        FOREIGN KEY (Artist_ID) REFERENCES Artist(ArtistID)
        )'''
        self.open()
        self.s.execute(create_str)
        self.s.close()
        print('Table created successfully------:')
obj=Artwork()
obj.create()