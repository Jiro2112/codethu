a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

flaot =denta = b*b-4*a*c

if  a==0:
  x=-b/a
  print(x)
elif denta>0:
  x1=-b-sqrt(denta)/2*a
  x2=-b+sqrt(denta)/2*a
  print("phuong trinh co 2 nghiem =",x1,x2)
elif denta=0:
  x3=-b/2*a
  print("phuong trinh co 1  nghiem ",x3)
else :
  print("vo nghiem ")
 



