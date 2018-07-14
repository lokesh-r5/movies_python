import webbrowser

#Create a class Movie
class Movie():
    #To create an instance that takes movie title, storyline, poster image and trailer link 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Method to open youtube trailer in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
