saldo=1000000
pin=123456
pinBaru=""
loop=True
# fungsi tanya digunakan untuk menanyakan aksi selanjutnya
def tanya():
    a=input("ingin melanjutkan transaksi lagi? \na.ya\nb.tidak\n")
    if a=="a":
        return True
    elif a=="b":
        print("terimakasih")
        return False
# fungsi cekSaldo digunakan untuk mengecek saldo
def cekSaldo():
    print("saldo anda adalah",saldo)
#fungsi pengambilUang digunakan untuk mengambil nilai saldo
def pengambilUang(saldo):
    ambil=int(input("masukan jumlah saldo yang ingin diambil : "))
    if ambil<saldo:
        saldo=saldo-ambil
        print("saldo anda sekarang ",saldo)
    else:
        print("Saldo tidak mencukupi")
    return saldo
# fungsi ganti pin digunakan untuk mengganti pin
def gantiPin(pin):
    pinlama=int(input("masukan PIN lama : "))
    if pinlama==pin:
        data=int(input("masukan PIN baru : "))
        cekpin=int(input("Masukan pin baru lagi : "))
        if data==cekpin:
            pin=data
            print("Ganti PIN berhasil")
            return pin
        else:
            print("maaf pin tidak sama")
            return pinlama
    else:
        print("PIN anda salah")
# fungsi login digunakan untuk mengecek pin
def login():
    pinSekarang=int(input("masukan pin anda "))
    return pinSekarang

while(loop==True):
    pinSekarang=login()
    if pinSekarang!=pin:
        print("pin yang anda masukan salah silahkan coba lagi!")
    elif pinSekarang==pin:
        pilihan=input("silahkan pilih menu dibawah \na.cek saldo\nb.Pengambilan uang\nc.ganti pin\n\n>> ")
        if pilihan=="a":
            cekSaldo()
        elif pilihan=="b":
            saldo=pengambilUang(saldo)
        elif pilihan=="c":
            pin=gantiPin(pin)
        else:
            print("maaf saya tidak mengerti")
    loop=tanya()