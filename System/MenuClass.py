from Entity.MatrixClass import Matrix
from Entity.DataBaseClass import DataBase


class Menu:
    @staticmethod
    def mainMenu():
        print("1: Create matrix")
        print("2: Delete matrix")
        print("3: Show existing records")
        print("4: Calculate matrices")
        print("5.Exit")
        print()

    @staticmethod
    def calculateMenu():
        print("1: Compare matrices")
        print("2: Sum up matrices")
        print("3: Subtract first matrix from second")
        print("4: Transpose matrices")
        print("5: Multiply matrices")
        print("6: Multiply matrix on number")
        print("7: Back to main menu")
        print()

    def __new__(cls):
        while True:
            cls.mainMenu()
            chose = int(input("Make a choice "))
            if chose == 1:
                cls.createMatrix()
            if chose == 2:
                cls.deleteMatrix()
            if chose == 3:
                cls.printMatrices()
            if chose == 4:
                while True:
                    cls.calculateMenu()
                    chose = int(input("Make a choice "))
                    if chose == 1:
                        cls.compareMatrix()
                    if chose == 2:
                        cls.sumMatrices()
                    if chose == 3:
                        cls.subMatrices()
                    if chose == 4:
                        cls.transposeMatrix()
                    if chose == 5:
                        cls.multiplyMatrices()
                    if chose == 6:
                        cls.multiplyMatrixNumber()
                    if chose == 7:
                        break
            if chose == 5:
                break

    @staticmethod
    def createMatrix():
        db = DataBase()
        MatrixName = input("Matrix name: ")
        RowNo = input("Enter rows quantity: ")
        ColNo = input("Enter cols quantity: ")
        CellValue = input("Enter values: ")
        db.createMatrix(MatrixName, RowNo, ColNo, CellValue)

    @staticmethod
    def deleteMatrix():
        db = DataBase()
        matrixName = input("Print matrix name for deleting matrix: ")
        db.deleteMatrix(matrixName)

    @staticmethod
    def printMatrices():
        db = DataBase()
        db.printMatrix()

    @staticmethod
    def compareMatrix():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        matrixName = input("Select matrix: ")
        M2 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        if M1 == M2:
            print("Matrix are equal")
            print()
        else:
            print("Matrix aren't equal")
            print()

    @staticmethod
    def sumMatrices():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        matrixName = input("Select matrix: ")
        M2 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        M3 = M1 + M2
        M3.printMatrix()

    @staticmethod
    def subMatrices():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        matrixName = input("Select matrix: ")
        M2 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        M3 = M1 - M2
        M3.printMatrix()

    @staticmethod
    def multiplyMatrices():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        matrixName = input("Select matrix: ")
        M2 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        M3 = M1 * M2
        M3.printMatrix()

    @staticmethod
    def transposeMatrix():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        M1.transposeMatrix()

    @staticmethod
    def multiplyMatrixNumber():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        number = int(input("Enter a number: "))
        M3 = M1 * number
        M3.printMatrix()

