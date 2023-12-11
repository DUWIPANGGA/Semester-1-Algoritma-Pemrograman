path="D:/KULIAH/pemrograman/praktikum/praktikum10/nilai.txt"
count=0
# membuka file berdasarkan path
file=open(path,"r")
# membaca data dari file
data=" "
nama=""
tambah=0
print("daftar rata rata nilai:")
for i in range(4):
    data=file.readline()
    nilai=data.split(",")
    for i in nilai:
        if len(i)>=4:
            nama=i
        else:
            tambah=tambah+int(i)
            count+=1
            # print(tambah)
    print(f"{nilai[0]} {tambah/count}")
    
    
