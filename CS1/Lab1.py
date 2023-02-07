import argparse
parser=argparse.ArgumentParser(description = "Calculate Area and Volume of a room")
parser.add_argument("-l",type=int, help= "Length of room")
parser.add_argument("-w",type=int, help= "Width of room")
parser.add_argument("-e",type=int, help= "Elevation of room")
args=parser.parse_args()
def find_area(l,w):
    if w is None:
        return "None"
    if l is None:
        return "None"
    else:
        Area = l * w
        return Area

def find_volume(l,w,e):
    if e is None :
        return "None"
    else:
        Volume = l * w * e
        return Volume
if __name__ == "__main__":
    print ('('+(str(find_area(args.l,args.w))) + "," + " " + str((find_volume(args.l,args.w,args.e)))+')')
