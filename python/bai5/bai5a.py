#5a
#th1 neu de cho san
list = [2,3,1,2,3]
themphantu = int(input("nhap gia tri bai 5a:  "))
#them append() se them phan tu vao cuoi list 
list.append(themphantu)
print("them gia tri cuoi list:  ", list)

#th2 neu cho nhu de 1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print(list)
list.append(themphantu)
print("thanh phan trong list:  ", list)