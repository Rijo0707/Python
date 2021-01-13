#Program to print file extension of the file
fName= input("Input the filename: ")
fExt = fName.split(".")
if fExt[1]=="py":
    print("Extension of the file is : 'Python'")
elif fExt[1]=="java":
     print("Extension of the file is : 'Java'")
elif fExt[1]=="c":
     print("Extension of the file is : 'C'")
elif fExt[1]=="cpp":
     print("Extension of the file is : 'C++'")
elif fExt[1]=="js":
     print("Extension of the file is : 'Javascript'")
else:
    print("No Match Found!!!!")
    
    

