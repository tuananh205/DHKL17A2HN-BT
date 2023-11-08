def tim_so_lon_nhat(a, b, c):
    max_so = a
    if b > max_so:
        max_so = b
    if c > max_so:
        max_so = c
    return max_so
a = int(input("số thứ nhất: "))
b = int(input("số thứ hai: "))
c = int(input("số thứ ba: "))
so_lon_nhat = tim_so_lon_nhat(a, b, c)
print("Số lớn nhất trong ba số là:", so_lon_nhat)