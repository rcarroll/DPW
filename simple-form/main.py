
import webapp2

from page import HTMLPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p= HTMLPage()
        if self.request.GET:
            fn=self.request.GET['first']
            ln=self.request.GET['last']
            cls= self.request.GET['class']
            hmo= self.request.GET['home']

            self.response.write(p.main (fn, ln, cls, hmo))
        else:
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
