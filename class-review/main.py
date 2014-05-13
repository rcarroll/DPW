
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        yoda = Character()
        yoda.name= "Yoda"
        yoda.age= -5
        yoda.gender= "Male"
        yoda.occ= "Jedi Master"
        yoda.print_info()
        yoda.squad_no= "Green 1"
        print yoda.squad_no


        luke = Character()
        luke.name= "Luke"
        luke.age= 24
        luke.gender= "Male"
        luke.occ= "Jedi Knight"
        luke.print_info()
        luke.squad_no= "Red 4"
        print luke.squad_no


        leia = Character()
        leia.name= "Leia"
        leia.age= 24
        leia.gender= "Female"
        leia.occ= "Princess"
        leia.print_info()
        leia.squad_no= "Pink 5"
        print leia.squad_no


class Character(object):
    def __init__(self):
                self.name=""
                self.__age= 0
                self.occ= ""
                self.gender= ""
                self.__rogue_squadron_no = "DEFAULT"

    def print_info(self):
        print self.name + " is a(n) " + self.occ

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):

        if new_age < 0 or new_age > 1000:
            print "ERROR"
        else:
            self.__age = new_age

    @property
    def squad_no(self):
        return self.__rogue_squadron_no

    @squad_no.setter
    def squad_no(self, new_no):

        if new_no == "Pink 5":
            new_no = "Red 1"

        self.__rogue_squadron_no = new_no

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
