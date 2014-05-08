
import webapp2

from page import HTMLPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p= HTMLPage()
        if self.request.GET:
            fn=self.request.GET['first']
            ln=self.request.GET['last']
            self.response.write(p.print_out(fn+' '+ln))
        else:
            self.response.write(p.print_out("All of your base are belong to us."))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
