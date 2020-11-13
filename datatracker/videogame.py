class VideoGame:
    def __init__(self, _id, rank, name, platform, year, genre, publisher, naSales, euSales, jpSales, otherSales, globalSales):
        self._id = _id
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.naSales = naSales
        self.euSales = euSales
        self.jpSales = jpSales
        self.otherSales = otherSales
        self.globalSales = globalSales

        @staticmethod
        def video_game_decoder(obj):
            return VideoGame(obj['_id'], obj['rank'], obj['name'], obj['platform'], obj['year'], obj['genre'], obj['publisher'], obj['naSales'], obj['euSales'], obj['jpSales'], obj['otherSales'], obj['globalSales'])
