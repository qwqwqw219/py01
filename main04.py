
a = int(input('Ввести с клавиатуры натуральное число :'))
def printBin( n ):
    k = 128
    print ( str(n) + "  :  ", end = "" )
    while k > 0:
        print ( n // k, 
                end = "" )
        n = n % k
        k = k // 2
printBin ( a )
