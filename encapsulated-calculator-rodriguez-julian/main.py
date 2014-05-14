##Julian Rodriguez

##May 12, Monday



import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        ## character data
        bodark = Point()
        bodark.NAME= "Bodark Bjorn"
        bodark.STR = 15
        bodark.DEX = 7
        bodark.CHR = 8
        bodark.INT = 3
        bodark.CON = 10

        ## Total Data and print function
        bodark.total = bodark.STR + bodark.DEX + bodark.INT
        bodark.update()
        self.response.write(bodark.print_info())

        nock = Point()
        nock.NAME= "Nock Fletching"
        nock.STR = 7
        nock.DEX = 15
        nock.CHR = 12
        nock.INT = 6
        nock.CON = 3

        nock.total = nock.STR + nock.DEX + nock.INT
        nock.update()
        self.response.write(nock.print_info())

        magnar = Point()
        magnar.NAME= "Magnar Magnil"
        magnar.STR = 15
        magnar.DEX = 15
        magnar.CHR = 3
        magnar.INT = 5
        magnar.CON = 6

        lina = Point()
        lina.NAME= "Lina Medina"
        lina.STR = 5
        lina.DEX = 5
        lina.CHR = 3
        lina.INT = 15
        lina.CON = 15
        # print lina.print_out()


class Point(object):  ###constructer
    def __init__(self):
                self.__NAME = ""
                self.__STR = 0
                self.__DEX = 0
                self.__CHR = 0
                self.__INT = 0
                self.__CON = 0
                self.total = 0

                ##HTML Template
                self.__open = '''

        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
            </head>
        <body>

            <div class="wrap">
        '''
                self.__content = '''
                <div>

                    <h1>{self.NAME}</h1>
                    <hr>

                    <h4>Strength</h4>
                    <p>{self.STR}</p>

                    <h4>Strength</h4>
                    <p>{self.DEX}</p>

                    <h4>Charisma</h4>
                    <p>{self.CHR}</p>

                    <h4>Intelligence</h4>
                    <p>{self.INT}</p>

                    <h4>Constitution</h4>
                    <p>{self.CON}</p>

                    <h4>Total Level</h4>
                    <p>{self.total}</p>



                </div>

                '''

                self.__close = '''
            </div>
        </body>
        </html>
        '''

    # def totalPoints(self):
    #     self.__all = self.__STR + self.__DEX + self.__CHR + self.__INT + self.__CON

                self.__all = self.__open + str(self.__content) + self.__close

    def print_info(self):
        return self.__all

    @property   ##getter
    def totalVal(self):
        return self.__all

    @totalVal.setter  ##setter
    def totalVal(self, newTotal):
            self.__all = str(newTotal)
            # self.update()

    def update(self):
        self.__all = self.__all.format(**locals())


    # def print_out(self):
    #     return self.__STR







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
