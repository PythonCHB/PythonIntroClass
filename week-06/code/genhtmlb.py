"""
genhtmlb.py  Python class example.

This module adds a <head> element

"""


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
    h = Head()
    h.append(Title("PythonClass = Revision 1087:"))
    h.append(Title("PythonClass = Revision 1088:"))
    h.render(sys.stdout)

