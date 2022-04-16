#4
#th1 cho san list
list =  [2,3,12,3,2]
#index se kiem tra vi tri trong list nhung no chi tra ket qua dau tien
nhapgiatri = int(input("Nhap gia tri bai 4: "))
ketqua4 = list.index(nhapgiatri)
print("phan tu thuoc vi tri:  ",ketqua4)

#th2 neu de yeu cau nhu de 1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list:",list)
nhapgiatri = int(input("Nhap gia tri bai 4: "))
ketqua4 = list.index(nhapgiatri)
print("phan tu thuoc vi tri:  ",ketqua4)