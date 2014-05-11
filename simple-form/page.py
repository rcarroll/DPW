
class HTMLPage(object):
    def __init__(self):
        self.page_open='''
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my page</title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>

        <div>
            <img src="img/pIcon-01.png">
        </div>
        '''
        self.page_content='''
        <form method="GET" action="">
            <input type="text" name="first" placeholder="First Name:">
            <input type="text" name="last" placeholder="Last Name:">

  			<input type="radio" name="class" value="Warrior">Warrior
  			<input type="radio" name="class" value="Paladin">Paladin

            <select id="list" name="home">
                <option value="Mirra">Mirra</option>
                <option value="Framm">Framm</option>
                <option value="Forossa">Forossa</option>
                <option value="Aldia">Aldia</option>
            </select>

            <input type="submit" name="submit" value="go" placeholder="Last Name:">
        </form>
        '''
        self.page_close= '''
    </body>
</html>
'''

    def print_out(self):
        return self.page_open + self.page_content + self.page_close

    def main(self, VAR1, VAR2, VAR3, VAR4):
        self.open='''
        <div>
        '''

        self.full_name_open='''<h1>'''
        self.content1= VAR1+" "+VAR2
        self.full_name_close='''</h1>'''

        self.class_name_open='''<h1>'''
        self.content2= VAR3
        self.class_name_close=''' </h1>'''

        self.home_name_open='''<h1>'''
        self.content3= VAR4
        self.home_name_close=''' </h1>'''

        self.close='''
        </div>
        '''
        return self.open + self.full_name_open + self.content1+ self.full_name_close \
               + self.class_name_open + self.content2 + self.class_name_close \
               + self.home_name_open + self.content3 + self.home_name_close + self.close