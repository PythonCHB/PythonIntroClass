# genhtml.py  Python class example.

# Generate xml (actually a small subset of html) like the following example:
# <html><head><title>PythonClass - Revision 1087:</title></head>
# <body>
#  <h2>PythonClass - Revision 1087:</h2>
#  <ul>
#   <li><a href="../">..</a></li>
#   <li><a href="branches/">branches/</a></li>
#   <li><a href="tags/">tags/</a></li>
#   <li><a href="trunk/">trunk/</a></li>
#  </ul>
# </body></html>

class Element(object):
    tag = "" # even though it never should be empty!!
    mid_new_line = ""
    body_indent = ""
    def __init__(self, txt):
        self.txt = txt
    def render(self, file_out, ind = ""):
        file_out.write(ind)
        file_out.write("<%s>%s"%(self.tag, self.mid_new_line))
        file_out.write(ind + self.body_indent)
        file_out.write(self.txt)
        file_out.write(self.mid_new_line + ind)
        file_out.write("</%s>\n"%self.tag)


class Head(object):
    tag = "head"
    def __init__(self):
        self.kids = []
    def append(self, element):
        self.kids.append(element)
    def render(self, file_out, ind = ""):
        file_out.write(ind)
        file_out.write("<%s>\n"%self.tag)
        for kid in self.kids:
            kid.render(file_out, ind + "    ")
        file_out.write(ind)
        file_out.write("</%s>\n"%self.tag)

class Title(Element):
    tag = "title"

class P(Element):
    tag = "p"
    mid_new_line = "\n"
    body_indent = "    "

if __name__ == "__main__":
    import sys
    h = Head()
    h.append(Title("PythonClass = Revision 1087:"))
    h.append(P(";sdlf ;sdjf a;siof ja;soifja;soif a;osfdj aso;fdi jao;sfd kioih"))
    h.render(sys.stdout)

