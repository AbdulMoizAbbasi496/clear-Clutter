f=open("C:/Users/Lenovo/Desktop/VS Files/Python/python projects for beginners/toRead.txt" , "r")
c=[]
for i in f:
    print(i)
    c.extend(i.split())
   
# d=0
# for i in range(len(c)):
#     d+=1
# print(d)

print("Total number of words in your file are : ",len(c))
