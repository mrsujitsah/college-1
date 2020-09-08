#string opration
str1=input("enter the string ")
print("the string is ",str1)

list1=str1.split(" ")
print("list is",list1 )

maxLen = -1
for word in list1:
    if len(word) >= maxLen:
        maxLen = len(word)
        result = word
# printing result
print("Maximum length string is : " + result)

