import media
import fresh_tomatoes

#Create instance toy_story of class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcRKk8fPFSi83NmjO4hlth9VpXsqigxNXrG10hXum8ljJ_fZ07c1",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")

#Create instance avatar of class Movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


#Create an array movies with all Movie instances
movies = [toy_story, avatar]

#Pass movies array to method open_movies_page of package fresh_tomatoes to create webpage that display all the movies 
fresh_tomatoes.open_movies_page(movies)
