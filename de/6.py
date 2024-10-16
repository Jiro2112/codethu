 n = int(input())
    
   
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        soDaoNguoc = 0
        
        while n > 0:
            chuSoCuoi = n % 10
            soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
            n = n // 10
        print(soDaoNguoc)