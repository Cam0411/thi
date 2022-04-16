#3 
#th1 cho san list
list =  [2,3,12,3,2]
demphantu = int(input("dem gia tri bai 3:  "))
#count dem phan tu trong list
ketqua3 = list.count(demphantu)
print("so lan xuat hien so",demphantu,"can tim la: ",  ketqua3)

#th2 neu de yeu cau nhu de 1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list: ",list)
demphantu = int(input("dem gia tri bai 3:  "))
ketqua3 = list.count(demphantu)
print("so lan xuat hien so",demphantu,"can tim la: ",  ketqua3)


