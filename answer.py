# ANSWER : START
import collections
from operator import itemgetter
import csv
import os


class myFile:
    def __init__(self, filename=None, openmode=None):
        if openmode == 'r':
            self.f = open(filename, 'r')  # self 해야하는...?
            self.contents = self.f.readlines()
            self.memberlist = []
            for line in self.contents[1:]:
                self.memberlist.append(line.strip('\n').split(','))
            # 얘가 정렬된 값이다!
            self.memberlist = sorted(self.memberlist, key=itemgetter(0))
        elif openmode == 'w':
            try:
                self.f = open(filename, 'w')  # fileIOstream
            except:
                raise Exception("Error")

    def getStatus(self):
        return isinstance(self.f, collections.Iterable)

    def getBody(self):  # read 모드 함수에서만 열린다 당연히!
        try:
            return self.memberlist
        except:
            print("Error")
            return False

    def setContentHead(self, firstline=None):
        try:
            self.firstline = firstline
            return True
        except:
            print("error")
            return False

    def setContentBody(self, body=None):
        try:
            self.body = body
            return True
        except:
            print("error")
            return False

    def writeFile(self):
        writer = csv.writer(self.f)
        writer.writerow(self.firstline)
        for i in self.body:
            writer.writerow(i)

    def closeFile(self):
        try:
            self.f.close()
            return True
        except:
            print("Error")
            return False


def mergeList(list1, list2):
    mergedlist = []
    # common ids 모으는 과정
    list1_ids = [list1[j][0] for j in range(len(list1))]
    list2_ids = [list2[j][0] for j in range(len(list2))]
    common_ids = (set(list1_ids)).intersection(set(list2_ids))
    common_ids = list(common_ids)
    for smallist1 in list1:
        if smallist1[0] in common_ids:
            littlelist = []
            littlelist.extend(smallist1)
            mergedlist.append(littlelist)
    i = 0
    for smallist2 in list2:
        if smallist2[0] in common_ids:
            avg = (int(smallist2[1]) + int(smallist2[2]) + int(smallist2[3]))//3
            mergedlist[i].extend(smallist2[1:])
            mergedlist[i].append(avg)
        i += 1
    return mergedlist


# ANSWER : END
print(os.getcwd())

file1 = myFile("inputdata1.csv", 'r')
file2 = myFile("inputdata2.csv", 'r')

if (file1.getStatus() != False) and (file2.getStatus() != False):
    newList = mergeList(file1.getBody(), file2.getBody())

    file3 = myFile("output.csv", 'w')
    file3.setContentHead(["ID", "Name", "Course 1", "Course 2", "Course 3", "Average"])
    file3.setContentBody(newList)
    file3.writeFile()
    file3.closeFile()
else:
    print("input file error")

file1.closeFile()
file2.closeFile()
