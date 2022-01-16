import xml.etree.ElementTree as ET
import sys, getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","offset="])
    except getopt.GetoptError:
        print ('adjusttiming.py -i <inputfile> -o <offset>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('adjusttiming.py -i <inputfile> -o <offset>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--offset"):
            offset = arg
            offset = int(offset)
    mytree = ET.parse(inputfile)
    myroot = mytree.getroot()
    for effects in myroot.iter('Effect'):
        starttime = effects.get('starttime')
        endtime = effects.get('endtime')
        newstarttime = str(int(starttime)+offset)
        newendtime = str(int(endtime)+offset)
        effects.set('starttime',newstarttime)
        effects.set('endtime',newendtime)
    outfile = inputfile.split('.')[0]
    mytree.write(outfile+'-modified.xtiming')

if __name__ == "__main__":
    main(sys.argv[1:])