class HTML:
    def __init__(self):
        self.source = ""

    def addElement(self, tag, content="", elClass="", elId="", additional=""):
        self.source += '<' + tag + ' class="' + elClass + '" id="' + elId + '"' + additional + ">" + content + "</" + tag + ">\n"

class md:
    def __init__(self):
        self.source = "" 

    def addElement(self, tag, content="", href=""):
        if tag[0] == "h": 
            sup = "#" * int(tag[1])
            self.source += sup + " " + content + "\n"
        elif tag == "a": 
            self.source += "[" + content + "][" + href + "]\n"
        elif tag == "code":
            self.source += "```\n" + content + "\n```"
        else:
            self.source += tag + " " + content + "\n"

htmlKod = HTML() 
htmlKod.addElement('p', 'matej', 'e', 'i', 'onclick="matej()"')
htmlKod.addElement('h1', 'test')
print(htmlKod.source)
mdKod = md()
mdKod.addElement("h5", "matej")
mdKod.addElement("a", "google", "https://google.com")
mdKod.addElement("code", 'printf("Hi world")')
print(mdKod.source)
