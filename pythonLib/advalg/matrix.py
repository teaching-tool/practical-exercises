#Probably not needed. Use numpy

class Matrix:
    def __init__(self, rows, cols):
        assert(rows >= 0 and cols >= 0)
        self._rows = rows
        self._cols = cols
        self._elem = [[0] * cols for i in range(rows)]

    def rows(self):
        return self._rows

    def columns(self):
        return self._cols

    def __getitem__(self, pos):
        row, col = pos
        assert(0 <= row < self.rows())
        assert(0 <= col < self.columns())
        return self._elem[row][col]

    def __setitem__(self, pos, value):
        row, col = pos
        assert(0 <= row < self.rows())
        assert(0 <= col < self.columns())
        self._elem[row][col] = value

    def __mul__(self, other):
        assert(self.columns() == other.rows())
        res = Matrix(self.rows(), other.columns())

        for r in range(res.rows()):
            for c in range(res.columns()):
                for k in range(self.columns()):
                    res[r,c] += self[r,k] * other[k,c]

        return res

    def __pow__(self, k):
        res = self
        for i in range(k-1):
            res *= self
        return res