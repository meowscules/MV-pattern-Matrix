from Entity.MatrixException import *


class Matrix:
    def __init__(self, read_matrix_rows, read_matrix_cols, read_matrix_value=None):
        self.rows = read_matrix_rows
        self.cols = read_matrix_cols
        if read_matrix_value:
            self.body = [read_matrix_value[i:i + read_matrix_cols]
                         for i in range(0, len(read_matrix_value), read_matrix_rows)]
        else:
            self.body = []
            for i in range(self.rows):
                self.body.append([0] * self.cols)

    def validationFunction(self, other):
        if self == other and isinstance(self, Matrix) and isinstance(other, Matrix):
            return True
        else:
            return False

    def __eq__(self, other):
        return len(self.body) == len(other.body) and len(self.body[0]) == len(other.body[0])

    def __add__(self, other):
        if self.validationFunction(other):
            matrixAdd = Matrix(self.rows, self.cols)
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixAdd.body[i][j] = self.body[i][j] + other.body[i][j]
            return matrixAdd
        else:
            raise MatrixError

    def __sub__(self, other):
        if self.validationFunction(other):
            matrixSub = Matrix(self.rows, self.cols)
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixSub.body[i][j] = self.body[i][j] - other.body[i][j]
            return matrixSub
        else:
            raise MatrixError

    def __mul__(self, other):
        try:
            if isinstance(other, int):
                matrixMul = Matrix(self.rows, self.cols)
                for i in range(len(self.body)):
                    for j in range(len(self.body[0])):
                        matrixMul.body[i][j] = other * self.body[i][j]
                return matrixMul
            elif isinstance(other, Matrix):
                tmp = []
                matrixMul = Matrix(self.rows, self.cols)
                matrixMul.body = []
                for i in range(len(self.body)):
                    for j in range(len(other.body[0])):
                        sums = 0
                        for k in range(len(other.body)):
                            sums = sums + (self.body[i][k] * other.body[k][j])
                        tmp.append(sums)
                    matrixMul.body.append(tmp)
                    tmp = []
                return matrixMul
        except MatrixError:
            return

    def transposeMatrix(self):
        try:
            tmp = [[0] * len(x) for x in self.body]
            for i in range(len(self.body)):
                for j in range(len(self.body[0])):
                    tmp[i][j] = self.body[j][i]
            return tmp
        except MatrixError:
            return

    def printMatrix(self):
        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                print(self.body[i][j], end=' ')
            print()
        print()
