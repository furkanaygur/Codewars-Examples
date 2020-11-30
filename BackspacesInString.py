'''
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

'''

def clean_string(s):
    result = []
    for i in s:
        if i == '#' and result != []:
            result.pop()
        else:
            if i == '#': continue
            result += i
    return ''.join(result)
        
print(clean_string('#*Ee#+J1K##'))