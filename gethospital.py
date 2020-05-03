def gethospital():
    import csv
    h_info=list(csv.DictReader(open('Hospital_General_Information.csv','r'),delimiter=','))
    statename=input("What state are currently residing?")
    samestate=[s for s in h_info if s['State']==statename]
    return samestate

def printHosList(hs):
    print('Here is a list of hospitals in your state of residence.')
    for h in hs:
        print(h['Facility Name'],'in',h['Address']+','+h['City']+','+h['State']+','+h['ZIP Code'])

printHosList(gethospital())
