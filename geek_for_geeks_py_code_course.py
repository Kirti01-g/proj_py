# value print using while loop 
# this code print the value from 0 to 10 using while loop
i = 0
while i <= 10:
    print(i)
    i += 1
# end of code


# ex: iteration by for loop on string
# this code print the s string character 1 at each line
s="hello world"

for i in s:
    print(i)
# end of code


# ex: iteration by for loop on list
# this code print the list value 1 at each line
# l is the list variable
l=[10,20,30,40,50]
for i in l:
    print(i)
# end of code


# ex: how to print the length of the function
a="hello world"
print(len(a))
# len() function is used to print the length of the string
# end of code


# ex: how to print the length of the list
l=[10,20,30,40,50]
print(len(l))
# len() function is used to print the length of the list
# end of code


# ex: how to print the length of the tuple
t=(10,20,30,40,50)
print(len(t))
# len() function is used to print the length of the tuple
# end of code


# ex: how to print the length of the dictionary
d={"a":10,"b":20,"c":30}
print(len(d))
# len() function is used to print the length of the dictionary
# end of code


# count()
a="hello  is world"
print(a.count("is",0,len(a)))
# count() function is used to count the number of occurrences of a substring in a string
# end of code


# center(), just() and ljust()
str = "geekforgeeks"
print(str.center(20, '-'))
print(str.ljust(20, '-'))
print(str.rjust(20, '-'))
print(str.center(20, '*'))
print(str.ljust(20, '#'))
print(str.rjust(20, '$'))
# end of code



# isalpha(), isalnum() and isspace()
str1="abc"
str2="abc123"
str3="   "
print("For string 1: isalpha():", str1.isalpha())
print("For string 1: isalnum():", str1.isalnum())
print("For string 1: isalpace():", str1.isspace())
print()
print("For string 2: isalpha():", str2.isalpha())
print("For string 2: isalnum():", str2.isalnum())
print("For string 2: isalpace():", str2.isspace())
print()
print("For string 3: isalpha():", str3.isalpha())
print("For string 3: isalnum():", str3.isalnum())
print("For string 3: isalpace():", str3.isspace())
print()
# end of code



# join()
s="-"
l=["geek","for","geeks"]
print(s.join(l))
# join() function is used to join the elements of a list into a string
# end of code



# find() and rfind()
s="this is a test string for is test"
print("the first occurrence of 'is' is at:")
print(s.find("is",0,len(s)))
print("the last occurrence of 'is' is at:")
print(s.rfind("is",0,len(s)))
# find() function is used to find the first occurrence of a substring in a string
# rfind() function is used to find the last occurrence of a substring in a string
# end of code



# strip(), lstrip() and rstrip()
s="   hello world   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# strip() function is used to remove the leading and trailing spaces from a string
# lstrip() function is used to remove the leading spaces from a string
# rstrip() function is used to remove the trailing spaces from a string
# end of code



# strtswitch() and endswitch()

A="geekforgeeks"
B="geek"

if (A.startswith(B)):
    print("String A starts with String B")
else:
    print("String A does not start with String B")
if (A.endswith(B)):
    print("String A ends with String B")
else:
    print("String A does not end with String B")

# end of code



#upper() and lower() titals() swapcase()
a="Hello World"
print(a.upper())
print(a.lower())
print(a.title())
print(a.swapcase())
# end of code



# large number
a = 100000000000
a =a+1
b = a*3
c = b-7
d = b-c-a
print(a,b,c,d)
# end of code



# type of variable
a = 10
b = 10.5
c = "hello"
print(type(a))
print(type(b))
print(type(c))
# end of code


# multiple assignment
print(100**100)
print(100*100)
# here * use to multiply the value
# while ** use to power the value
# end of code


# string calculation
a = "hello"
b = "world"
print(a+b)
# here + use to concatenate the string
a = "hello"
b = "world"
print(a+' '+b)
# end of code


# string(), lstrip(), rstrip()
str = '----geeksforgeeks----'

# using string () to delete all
print("string after stripping all'-' is :  ")
print(str.strip('-'))

# using lstrip() to delete leading '-'
print("string after striping all leading '_' is :  ")
print(str.lstrip('-'))

# using rstrip() to delete trailing '-'
print("string after striping all trailing '_' is :  ")
print(str.rstrip('-'))

# end of code



# min() and max()
str = "geeksforgeeks"

# using min() to find minimum character
print("minimum character is : " + min(str));

