#cau 6 
#th1
#neu de cho san list
list = [2,3,2,12]
phantu6b = int(input("nhap phan tu bai 6b: "))
#kiem phan tu co trong list ko 
if phantu6b in list: 
    #neu co thi xoa phan tu trc khi nhap
    #remove() xoa phan tu trong list.
    #remove(phan tu)
    #remove(phan tu) khac voi pop(vi tri)
    list.remove(phantu6b)
    print(list)
else:
    #neu ko thi bao ko co phan tu
    print("ko co phan tu")
#th2 
#neu de nhu bai 1
giatri = int(input("nhap gia tri: "))
list = [int(i) for i in str(giatri)]
print("thanh phan trong list:  ",list)
phantu6b = int(input("nhap phan tu bai 6b: "))
#kiem phan tu co trong list ko 
if phantu6b in list: 
    #neu co thi xoa phan tu trc khi nhap
    #remove() xoa phan tu trong list.
    #remove(phan tu)
    #remove(phan tu) khac voi pop(vi tri)
    list.remove(phantu6b)
    print(list)
else:
    #neu ko thi bao ko co phan tu
    print("ko co phan tu")