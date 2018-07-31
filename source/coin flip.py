import sys, random
def flip(Invalid, TT):
    total = {'H':0, 'T':0}
    while Invalid:
        cnt = int(input("Enter the number of times you want to flip a coin\n"))
        if not cnt > 0:
            print("Invalid Input")
            cont = input("Y to try again N to exit")
            if cont.upper() == 'N':
                sys.exit("Bye!")
            elif cont.upper() == 'Y':
                continue
        else:
            Invalid = False
            for i in range(0,cnt):
                r = random.randint(0,1)
                output = TT[r]
                if output == 'H':
                    print('Head')
                    total['H'] = total['H']+1
                elif output == 'T':
                    print('Tail')                    
                    total['T'] = total['T']+1
        return total
if __name__ == '__main__':
    Invalid = True
    TT = {0:'H',1:'T'}
    res = flip(Invalid, TT)
    print("Total Head",res['H'],"\nTotal Tails",res['T'])