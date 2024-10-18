def binhphuong(n):
    if n<0:
        return "So nhap phai >= 0"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*n
n=int(input())
print(binhphuong(n))