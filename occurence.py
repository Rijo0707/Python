#Program to find the number of occurrence of letters in a string
def most_frequent(str1):
    l=len(str1)
    for i in range(0,l):
        cnt=0
        for j in range(0,l):
            if str1[i]==str1[j]:
                cnt+=1
        occ[str1[i]]=str(cnt)
    print(sorted(occ.items(), key=lambda x: x[1], reverse=True))
occ={}
str_name=input("Please enter a String: ")
most_frequent(str_name)

