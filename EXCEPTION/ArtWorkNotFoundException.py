class ArtWorkNotFoundException(Exception):
    def __init__(self,message="Artwork not found"):
        self.message=message
        super().__init__(self.message)
class ArtWork:
    def __init__(self,artwork_id,title,artist,year,medium):
        self.ArtworkID=artwork_id
        self.Title=title
        self.Artist=artist
        self.Year=year
        self.Medium=medium
def get_artwork_by_id(artwork_list,artwork_id):
    for artwork in artwork_list:
        if artwork.ArtworkID==artwork_id:
            return artwork
    raise ArtWorkNotFoundException()

artwork_list = [ArtWork(1,"Starry Night","Vincent van Gogh",1889,"Oil on canvas"),
                ArtWork(2,"Mona Lisa","Leonardo da Vinci",1503,"Oil on wood"),]
class ArtworkException:
    def RaiseException(self):
        try:
            artwork_id_to_find=int(input("Enter artwork_id:"))
            found_artwork=get_artwork_by_id(artwork_list, artwork_id_to_find)
            print(f"Artwork found: {found_artwork.Title} by {found_artwork.Artist}")
        except ArtWorkNotFoundException:
            print("Artwork not found. Invalid ID.")
        except Exception as e:
            print(f"Unexpected error: {e}")
