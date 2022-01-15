import xml.etree.ElementTree as ET

mytree = ET.parse('Toy-Sack.xtiming')
myroot = mytree.getroot()
for effects in myroot.iter('Effect'):
    starttime = effects.get('starttime')
    endtime = effects.get('endtime')
    newstarttime = str(int(starttime)+500)
    newendtime = str(int(endtime)+500)
    effects.set('starttime',newstarttime)
    effects.set('endtime',newendtime)
  


mytree.write('Toy-Sack-modified.xtiming')