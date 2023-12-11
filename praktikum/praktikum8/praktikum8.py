# mendeklarasikan String nilai_huruf sebagai empty string
nilai_huruf=""
# fungsi main() adalah program utama
def main():
    # input nilai dari user
    nilai=eval(input("masukan nilai anda : "))
    # perbandingan untuk menentukan grading nilai dakan huruf
    if(nilai>=80.1):
        nilai_huruf="A"
    elif(nilai>=75.1):
        nilai_huruf="AB"
    elif(nilai>=70.1):
        nilai_huruf="B"
    elif(nilai>=65.1):
        nilai_huruf="BC"
    elif(nilai>=60.1):
        nilai_huruf="C"
    elif(nilai>=55.1):
        nilai_huruf="CD"
    elif(nilai>=50.1):
        nilai_huruf="D"
    elif(nilai<50.1):
        nilai_huruf="E"
    # print ke console
    print("grading nilai anda adalah "+nilai_huruf)
# eksekusi program utama
main()