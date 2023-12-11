data=[25,2,6,50,16,100,99,75,80,1]
print(data)
user=eval(input('masukan nilai yang ingin anda cari : '))
for i in data:
    if i==user:
        print(data.index(i))