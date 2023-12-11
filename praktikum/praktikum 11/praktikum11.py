list=[]
count=0
while True:
    pilihan=eval(input("""
        menu pilihan:
        -------------
        1.Ayam Geprek
        2.Ayam Penyet
        3.Nasi Goreng
        4.Nasi Briyani
        5.Jus Alpukat
        6.Jus Jeruk
        0.Keluar
    """))
    if(pilihan==1):
        list.append("Ayam Geprek")
    elif(pilihan==2):
        list.append("Ayam Penyet")
    elif(pilihan==3):
        list.append("Nasi Goreng")
    elif(pilihan==4):
        list.append("Nasi Briyani")
    elif(pilihan==5):
        list.append("Jus Alpukat")
    elif(pilihan==6):
        list.append("Jus Jeruk")
    elif(pilihan==0):
        break
    jawaban=input("Menu yang anda pilih adalah {} Apakah anda mau memilih pesanan lagi (Y/N):\n".format(list[count]))
    count+=1
    if jawaban[0] == 'N'or jawaban[0]=='n':
        break
hitung=1
print('\npesanan anda')
for i in list:
    print(str(hitung)+'.'+i)
    hitung+=1
print('Terimakasih atas pesanannya')