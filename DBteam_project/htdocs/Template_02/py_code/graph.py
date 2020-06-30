# -*-coding: utf-8-*-
import sys
import csv, codecs
def graph(name):
    count = [0, 0, 0, 0, 0, 0]
    result = [0,0,0,0,0,0]
    file = open('part\\c1={} Station\\000000_0'.format(name), 'r', encoding='utf-8')
    read = csv.reader(file, delimiter="\n")
    for cell in read:
        cell = cell[0].split(",")
        if cell[0][:-1] != 'Erro':
            if int(cell[0][:-1]) < 6:
                count[int(cell[0][:-1])] += 1
    for i in range(0,6):
         result[i]=((count[i]-min(count))/(max(count)-min(count))+0.5)*10//1
         
    for i in result:
        print(i)

graph(sys.argv[1])