# using max() to find maximum character
print("maximum character is : " + max(str));

# end of code



# maketrans() and translate()
str_ = "geeksforgeeks"
str1 = "gfo"
str2 = "abc"

# using maktrans() to map elements of str2 with str1
mapping = str_.maketrans(str1, str2);
# using translate() to replace the characters
print("The string after mapping is : ");
print(str_)
print("The string before mapping is : ");
print (str_.translate(mapping));
# end of code



# replace()

str = "geeksforgeeks is best for geeks"
str1 = "geeks"
str2 = "students"
# using replace() to replace 'geeks' with 'students'
print("The string after replacing 'geeks' with 'students' is : ");
print(str.replace(str1, str2, 2));
# end of code



# len(), min() and max() 
l = [10, 20, 5, 40, 15]
# using len() to find length of list
print("length of list is : " ,len(l))
# using min() to find minimum value in list
print("minimum value in list is : " ,min(l))
# using max() to find maximum value in list
print("maximum value in list is : " ,max(l))
# end of code



#"+,*,-,/,//,%,**"
l1 =[1,2,3,4,5]
l2 =[6,7,8,9,10]
l3 =[11,12]
l4 =l1 + l2 + l3
print(l4)
print(l4*4)
# end of code



#index() and count()
l = [1, 2, 3, 4, 5]
# using index() to find index of 3
print("index of 3 is : " ,l.index(3,1,4))
print("the no of occurrences of 2 is :", l.count(2))
# end of code



# del(list[a:b]) and remove()
l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,3,4,5,6,7,8,9,10]
print("list l1 intitially",l1)
del (l1[1:6])          # this function will not desplay the value between 1 to 7
# when del(l1[1:6]) was use then the value contain in last like it contain 6
# will deleate from the fun list
print("list l1 after using del function",l1)
print("list l2 initially",l2)
l2.pop(3)              #this function will not desplay the value .pop(3) contain 
# if it contain pop(1) then it did not print the 2nd value because it count 0,1,2,3...
print("list l2 after using pop function",l2)
# end of the code



# insert(i,x) ,remove(x)
l = [1,2,3,4,5,]
l.insert(3,2)
print("list after inserting 2",l)
l.remove(4)
print("list after removing first occurrence of 4",l)
# end of code



#sort() reverse()
l=[1,4,2,3,7,6,3,4,100,67]
l.sort()
print("list after sorting becomes",l)
l.reverse()
print("list after reversing becomes",l)
# end of code


#extend(<list>)
#clear

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)              # this fun connect l1 with l2
print("list 1 after extending with list 2", l1)
l2.clear()                 # this fun clear l2
print("list 2 after using clear function", l2)
# end of code 


# while(expression):
# stement(s)
count = 0
while (count < 4 ):  # here the value of count define how many time to print the value in print
    print("hello guyes this is a python code")       # this is the value
    count = count + 1
# end of the code 



#for interator var in sequence:
#statement
l = [" this","is","a","python","code"]
for i in l:
    print(i)
# end of the code 


# nested for loop for iterator_var in seq:
# for iteration_var in seq:
# statement
# nested while loop while expression:
# while expresion: statement(s)
# statement(s)
l = ["this","is","geek"]
for word in l:
    for character in word:
        print(character)
# this statement prints each carecter in line 
#ex: t
# h
# i
# ...


# loop control statement
# it also print values the same way but diid not print the value spaciefie
l = "domainhost"
for letter in l:
    if(letter == 'e' or letter == 's'):   # these are the spaciefie values
        continue;
    else:
        print(letter)


# break state,ment
l = "domain"
for letter in l:
    if(letter == 'o' or letter == 'i'):   # these are the spaciefie values
        break;
    else:
        print(letter)
# end of the code 

# past statement
# use to write the empety loops
l = "geeksforgeeks"
for letter in l:
    pass;
print("last letter: ",letter )


#logical operastors

str1 = ""
str2 = "funtime"
str3 = "fun"
print("str1: ",str1)
print("str2: ",str2)
print("str3: ",str3)

print("str1 and str2: ",str1 and str2)
print("str1 or str2: ",str1 or str2)
print("str2 and str1: ",str2 and str1)
print("str2 or str1: ",str2 or str1)
print("str2 and str3: ",str2 and str3)
print("str2 or str3: ",str2 or str3)
print("str3 and str2: ",str3 and str2)
print("str3 or str2: ",str3 or str2)


