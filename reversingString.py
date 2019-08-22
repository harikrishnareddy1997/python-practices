'''
#1
def reverse_for_loop(s):
    rs = ''
    for c in s:
        rs = c + rs
    return rs

s=str(input("Enter String\n"))
print("reverse string:",reverse_for_loop(s))

#2
def reverse_slicing(s):
    return print("reversed strng:",s[::-1])
s=str(input(" "))
reverse_slicing(s)
ha
'''

s='Hari'
print(s[4:-5:-1])

