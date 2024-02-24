print("ВВедите координаты точки P(X0,Y0)")
x,y=int(input()),int(input())
if 1<=(x-1)**2+y**2<=4:
    a=1
if abs(x-4)<2 and abs(y-2)<3:
    c=1
if a==1 and c==1:
    print("yes,yes")
elif a<1 and c==1:
    print("no,yes")
elif a<1 and c<1:
    print("no,no")

