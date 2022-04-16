#2
#th1 neu de cho san list 
list = [2,3,4,5]
#sorted() la ham sap xe trat tu.
print("gia tri tu lon den be:  ",sorted(list, reverse=True))
list.sort()
print("gia tri tu be den lon:  ",list)

#th2 neu de yeu cau nhu de 1 
giatri = int(input("tao danh sach list: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list:  ",list)
print("gia tri tu lon den be:  ",sorted(list, reverse=True))
list.sort()
print("gia tri tu be den lon:  ",list)
