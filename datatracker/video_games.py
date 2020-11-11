class VideoGame:
    def __init__(self,_id, rank,name,platform,year,genre,publisher,naSales,euSales,jpSales,otherSales,globalSales):
        self._id = _id
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre