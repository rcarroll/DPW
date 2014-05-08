
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
        '''
        self.page_content='''
        <form method="GET" action="">
            <input type="text" name="first" placeholder="First Name:"></input>
            <input type="text" name="last" placeholder="Last Name:"></input>
            <input type="submit" name="submit" value="go" placeholder="Last Name:"></input>
        </form>
        '''
        self.page_close= '''
    </body>
</html>
'''

    def print_out(self ,content):
        return self.page_open + self.page_content + content + self.page_close