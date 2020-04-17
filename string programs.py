'''
Q1)string="hello world"
 len(string)
'''
'''
Q2) Write a program to count the number of charaters(char ferq) in a string.
string="google.com"
s=set(string)      #give unique values
for i in s:
    a=string.count(i)
    print(i,a)
'''
''' 
#Q3)Write program to get a string made of the first 2 and last 2 char from given a string.
#If the string length is less than 2, return instead of the empty string.
s=input("enter a string: ")
if len(s)>=2:
    print(s[0]+s[1]+s[-2]+s[-1])
else:
    print("empty string")
'''
'''
#Q4)write a program to get a string from a given string where all occurence of its first char have been changed to '$',
#except the first char itself.
def rep_char(s):
    char= s[0]
    s=s.replace(char,'$')
    s=char + s[1:]
    return s
print(rep_char('navin'))
'''
'''
#Q5) write a program to get a string from two given strings,
#seperated by a space and swap the first two characters of each string
def swap(a,b):
    c=b[0:2]+a[2:]
    d=a[0:2]+b[2:]
    return c,d
print (swap(a="abc",b="xyz"))
'''
'''
#Q6)write a program to add 'ing' at the end of a given string(length should be at least 3).
#if the given string is already ends with 'ing' then add'ly'. if the given string is less than 3, leave it unchanged.
s=input("enter a string: ")
def add(s):
    if len(s)>=3:
        if s[-3:]=='ing':
            return s+'ly'
        else:
           return s+'ing'
    return s
print(add(s))
'''
'''
#Q8) write a python function that takes a list of words and returns the length of the longest one.
def longest_word(words_list):
    word_len=[]
    for i in words_list:
        word_len.append((len(i),i))
    word_len.sort()
    return word_len[-1][1]
print(longest_word(["mango","banana","watermelon"]))
'''
'''
#Q9)write a program to remove the nth index character from a nonempty string.
str=input("enter a string: ")
def remove_char(str,n):
    first_part=str[:n]
    last_part=str[n+1:]
    return first_part+last_part
'''
#Q10)write a program to change a given string to a new string where the first and last chars have been exchanged.
str=input("enter a string: ")
print(str[-1:]+str[1:-1]+str[:1])


 


