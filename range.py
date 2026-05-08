class range :
    def __init__(self, start, stop=None, step = 1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start,stop = 0, start
        self._length = max(0,(stop - start + step - 1)//step)
        self._start = start
        self._step = step
    def __len__(self):
        return self._length
    def __getitem__(self,k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError ('index out of page')
        return self._start + k * self._step

r = range(8,140,5)
print('length of r: ',len(r))
print('sixteenth element of r =', r[15])

for i in r:
    print(i, end=' ')
print()

for i in range(0,27):
    print(r[i], end=' ')
print()

for i in range(8,140, 5):
    print(i, end=' ')
print()