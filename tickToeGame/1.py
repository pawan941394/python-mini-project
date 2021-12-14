vowels= ['a','e','i','o','u']
name= (input("Enter name ")).lower()
getDict = {'a':0,
           'e':0,
           'i':0,
           'o':0
           ,'u':0,
           'Total vowels is ':0
           }
for i in name:
    if i in vowels:
        getDict[i]=+1
        getDict['Total vowels is ']=+1

for i in getDict:
    print(f"{i} = {getDict[i]}")
