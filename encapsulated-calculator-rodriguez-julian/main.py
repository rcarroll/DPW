##Julian Rodriguez

##May 12, Monday



import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        bodark = Point()
        bodark.STR = 15
        bodark.DEX = 7
        bodark.CHR = 8
        bodark.INT = 3
        bodark.CON = 10
        bodark.total = bodark.STR + bodark.DEX + bodark.INT
        bodark.update()
        self.response.write(bodark.print_info())

        nock = Point()
        nock.STR = 7
        nock.DEX = 15
        nock.CHR = 12
        nock.INT = 6
        nock.CON = 3
        # print nock.print_out()

        magnar = Point()
        magnar.STR = 15
        magnar.DEX = 15
        magnar.CHR = 3
        magnar.INT = 5
        magnar.CON = 6
        # print magnar.print_out()

        lina = Point()
        lina.STR = 5
        print lina.STR
        lina.DEX = 5
        lina.CHR = 3
        lina.INT = 15
        lina.CON = 15
        # print lina.print_out()


class Point(object):
    def __init__(self):
                self.__STR = 0
                self.__DEX = 0
                # self.__CHR = 0
                self.__INT = 0
                # self.__CON = 0
                self.total = 0

                self.__open = '''

        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
            </head>
        <body>
        '''
                self.__content = '''<p>{self.total}</p>'''

                self.__close = '''
        </body>
        </html>
        '''

    # def totalPoints(self):
    #     self.__all = self.__STR + self.__DEX + self.__CHR + self.__INT + self.__CON
                self.__all = self.__open + str(self.__content) + self.__close

    def print_info(self):
        return self.__all

    @property
    def totalVal(self):
        return self.__all

    @totalVal.setter
    def strength(self, newTotal):
            self.__all = str(newTotal)
            # self.update()

    def update(self):
        self.__all = self.__all.format(**locals())
    # def print_out(self):
    #     return self.__STR







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
