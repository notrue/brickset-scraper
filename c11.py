import lxml.html
html = lxml.html.parse("x11.html")
nodes = html.xpath("//div[@class='c3']/text()")
print(nodes)