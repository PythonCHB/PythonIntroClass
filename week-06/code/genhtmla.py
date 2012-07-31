"""
genhtmla.py  Python class example.

This module holds a simple class for writing a <title> element in html

"""



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
