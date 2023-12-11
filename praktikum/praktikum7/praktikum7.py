def pemanggil(x1,x2,x3):
    return str(x1)+"/"+str(x2)+"/"+str(x3)
def backPropagation(y1,y2,y3):
    x1,x2,x3=pemanggil(10,12,29).split("/")
    eror1=int(x1)-y1
    eror2=int(x2)-y2
    eror3=int(x3)-y3
    return str(eror1)+"/"+str(eror2)+"/"+str(eror3)
def main():
    print(backPropagation(1,5,3))
    p1,p2,p3=backPropagation(1,2,3).split("/")
    print("error 1="+p1+"\nerror 2="+p2+"\nerror 3="+p3)
main()