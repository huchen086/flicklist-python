import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movielist = ["Star Wars", "Forrest Gump", "The Godfather",
        "The Shawshank Redemption", "Pupl Fiction", "The Matrix", "Fight Club",
        "The Wizard of Oz", "E.T."]

        # TODO: randomly choose one of the movies, and return it
        n = random.randint(0,len(movielist)-1)

        return movielist[n]

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        movie2 = self.getRandomMovie()
        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + movie2 + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
