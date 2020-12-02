from stack import ArrayStack

# source.c => target.c made with stack data theory

stack = ArrayStack()

with open('source.c','r+', encoding='utf-8') as file:
    for i in file:
        if i[0] == '#':
            stack.reverse_file('source.c')
            break

with open('source.c','r+', encoding='utf-8') as file:
    for i in file:
        stack.push(i.rstrip('\n'))

data = ''
spaceCount = 0
space = ''

for i in range(0,len(stack._data)):
    temp = stack.pop()

    if (temp == '}'):
        spaceCount = spaceCount - 1
        space = '\t' * spaceCount
        
    data = data + space + temp + '\n'

    if (temp == '{'):
        spaceCount = spaceCount + 1
        space = '\t' * spaceCount
        
with open('target.c', 'w') as file:
    file.write(data)

stack.reverse_file('source.c')   
