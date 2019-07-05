class ArgumentError(Exception):
    def __init__(self, text):
        self.txt = text



def flag():
    x = ''
    while x != 'stop':
        print('to exit write "stop"\n')
        n = None
        while n == None:
            try:
                x = input('enter an integer even number: ')
                if x == 'stop':
                   return 'good luck!' 
                if float(x) < 0 or not float(x) % 2 == 0:
                    raise ArgumentError('this number is not valid\n')
                else:
                    n = int(x)
            
            except ValueError:
                print('this is not a number!')
            except ArgumentError as ar:
                print(ar)
        r = int(n/2)
        hor_dist = n
        vert_dist = int(n/2)
        border = '#'*(n*3)+'##\n'
        flag = ''
        
        v = vert_dist*('#'+' '*(n*3)+'#\n')
        flag+= border + v
        for i in range(r):
            
            flag += '#' + ' '*hor_dist + ' '*(r-i-1) + '*' + "o"*(i*2) + '*' + ' '*(r-i-1)+ ' '*hor_dist + '#\n'
        for i in range(r-1,-1,-1):
            flag += '#' + ' '*hor_dist + ' '*(r-i-1) + '*' + "o"*(i*2) + '*' + ' '*(r-i-1) + ' '*hor_dist + '#\n'
        flag+= v + border
        
        print (flag)
