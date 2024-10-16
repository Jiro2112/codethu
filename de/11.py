def sinh_xau_nhi_phan(n):
 
  if n == 0:
    return ['']
  else:
    xau_nhi_phan = []
    for xau in sinh_xau_nhi_phan(n - 1):
      xau_nhi_phan.append(xau + '0')
      xau_nhi_phan.append(xau + '1')
    return xau_nhi_phan


n = int(input("Nhập độ dài xâu nhị phân: "))


xau_nhi_phan = sinh_xau_nhi_phan(n)
print("Tất cả các xâu nhị phân có độ dài", n, "là:")
for xau in xau_nhi_phan:
  print(xau)