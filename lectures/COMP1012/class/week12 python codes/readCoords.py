#readCoords

from time import ctime
def getCoords(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    coords = []
    for line in lines:
        points = line.strip().split() # remove \n
        for point in points:
            point = point[1:-1] # remove ( )
            coord = point.split(',')
            n = (float(coord[0]),float(coord[1]))
            coords.append(n)
        print(coords)
    return coords

def displayCoords(coords):
    print('   X\t   Y')
    for x, y in coords:
        print ('%6.2f\t%6.1f' % (x, y))
    
def main():
    print ('----------------------------------\n')
    displayCoords(getCoords('coords1.txt'))
    print("""
Programmed by Stew Dent.
Date: %s
End of processing.""" % ctime())

main()

