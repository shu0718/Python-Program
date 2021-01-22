vowels=['a','i','o','e','u']
word=input("enter your name")
found=[]
for i in word:
    if i in vowels:
        if i not in found:
            found.append(i)
for vowels in found:
    print(vowels)
        
