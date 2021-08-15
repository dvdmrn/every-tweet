import functools

maxChars = 280 # 250 chars is max tweet length
nChars = len("abcdefghijklmnopqrstuvwxyz 0123456789!,?.$'~+&*():/#")
print(nChars)
charMap = {"a":0,
           "b":1,
           "c":2,
           "d":3,
           "e":4,
           "f":5,
           "g":6,
           "h":7,
           "i":8,
           "j":9,
           "k":10,
           "l":11,
           "m":12,
           "n":13,
           "o":14,
           "p":15,
           "q":16,
           "r":17,
           "s":18,
           "t":19,
           "u":20,
           "v":21,
           "w":22,
           "x":23,
           "y":24,
           "z":25,
           " ":26,
           "0":27,
           "1":28,
           "2":29,
           "3":30,
           "4":31,
           "5":32,
           "6":33,
           "7":34,
           "8":35,
           "9":36,
           "!":37,
           ",":38,
           "?":39,
           ".":40,
           "$":41,
           "'":42,
           "~":43,
           "+":44,
           "&":45,
           "*":46,
           "(":47,
           ")":48,
           ":":49,
           "/":50,
           "#":51,
           "\"":52
           }

def allSeqLes(N):
    '''
        gets number of sequences < i
    '''
    acc = 0
    for i in range(1,N):
        print(f"{nChars}^{i}={nChars**i}")
        acc += nChars**i
    return(acc)

def allSeqWithin(sequence):
    '''
        sequence := String
    '''
    N = len(sequence)
    acc = 0
    for i in range(1,N+1):
        print(f"character: {sequence[i-1]}, map: {charMap[sequence[i-1]]}, {nChars}^{N-i}; val: {charMap[sequence[i-1]]*(nChars**(N-i))}")
        acc += charMap[sequence[i-1]]*(nChars**(N-i))
    return (1+acc)

def complexity(sequence):
    # sequence := String
    print(f"------\nevaluating: {sequence}")
    withinComplexity = allSeqWithin(sequence)
    lessThanComplexity = allSeqLes(len(sequence))
    print(f"complexity so far of sum 52^{len(sequence)-1}: {lessThanComplexity}")
    print(f"complexity of intersequence: {withinComplexity}")
    return withinComplexity+lessThanComplexity

def timeScale(hrs):
    days = hrs/24
    years = days/365
    return (hrs, days, years)

print(complexity("am i?") - complexity("jf"))
print(timeScale(complexity("am i?") - complexity("jf")))
