pin=123456
def gantiPin(pin):
    pinlama=int(input("masukan pin lama"))
    if pinlama==pin:
        data=int(input("masukan pin baru : "))
        pin=data
        return pin
        print(data)
    else:
        print("maaf pinn yang anda masukan salah")
while(True):
    pin=gantiPin(pin)
    