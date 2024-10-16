def dem():
    cau = input("Nhập một câu gồm các chữ thường: ")
    tu = cau.split()
    ki_tu = len(cau)
    print(f"Số từ trong câu là: {len(tu)}")
    print(f"Số ký tự trong câu là: {ki_tu}")

if __name__ == "__main__":
    
    dem()