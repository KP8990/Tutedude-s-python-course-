try:
    with open("sample.txt","r") as f:
        line=f.readline()
        i=1
        while(line !=""):
            print(f"line{i}:",line,end="")
            line=f.readline()
            i+=1
        # line_1=f.read()
        # print(line_1)
except FileNotFoundError:
    print("Error: The file'sample.txt' was not found")