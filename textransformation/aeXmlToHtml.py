from lxml import etree

xml= etree.parse("desktop/ae_XMLTEI .xml")
xslt= etree.parse("desktop/ae_transf.xsl")
transform= etree.XSLT(xslt)

html= transform(xml)

with open("desktop/out.html", "w") as f:
    f.write(str(html))




    