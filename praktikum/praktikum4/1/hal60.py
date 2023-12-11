def main():
 fname = input("Enter filename: ")
 infile = open(fname,'r')
 data = infile.read()
 print(data)
main()