class IndexList:
    _index = {}

    def __getitem__(self, pow):
        if (pow in self._index.keys()):
            return self._index[pow]
        else:
            return 0

    def __setitem__(self, pow, val):
        self._index[pow] = val

class Polynomial(IndexList):
    _pow = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

    def __init__(self, *args, reverse=False):
        if reverse:
            args = list(reversed(args))

        for i, e in enumerate(args):
            self._index[len(args) - i - 1] = e
    
    def __repr__(self) -> str:
        s = ""

        for i in self._index.keys():
            p = ""

            for j in str(i):
                p += self._pow[int(i)]

            s += f"{self._index[i]}x{p} + "

        return s[0:-3]

a = Polynomial(5, 3, 5, 1)

print(a)