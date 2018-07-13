import webapp2
import os
import jinja2
import cgi

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Base(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainPage(Base):
    def get(self):
        self.render("hw6-1.html")

class ResultPage(Base):
    def get(self):
        self.render("hw6-2.html")
        text1 = cgi.escape(self.request.get("text1"))
        text2 = cgi.escape(self.request.get("text2"))
        result = ""
        text1_split = list(text1)
        text2_split = list(text2)
        index1 = min(len(text1_split) , len(text2_split))
        index2 = max(len(text1_split) , len(text2_split))
        index = 0
        while index < index1:
            result += text1_split[index]
            result += text2_split[index]
            index += 1
        if index1 == index2:
            pass
        else:
            if len(text1_split) > len(text2_split):
                result += text1_split[index]
                index += 1
            else:
                result += text2_split[index]
                index += 1
        self.response.out.write(result)  

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/output",ResultPage)
], debug=True)
