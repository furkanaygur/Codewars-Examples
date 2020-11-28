'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

'''

def namelist(names):
    result = ''
    a = ', '
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 0:
        return ''
    for i in range(len(names)):
        if i == len(names)-1:
            result = result + '& ' +str(names[i]['name'])
            return result
        if i == len(names) -2:
            a = ' '
        result = result + str(names[i]['name'])+a
    


print(namelist([]))