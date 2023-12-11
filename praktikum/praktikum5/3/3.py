# mendeklarasikan path file
path="D:/KULIAH/pemrograman/Praktikum/praktikum5/3/infile.txt"
# membuka file berdasarkan path
file=open(path,"r")
# membaca data dari file
data=file.read()
# print hasil baca ke console
print(data)