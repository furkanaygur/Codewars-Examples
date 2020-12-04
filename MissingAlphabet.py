'''

In this Kata you have to create a function,named insertMissingLetters,that takes in a string and outputs the same string processed in a particular way.

The function should insert only after the first occurrence of each character of the input string, all the alphabet letters that:

-are NOT in the original string
-come after the letter of the string you are processing

Each added letter should be in uppercase, the letters of the original string will always be in lowercase.

Example:

input: "holly"

missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"

output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"

You don't need to validate input, the input string will always contain a certain amount of lowercase letters (min 1 / max 50).
'''

def insert_missing_letters(st):
    result,temp = '', []
    for i in st:
        result += i
        if i in temp : continue
        a = ord(i)- ord(i.upper())
        for j in range(1,ord('z')-ord(i)+1):
            if chr(ord(i.upper())+j+32) in st: continue
            result += chr(ord(i.upper())+j)
        temp.append(i)
    return result        


print(insert_missing_letters('xixax'))