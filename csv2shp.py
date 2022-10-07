import shapefile
import csv

# 读取文件的路径
readPath = r"Taxi_105 - trace.csv"

# 要写入新的文件存放路径
writeFilePath = r"CSVToShp.shp"

def readPointsCSV(readPath):
    with open(readPath) as myFile:
        myReader = csv.reader(myFile)
        i = 0
        for row in myReader:
            if i == 0:
                fields = row
                print(fields)
            if i>10:
                break
            # 此时输出的是一行行的列表
            # print(row)
            # print('+'.join(row))
            i=i+1
    return fields,myReader

'''CSV转ShapeFile'''
if __name__ == '__main__':
    print()

    # 写入文件的操作,并且是以线的方式
    w = shapefile.Writer(writeFilePath)
    # fields = readPointsCSV(readPath)
    with open(readPath) as myFile:
        myReader = csv.reader(myFile)
        i = 0
        for row in myReader:
            if i == 0:
                w.field(row[0],"N")
                w.field(row[1], "C")
                w.field(row[2], "F")
                w.field(row[3], "F")
                w.field(row[4], "N")
                w.field(row[5], "N")
                w.field(row[6], "N")
                # print(row)
                # w.fields = row
            else:
                # print(*row)
                # print(row[2],row[3])
                w.point(float(row[2]), float(row[3]))
                w.record(*row)

                # print(' '.join(row))
            i = i + 1

    # 激活自动平衡功能
    w.autoBalance = 1
    # 关闭写操作
    w.close()