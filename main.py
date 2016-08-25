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
        error = self.request.get("error1")
        email1 = self.request.get("email1")
        username = self.request.get("username")
        name_form="""
        <form action="/signup" method="post">
            <table class="error">
            <tbody>
            <tr><td>
            <label for="username">Username:</label></td>
                <td><input name="name" type="text" value=""" + username + """></td><td class="error1">""" + error + """</td>
                </tr><tr>
            <td><label for="password">Password:</label></td>
                <td><input name="password" type="password"></td><td class="error1">""" + error + """</td>
                </tr><tr>
            <td><label for="verify">Verify Password:</label></td>
                <td><input name="verify" type="password"></td><td class="error1">""" + error + """</td>
                </tr><tr>
            <td><label for="email">Email (optional):</label></td>
                <td><input name="email" type="text" value=""" + email1 + """></td><td class="error1">""" + error + """</td>
                </tr><tr>
                <td><input type="submit"></td>
                </tr>
                </tbody>
                </table>
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
            error1 = "Please enter a Username."
            error_escaped = cgi.escape(error1, quote=True)
            self.redirect("/?error=" + error_escaped)
        elif password1 != verify1:
            error2 = "Your passwords don't match."
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=password")
        elif not re.match("^[a-zA-Z0-9_-]{3,20}$", username):
            error3 = "Please use a valid Username."
            error_escaped = cgi.escape(error3, quote=True)
            self.redirect("/?error")
        elif not re.match("^.{3,20}$", password1):
            error4 = "Please enter a valid password."
            error_escaped = cgi.escape(error4, quote=True)
            self.redirect("/?error=password")
        elif not re.match("^[\S]+@[\S]+.[\S]+$", email1):
            error5 = "Please enter a valid email"
            error_escaped = cgi.escape(error5, quote=True)
            self.redirect("/?error=email")

        greatjob = "Signup successful"
        response = page_header + greatjob + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup)
], debug=True)
