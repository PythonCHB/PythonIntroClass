"""
genhtmlg.py  Python class example.

This module does some more consolidating...

"""

class Element(object):
    tag = "html"
    indent = "  "

class JustTextElement(Element):
    """
    base class for an html element with only text -- no children
    
    """
    def __init__(self, txt):
        self.txt = txt
    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that put the tags on different lines
        """
        file_out.write(ind)
        file_out.write("<%s>\n"%self.tag )
        file_out.write(ind + self.indent)
        file_out.write(self.txt)
        file_out.write("\n" + ind)
        file_out.write("</%s>\n"%self.tag)
 
class SameLineElement(JustTextElement):
    """
    Base class for an element with just text that puts the tags on the same
    line as the text
    """
    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that put the tags on same line
        """
        file_out.write(ind)
        file_out.write("<%s>"%self.tag)
        file_out.write(self.txt)
        file_out.write("</%s>\n"%self.tag)
 
class JustKidsElement(Element):
    """
    Base class for elements that only hold kids -- no raw text
    """
    def __init__(self):
        self.kids = []

    def append(self, element):
        self.kids.append(element)
    
    def render(self, file_out, ind = ""):
        """
        renders an html tag with kids to the file-like object.
        
        :param file_out: file-like object that is rendered to
        """
        file_out.write(ind)
        file_out.write("<%s>\n"%self.tag)
        for kid in self.kids:
            kid.render(file_out, ind + self.indent)
        file_out.write(ind)
        file_out.write("</%s>\n"%self.tag)
                 
class Html(JustKidsElement):
    """
    class for the main html element
    """
    tag = "html"

class Body(JustKidsElement):
    """
    class for the main body element
    """
    tag = "body"

class Head(JustKidsElement):
    """
    class for the html header data
    """
    tag = "head"

class Title(SameLineElement):
    tag = "title"

class P(JustTextElement):
    tag = "p"

if __name__ == "__main__":
    import sys
    page = Html()
    
    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))
    
    page.append(head)
    
    body = Body()
    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

    page.append(body)
    page.render(sys.stdout)

