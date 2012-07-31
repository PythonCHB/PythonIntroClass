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

class Title(object):
    tag = "title"
    def __init__(self, txt):
        self.txt = txt
    def render(self, file_out, ind = ""):
        file_out.write(ind)
        file_out.write("<%s>"%self.tag)
        file_out.write(self.txt)
        file_out.write("</%s>\n"%self.tag)

if __name__ == "__main__":
    import sys  
    t = Title("PythonClass = Revision 1087:")
    t.render(sys.stdout)
