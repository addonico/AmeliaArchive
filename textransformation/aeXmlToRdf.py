import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

with open ("desktop/ae_XMLTEI .xml", "r") as file:
     xml_content= file.read()

root= ET.fromstring(xml_content)


# FOR THE NAMED ENTITIES
ns= set() #names' set
ds= set() #dates' set
dl=[]     
ol=[]     #organizations' list
nl=[]     #names' list

for name in root.findall(".//{http://www.tei-c.org/ns/1.0}name"):
    if name.attrib.get("type")== "org":
        ol.append(name.text)
    elif name.attrib.get("type")== "person":
            if "Miss" in name.text:
                 n=name.text
                 y=n.strip("Miss")
                 l=y.lstrip()
                 r=y.rstrip()
                 if l == "Earhart" or r== "Earhart":
                     pass
                 else:
                     ns.add(y) 
            else:
                 ns.add(name.text)


for x in ns:
      if type(x) == str:
           nl.append(x)




for date in root.findall(".//{http://www.tei-c.org/ns/1.0}date"):
      ds.add(date.text)
for x in ds:
      dl.append(x)




#FOR THE METADATA INFORMATION
mL=[]
oTitle="" #title of online article
title=""
publisher=""
for x in root.findall(".//{http://www.tei-c.org/ns/1.0}titleStmt/{http://www.tei-c.org/ns/1.0}title"):
     if not x.attrib.values():
          oTitle= x.text
          mL.append(oTitle)
     elif x.attrib.get("n")== "1":
          title=x.text
          mL.append(title)
     
for x in root.findall(".//{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}publisher"):
     if x.text:
          publisher= x.text



import hashlib
base= "http://example.org/"
ppuri={}
oouri={}
mLD={}
for p in nl:
   
    p_id= hashlib. md5(p.encode("UTF-8")).hexdigest()
    puri= base + p_id 
    ppuri[p]= puri

for o in ol:
     oid=hashlib. md5(o.encode("UTF-8")).hexdigest()
     ouri= base + oid
     oouri[o]= ouri

for m in mL:
     id= hashlib. md5(m.encode("UTF-8")).hexdigest()
     uri= base + id
     mLD[m]= uri



from rdflib import Graph, URIRef, Literal, Namespace 
from rdflib.namespace import OWL, FOAF, RDF, DC

DBO= Namespace("http://www.dbpedia.org/ontology/")
fabio=Namespace("http://purl.org/spar/fabio")

pdic= {}
pdic["Earhart"]= URIRef("https://viaf.org/viaf/59886046/")
pdic["Elder"]= URIRef("https://viaf.org/viaf/75751987/")
pdic["Putnam"]= URIRef("https://viaf.org/viaf/3304149/")
arturi=URIRef("http://addonico.github.io/AmeliaArchive/item/1929Interview")
on_article=URIRef("http://addonico.github.io/AmeliaArchive/item/1929Interview/html-article")
p_publisher= URIRef("http://addonico.github.io/AmeliaArchive/item/EveningStar")

g= Graph()
g.bind("dbo", DBO)
g.bind("fabio", fabio)

for x in ppuri.values():
     g.add((URIRef(x), RDF.type, FOAF.Person))

for x in ppuri.keys():
     g.add((URIRef(ppuri.get(x)), FOAF.name, Literal(x)))
     for z in pdic.keys():
          if z in x:
              g.add(((URIRef(ppuri.get(x))), OWL.sameAs, pdic.get(z)))

for x in oouri.values():
     g.add((URIRef(x), RDF.type, FOAF.Organization))

for x in oouri.keys():
     g.add((URIRef(oouri.get(x)), FOAF.name, Literal(x)))

for x in dl:
     if "2024" in x: 
           g.add((on_article, DC.date, Literal(x)))
     else:
          g.add((arturi, fabio.hasPublicationDate, Literal(x)))


g.add((arturi, fabio.hasPublisher, p_publisher))

for x in mLD.keys():
     if x == oTitle:
           g.add((on_article, FOAF.name, Literal(x)))

g.serialize("desktop/final_ae_output.ttl", format="turtle")

     



    

