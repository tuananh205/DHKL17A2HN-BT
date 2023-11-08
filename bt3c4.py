def hien_tat_ca_so_chia_het(m, n):
    if m >= n:
        return
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
hien_tat_ca_so_chia_het(m, n)