one = int(input("Enter a number: "))
two = int(input("Enter a second number: "))

def gcdandlcm(a):
    n = len(a)
    gcd = euc(a[0], a[1])
    lcm = a[0]*a[1]/gcd
    #print(lcm)
    for i in range( 2, n ):
        gcd = euc( gcd, a[i])
        gcdlcm = euc(lcm, a[i])
        #print gcdlcm
        lcm = lcm*a[i]/gcdlcm
        #print lcm
    return gcd, lcm


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if greater % a == 0 and greater % b == 0:
            break
        else:
            greater += 1
    return greater


def euc(a, b):
    if b > a:
        return euc(b,a)
    if a % b == 0:
        return b
    return euc(b, a%b)

print( "\nGreatest Common Divisor of "+str(one) + " & "+ str(two)+ " = " + str(euc(one,two)) )
print( "Least Common Multiple of "+str(one) + " & "+ str(two)+ " = " + str(lcm(one,two)) + "\n")

array = [9720,4158,594,612]
def test(arr):
    for i in range(len(arr)):
        a = arr[i]
        for j in range(len(arr)):
            b = arr[j]
            if a == b:
                break
            print( "Greatest Common Divisor of "+str(a) + " & "+ str(b)+ " = " + str(euc(a,b)) )
            print( "Least Common Multiple of "+str(a) + " & "+ str(b)+ " = " + str(lcm(a,b)) + "\n")

print( "The GCD and LCM of the array "+ str(array) +" is ")
answer = gcdandlcm(array)
print ( "GCD: " + str(answer[0]) )
print ( "LCM: " + str(answer[1]) )