import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictitonary = xmltodict.parse(filestring)
        return  xmldictitonary

voorbeeldendict = processXML('artikelen.xml')
voorbeelden = voorbeeldendict['artikelen']['artikel']
for voorbeeld in voorbeelden:
    if voorbeeld['naam'] is not None:
        print(voorbeeld['naam'])