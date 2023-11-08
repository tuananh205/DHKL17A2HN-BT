N=int(input("nhập một số tự nhiên N:"))
if N<1:
   print("số bạn đã nhập không phải số tự nhiên")
else:
   print("các số nguyên từ 1 đến", N, "là:")
   for i in range(1, N+1):
      print(i)