p=int(input())
ir=float(input())
ir1=ir/100
nt=int(input())
noy=float(input())
def compound_intrest():
    A=p*(pow((1+ir1/nt),noy))
    return A
print(compound_intrest())


