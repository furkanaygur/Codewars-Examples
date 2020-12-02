class ArrayStack:
 
  def __init__(self): self._data = []                       

  def __len__(self): return len(self._data)

  def is_empty(self): return len(self._data) == 0

  def push(self, e): self._data.append(e)                  

  def top(self):
    if self.is_empty(): return False
    return self._data[-1]        

  def pop(self):
    if self.is_empty(): return False
    return self._data.pop()   

  def printStack(self): print(self._data)

  def reverse_file(self,filename):
    S = ArrayStack()

    original = open(filename,'r')       
    for line in original: S.push(line.rstrip('\n'))     
    original.close()

    output = open(filename, 'w')   
    while not S.is_empty(): output.write(S.pop() + '\n')  
    output.close()