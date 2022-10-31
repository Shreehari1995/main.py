path = r"C:\Users\Dell\PycharmProjects\pythonProject\project1\file1"

import os
print(os.getcwd())

# with open(path) as file:
#     count = 0
#     for line in file:
#         j = line.split()
#         for i in j:
#             count += 1
#     print(count)

# with open(path) as file:
#     l = []
#     for i in file:
#         l.append(i)
#     print(l[::-1])
#
#     for i in l[::-1]:
#         print(i)

# with open(path) as file:
#     f = file.read()
#     print(f.count(" "))
#
# with open(path) as file:
#     c = 0
#     for i in file:
#         for j in i:
#             if j == " ":
#                 c += 1
#     print(c)



# with open(path) as file:
#     count = 0
#     for line in file:
#         j = line.split()
#         for i in j:
#             if i[0] in "aeiouAEIOU":
#                 count += 1
#     print(count)


# with open(pa5th) as file:
#     d = {}
#     for i in file:
#         j = i.split()
#         for m in set(j):
#             if m not in d:
#                 d[m] = j.count(m)
#             else:
#                 d[m] = d[m] + j.count(m)
#     print(d)
#
# with open(path) as file:
#     d = {}
#     for i in file:
#         j = i.split()
#         for m in j:
#             if m not in d:
#                 d[m] = 1
#             else:
#                 d[m] +=1
#     print(d)


# n = 5
# with open(path) as file:
#     for i in range(n):
#         i
#
#     print(list(file)[i])
# n = 3
from itertools import islice
from  collections import deque
# with open(path) as file:
#     r = islice(file, n)
#     print(list(r))

# with open(path) as file:
#     c = 0
#     for i in file:
#         c += 1
#     file.seek(0)
#     r = islice(file, c-n, c)
#     print(list(r))
#     file.seek(0)
#     r1 = deque(file, n)
#     print(list(r1))

lgpath = (r"C:\Users\Dell\PycharmProjects\pythonProject\Alpha_3\files_directory\txt_log_files\sample.log")
# with open(path) as file:
#     for i in file:
#         print(len(i),end=" ")
#
# with open(lgpath) as file:
#     for i in file:
#         if i.strip():
#             j = i.split()
#             r =


csvpath = r"C:\Users\Dell\PycharmProjects\Alpha_3_class\files_directory\csv_files\test.csv"
import csv
# with open(csvpath) as csv_f:
#     r_obj = csv.reader(csv_f)
#     header = next(r_obj)
#     shares = 0
#     for row in r_obj:
#         shares += int(row[1])
# print(shares)

  # ASSAIGNMEN
#total vaccination of all the country and total vaccinations by country
pathvc = r"C:\Users\Dell\PycharmProjects\Alpha_3_class\files_directory\csv_files\vaccination_data.csv"
import csv
# with open(pathvc) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         print(row[0], row[5],sep="-")

# with open(pathvc) as file:
#     r_obj = csv.DictReader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         print(row["TOTAL_VACCINATIONS"],sep="-")

d = {}
# with open(pathvc) as file:                doubt
#     r_obj = csv.DictReader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         d[row[0]] = row[5]
# print(d)



#names of countries and WHO region
# with open(pathvc) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         print(row[0], row[2],sep="-")

# country and person vaccinated and top 3 countries with most vaccinated people          DOUBT
from itertools import islice
# with open(pathvc) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     c = 0
#     for row in r_obj:
#         c += 1
#         print(row[0], row[7],sep="-")
#     file.seek(0)
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     l = list(r_obj)
#     print(l)
#     r = sorted(l, key=lambda i: float(i[7]))
#     print(list(r))
#     print(list(islice(r, c-3, c)))



# countries with less than 10000 vaccination people               DOUBT
# with open(pathvc) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         if int(row[5]) <= 10000:
#             print(row[0], row[5],sep="-")


#latest updated contry and its total vaccinations ans no of ppl vaccinated
# with open(pathvc) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     c = 0
#     for i in r_obj:
#         c += 1
#     file.seek(0)
#     l = list(r_obj)
#     print(l[c][0], l[c][5], l[c][6], sep="-")

# d = {}
# with open(pathvc) as file:
#     r_obj = csv.DictReader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         d[row["TOTAL_VACCINATIONS"]] = row["DATE_UPDATED"]
#     print(d)
#     r = sorted(d.items(), key= lambda i: int(i[1]))
#     print(r)


# l = [2, 3, 9, 5, 8, 2, 3, 0, 4, 5, 3, 7, 1, 3, 8]
# l1 = []
# key = 3
# c = 0
# for i in range(key+1):
#     if i % 2 == 0:
#         l1.append(l[i] + l[i+2-c])
#         c += key
#     else:
#         l1.append(l[i-1])
# print(l1)


# s = "AABBCCCDAACD"
# # O/P = 2A2B3C1D2A1C1D
# s1 = ""
# n = 0
# k = "l"
# if s[0] != k:
#     m = k       # 'l'
# else:
#     m = "k"
# for i in s:
#     if m == i:
#         continue
#     else:
#         m = i
#         c = 0
#         for j in s[n:]:
#             if i == j:
#                 c += 1
#             else:
#                 break
#         n += c
#         s1 = s1 + str(c) + i
# print(s1)
import re
#print(dir(re))
# s = re.findall(r".","hallo world")
# print(s)
#
# string = "hai python"
# a = re.findall(r"a.c", "acb")
# print(a)
#
# a = re.findall(r"^hei", "hei hello how are uh")
#print(a)
# a = re.findall(r"n*a","anna")
# print(a)
#
# # a = re.findall(r"a*b","aaaaaannb")
# # print(a)
# #
# #
# a = re.findall(r"an*a","annnaaanna")
# print(a)
#
# a = re.findall(r"a*b", "abbhjhshjaaaamb")
# print(a)

# s = re.findall(r"ab+b", "abbc")
# print(s)


s = "Aaaaaa@#$$ABBCCCDAACD"
# O/P = 2A2B3C1D2A1C1D
print ("output:2A2B3C1D2A1C1D")
i = 0
count = 0
res = ""
while i < len(s):
    if s[i] == s[i+1 : i+2]:
        count += 1
        i += 1
    else:
        count += 1
        res += str(count) + s[i]
        count = count - count
        i += 1
print(res)


























