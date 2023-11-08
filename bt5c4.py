def find_lcm(num1, num2):
    # ước chung lớn nhất
    max_num = max(num1, num2)
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1
    return lcm
# Nhập hai số từ bàn phím
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
# bội chung nhỏ nhất
lcm = find_lcm(num1, num2)
# In kết quả
print("Bội chung nhỏ nhất của", num1, "và", num2, "là", lcm)