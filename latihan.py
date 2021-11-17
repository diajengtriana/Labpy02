a = int(input("Masukkan Nilai a : "))
b = int(input("Masukkan Nilai b : "))
c = int(input("Masukkan Nilai c : "))

print("a = ", a)
print("b = ", b)
print("c = ", c)

if a > b and a > c:
    maks = a
    print("Bilangan terbesar adalah a = ", maks)
elif b > a and b > c:
    maks = b
    print("Bilangan terbesar adalah b = ", maks)
else:
    maks = c
    print("Bilangan terbesar adalah c = ", maks)