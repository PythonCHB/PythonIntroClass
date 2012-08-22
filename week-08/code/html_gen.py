"""
Python class example.

Set of classes to build HTML

This version adds a decorator to create a <p> element around any function
that returns a string

"""

class Element(object):
    """
    An element with optional attributes and multiple items in the content
    """
    tag = ""
    indent = "    "
    def __init__(self, content=None, **attributes):
        """
        initialize an element with optional attributes, and any number of sub-elements and content

        :param content: content of the element:  single string or another element.
                        an empty string will be ignored
        :param [attributes]: optional attributes as keyword parameters.

        example:
        """
        if not content:
            self.children = []
        else:
            self.children = [content]

        self.attributes = attributes

    def append(self, element):
        self.children.append(element)

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(">")
        for child in self.children:
            try:
                child.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("\n")
                file_out.write(ind + self.indent)
                file_out.write(str(child))
        file_out.write("\n")
        file_out.write(ind)
        file_out.write('</%s>'%self.tag)

class Html(Element):
    tag = "html"

    ## override the render method to add the "<!DOCTYPE html>"
    def render(self, file_out, ind = ""):
        file_out.write("<!DOCTYPE html>")
        # call the superclass render:
        Element.render(self, file_out, ind)

class Head(Element):
    tag = "head"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Ul(Element):
    """
    element for an unordered list
    """
    tag = "ul"

class Li(Element):
    """
    element for the item in a list
    """
    tag = "li"

class SelfClosingTag(Element):
    """
    Element with a single tag -- no content, only attributes
    """
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, ind = ""):
        """
        an html rendering method for self-closing elements:
        attributes, but no content a no closing tag
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(" />")

class Meta(SelfClosingTag):
    tag = "meta"

class Hr(SelfClosingTag):
    tag = "hr"

class OneLineTag(Element):

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(">")
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(str(child))
        file_out.write('</%s>'%self.tag)

class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    """
    element for a link ( <a> tag )
    """
    tag = "a"
    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)

class H(OneLineTag):
    """
    class for header tags, the level is specified in a parameter

    """
    def __init__(self, level, content, **attributes):
        OneLineTag.__init__(self, content, **attributes)

        self.tag = "h%i"%level


######
## making a decorator

#def make_a_paragraph(func, *args, **kwargs):
def make_a_paragraph(func):
    """
    decorator example -- wrap anything that creates a string in a <P> tag
    """
    print "in make_a_paragraph"
    def wrapper(*args, **kwargs):
        """
        make_a_paragraph decorator
        
        Takes any function that returns a string, and wraps it in a P element
        class for rendering an html paragraph
        """
        func.__doc__ = "a doctring"
        print "in wrapper", kwargs
        return P( func(*args), **kwargs )
    return wrapper

@make_a_paragraph
def simple_string():
    """
    An example function that returns a hard-coded string
    """
    return "this is a really simple string"

@make_a_paragraph
def simple_string_from_numbers(limit):
    """
    An example function that prints some text from a bunch of numbers
    """
    msg = []
    for i in range(limit):
        msg.append('the next number is: %i ...'%i)
    return " ".join(msg)

@make_a_paragraph
def random_sentence(num_words):
    """
    An example function that generates random nonsence words
    """
    import random
    import string
    msg = []
    for i in xrange(num_words):
        length = random.randint(1,10)
        word = "".join(random.sample(string.lowercase, length))
        msg.append(word)
    msg[0] = msg[0].capitalize()
    msg[-1] = msg[-1] + "."
    return " ".join(msg)


if __name__ == "__main__":
    import sys, cStringIO
#    page = Html()
#
#    head = Head()
#    head.append( Meta(charset="UTF-8") )
#    head.append(Title("PythonClass = Revision 1087:"))
#
#    page.append(head)
#
#    body = Body()
#
#    body.append(  H(2, "PythonClass - Class 6 example") )
#
#    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
#                  style="text-align: center; font-style: oblique;"))
#
#    body.append(Hr())
#
#    list = Ul(id="TheList", style="line-height:200%")
#    list.append( Li("The first item in a list") )
#    list.append( Li("This is the second item", style="color: red") )
#    item = Li()
#    item.append("And this is a ")
#    item.append( A("http://google.com", "link") )
#    item.append("to google")
#    list.append(item)
#    body.append(list)
#
#    page.append(body)
#
#    f = cStringIO.StringIO()
#
#    page.render(f)
#
#    f.reset()
#    print f.read()
#
#    f.reset()
#    open("test_html.html", 'w').write(f.read())

# Test the @make_a_paragraph decorator

    import sys

    p = P("some text")
    p.render(sys.stdout)

    el = simple_string(font="large")
    el.render(sys.stdout)
    
    el = simple_string_from_numbers(3)
    el.render(sys.stdout)
    
    el = random_sentence(10)
    el.render(sys.stdout)