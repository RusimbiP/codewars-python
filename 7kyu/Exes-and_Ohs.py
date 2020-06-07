# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

##################### Solution ##########################################################

def xo(s):
    Xs = []
    Os = []
    string = s.lower()
    
    for char in string:
        if char == 'x':
            Xs.append(char)
        if char == 'o':
            Os.append(char)
            
    if len(Xs) == len(Os):
        return True
    else:
        return False