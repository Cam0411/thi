#cau 6
#th1 
#de cho san list
list = [2,3,2,2]
vitri6a = int(input("nhap vi tri bai 6a: "))
#pop() la ham se xoa vi tri tu cho 
#pop(vitri) dung 
#pop(vitri,giatri) sai 
#pop() no khac insert chi xoa chu ko them phan tu
list.pop(vitri6a)
print("list da xoa", list)


#th2 
#de nhu cau 1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list:  ",list)
vitri6a = int(input("nhap vi tri bai 6a: "))
#pop() la ham se xoa vi tri tu cho 
#pop(vitri) dung 
#pop(vitri,giatri) sai 
#pop() no khac insert chi xoa chu ko them phan tu
list.pop(vitri6a)
print("list da xoa", list)