import webapp2
import re
import cgi

page_header="""
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        table.error tbody .error1 {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer="""
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        name_form="""
        <form action="/signup" method="post">
            <table>
            <tbody>
            <tr><td>
            <label for="username">Username:</label></td>
                <td><input name="name" type="text"></td>
                </tr><tr>
            <td><label for="password">Password:</label></td>
                <td><input name="password" type="password"></td>
                </tr><tr>
            <td><label for="verify">Verify Password:</label></td>
                <td><input name="verify" type="password"></td>
                </tr><tr>
            <td><label for="email">Email (optional):</label></td>
                <td><input name="email" type="text"></td>
                </tr><tr>
                <td><input type="submit"></td>
                </tr></tbody></table>
        </form>
        """
        self.response.write(page_header + name_form + page_footer)

class Signup(webapp2.RequestHandler):
    def post(self):
        username= self.request.get("name")
        password1= self.request.get("password")
        verify1= self.request.get("verify")
        email1= self.request.get("email")
        if username == "":
            error1= "Please enter a username."
        else:
            error1 = ""
        if password1 != verify1:
            error2= "Passwords do not match."
        else:
             error2 = ""
        if not re.match("^[a-zA-Z0-9_-]{3,20}$", username):
            error3= "Please enter a valid username."
        else:
             error3 = ""
        if not re.match("^.{3,20}$", password1):
            error4= "Please enter a valid password."
        else:
            error4 = ""
        if not re.match("^[\S]+@[\S]+.[\S]+$", email1):
            error5= "Please enter a valid email."
        else:
            error5=""

        name_form_response="""
        <form action="/signup" method="post">
            <table class="error">
            <tbody>
            <tr><td>
            <label for="username">Username:</label></td>
                <td><input name="name" type="text" value=""" + username + """></td><td class="error1">""" + error1 + """</td>
                </tr><tr>
            <td><label for="password">Password:</label></td>
                <td><input name="password" type="password"></td><td class="error1">""" + error2 + error4 + """</td>
                </tr><tr>
            <td><label for="verify">Verify Password:</label></td>
                <td><input name="verify" type="password"></td><td class="error1">""" + error4 + """</td>
                </tr><tr>
            <td><label for="email">Email (optional):</label></td>
                <td><input name="email" type="text" value=""" + email1 + """></td><td class="error1">""" + error5 + """</td>
                </tr><tr>
                <td><input type="submit"></td>
                </tr>
                </tbody>
                </table>
        </form>
        """

        welcome = "Welcome """ + username + ""

        if error1 != "":
            self.response.write(page_header + name_form_response + page_footer)
        elif error2 != "":
            self.response.write(page_header + name_form_response + page_footer)
        elif error3 != "":
            self.response.write(page_header + name_form_response + page_footer)
        elif error4 != "":
            self.response.write(page_header + name_form_response + page_footer)
        elif error5 != "":
            self.response.write(page_header + name_form_response + page_footer)
        else:
            self.response.write(page_header + welcome + page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup),
], debug=True)
