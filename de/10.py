def cong_hai_so(a, b):
    a = a[::-1]
    b = b[::-1]

    if len(a) < len(b):
        a += '0' * (len(b) - len(a))
    elif len(b) < len(a):
        b += '0' * (len(a) - len(b))

    tong = []
    du = 0

    for i in range(len(a)):
        tong_chu_so = int(a[i]) + int(b[i]) + du
        du = tong_chu_so // 10
        tong.append(str(tong_chu_so % 10))

    if du:
        tong.append(str(du))

    return ''.join(tong[::-1])


a = input("Nhap so tu nhien a: ")
b = input("Nhap so tu nhien b: ")

tong = cong_hai_so(a, b)
print("Tong cua", a, "va", b, "la:", tong)