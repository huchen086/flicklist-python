import webapp2

header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def get(self):
        form = """
            <h3>Edit My Watchlist</h3>
            <form action="/add" method="post">
                <lable>I would like to add
                <input type="text" name="new-movie"/>
                to my watchlist.
                </lable>
                <input type="submit" value="Add it!"/>
            </form>
		"""

        self.response.write(header + form + footer)

class AddMovie(webapp2.RequestHandler):

    def get(self):
        self.response.write("Shouldn't taken a left turn at ALberqueque.")

    def post(self):
        moviename = self.request.get("new-movie")
        successmsg = "<strong>" + moviename + "</strong> has been posted to your list."

        self.response.write(header + successmsg + footer)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie)
], debug=True)
