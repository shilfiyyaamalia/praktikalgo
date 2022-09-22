print("program python menghitung luas ruangan ")
print(" hitunglah sebuah ruangan ini!")
#keterangan:
#P merupakan panjang ruangan
#L merupakan lebar ruangan

P = float(input("masukkan niai panjang : "))
L = float(input("masukkan nilai lebar :  "))
n = input("pilih satuan(meter/inci) = ")

if (n == 'meter') :
    l = P*L
elif (n == 'inci') :
    l = P*L*39.37
    
print(" jadi ruangan luas ruangan tersebut = ", l)
 
