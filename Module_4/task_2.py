with open("output.txt","a") as f:
    l1=input("Enter text to write to the file: ")
    f.write(l1+"\n")
    print("Data sucessfully written to output.txt\n")
    l2=input("Enter additional text to append: ")
    f.write(l2+"\n")
    print("Data sucessfully appended\n")
    print("Final content of output.txt")

with open("output.txt","r") as f:    
    r=f.read()
    print(r)