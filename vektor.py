class vektor:
    def __init__(self,d):
        self._coords = [0] * d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self,j):
        return self._coords[j]
    def __seitem__(self, j, val):
        self._coords[j] = val
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = vektor(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self,other):
        return self._coords == other._coords
    def __ne__(self,other):
        return not self == other
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"

# inputan

a = vektor(5)
b = vektor(5)
c = vektor(5)
d = vektor(0)

print("a dimension : ",len(a))
print("b dimension : ",len(b))

a[2] = 3
b[3] = 2

c = a + b

print ("c : ", c)