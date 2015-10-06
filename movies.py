import fresh_tomatoes
#matched up class attributes with attribute names in included file
class Movies(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

l = []
l.append(Movies("Ghostbusters","http://ia.media-imdb.com/images/M/MV5BMTkxMjYyNzgwMl5BMl5BanBnXkFtZTgwMTE3MjYyMTE@._V1_SX214_AL_.jpg","https://youtu.be/vntAEVjPBzQ"))
l.append(Movies("Back to the Future","http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg","https://youtu.be/qvsgGtivCgs"))
l.append(Movies("Pulp Fiction","http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SX214_AL_.jpg","https://youtu.be/s7EdQ4FqbhY"))
l.append(Movies("The Silence of the Lambs","http://ia.media-imdb.com/images/M/MV5BMTQ2NzkzMDI4OF5BMl5BanBnXkFtZTcwMDA0NzE1NA@@._V1_SX214_AL_.jpg","https://youtu.be/lQKs169Sl0I"))
#Since comments were listed as required, I wanted to take a minute to wonder if my movie choices dated me before calling the function

fresh_tomatoes.open_movies_page(l)
