#cau 5 
#th1 de cho san list
list = [2,3,2,2,1]
vitri = int(input("nhap vi tri bai 5b:  "))
themphantu = int(input("them phan tu vao list:  "))
#insert() la ham them phan tu vao vi tri muon tron 
#insert(vitri,giatri)
list.insert(vitri,themphantu)
print("them vi tri tu chon:  ",list)

#th2 de nhu bai1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list:  ",list)
vitri = int(input("nhap vi tri bai 5b:  "))
themphantu = int(input("them phan tu vao list:  "))
list.insert(vitri,themphantu)
print("them vi tri tu chon:  ",list)
