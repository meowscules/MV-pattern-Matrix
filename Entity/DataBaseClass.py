import sqlite3
from collections import deque
from sqlite3 import DataError


class DataBase:
    global db
    global cur
    db = sqlite3.connect('matrix.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS matrices
                                     (MatrixName varchar(24) NOT NULL,
                                     RowNo smallint NOT NULL,
                                     ColNo smallint NOT NULL,
                                     CellValue varchar(50) NULL)
                                     """)
    db.commit()

    @staticmethod
    def createMatrix(MatrixName, RowNo, ColNo, CellValue):
        cur.execute("INSERT INTO matrices VALUES (?, ?, ?, ?)", (MatrixName, RowNo, ColNo, CellValue))
        db.commit()

    @staticmethod
    def deleteMatrix(matrixName):
        cur.execute("SELECT * FROM matrices")
        if cur.fetchone() is not None:
            cur.execute(f"DELETE FROM matrices WHERE MatrixName = '{matrixName}'")
            db.commit()
            print("Matrix deleted!")
            print()
        else:
            raise DataError

    @staticmethod
    def printMatrix():
        cur.execute("SELECT MatrixName FROM matrices")
        if cur.fetchone() is not None:
            for value in cur.execute("SELECT * FROM matrices"):
                print(value)
                print()
        else:
            raise DataError

    @staticmethod
    def readMatrixValues(matrixName):
        tmp = cur.execute(f'SELECT CellValue FROM matrices WHERE MatrixName= "{matrixName}"')
        body = []
        for string in tmp.fetchone():
            for value in range(len(string)):
                body.append(string[value])
        del body[1::2]
        for conversion in range(len(body)):
            body.append(int(body[conversion]))
        rows = cur.execute(f'SELECT RowNo FROM matrices WHERE MatrixName = "{matrixName}"')
        firstMultiplier = rows.fetchone()[0]
        cols = cur.execute(f'SELECT ColNo FROM matrices WHERE MatrixName = "{matrixName}"')
        secondMultiplier = cols.fetchone()[0]
        del body[0:firstMultiplier*secondMultiplier]
        return body

    @staticmethod
    def readMatrixRows(matrixName):
        value = cur.execute(f'SELECT RowNo FROM matrices WHERE MatrixName = "{matrixName}"')
        return value.fetchone()[0]

    @staticmethod
    def readMatrixCols(matrixName):
        value = cur.execute(f'SELECT ColNo FROM matrices WHERE MatrixName = "{matrixName}"')
        return value.fetchone()[0]
