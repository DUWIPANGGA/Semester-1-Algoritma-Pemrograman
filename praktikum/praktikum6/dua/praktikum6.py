# variable path digunakan untuk menyimpan path file output.txt
path="E:\KULIAH\pemrograman\praktikum\praktikum6\dua\output.txt"
#fungsi input user digunakan untuk menginput data diri
def input_user():
    nama=input("masukan nama : ")
    usia=eval(input("masukan usia : "))
    anak=eval(input("masukan jumlah anak : "))
    alamat=input("masukan alamat tinggal : ")
    return [nama,usia,anak,alamat]
# fungsi main() adalah fungsi utama 
def main(paths):
    # variable data digunakan untuk menampung data diri
    data= input_user()
    # variable all digunakan untuk menampung string sebelum di save ke file
    all= ("ahlan wa sahlan {}\nusia kamu adalah {} tahun \njumlah anak kamu adalah {}\nalamat tinggal kamu adalah {}".format(data[0],data[1],data[2],data[3]))
    # dibawah merupakan code untuk write string ke file output.txt
    file=open(paths,"a")
    file.write(all)
    # print ke console
    print("output:")
    print(all)
# eksekusi main program
main(path)