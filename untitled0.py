# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:46:58 2024

@author: Navin
"""




import numpy as np
import xlrd # type pip install xlrd in console window

#Read excel file
wb = xlrd.open_workbook('D:\equations.xls')

sheet1 = wb.sheet_by_index(0) # index 0 means first sheet
m = sheet1.nrows #This will return numbers of row
n = sheet1.ncols #This will return numbers of column


b = np.zeros([m, m, n-1]) #This is a 3-Dimentional Matrix

Const = np.zeros([m, 1])

d = np.zeros([m, 1])
roots = np.zeros([m, 1])

#Extract value from excel file and store in "b" which is a 3-dimentional matrix
for rowNumber in range(sheet1.nrows):
    for colNumber in range(sheet1.ncols):
        if colNumber == n-1:
            Const[rowNumber, 0] = sheet1.cell_value(rowx=rowNumber, colx=colNumber)
        else:
            b[0, rowNumber, colNumber]  = sheet1.cell_value(rowx=rowNumber, colx=colNumber)

print("The equations coefficients are: ")
print(b[0,:,:])
print("\nThe equations constant are: ")
print(Const)

c = np.zeros([m,m])
t = m
p=m
k=0


#Detemin U
for k in range(m-1):
    for i in range(m):
        for j in range(n-1):
            if i<=k:
                b[k+1, i, j] = b[k, i, j]
            else:
                b[k+1, i, j] =b[k, i, j] - (b[k,k,j]/b[k,k,k])*b[k,i,k]
        
print("\nThe U is: ")
print(b[m-1,:,:])

#Determin L
s=0
for j in range(n-1):
    for i in range(m):
        if i==j:
            c[i, j] = 1
        elif i<j:
            c[i, j] = 0
        else:
            c[i, j] = b[s, i, j]/b[s, s, s]
    s=s+1
    
print("\nThe L is: ")
print(c)

#Find D
sum = 0
for i in range(m):
    for j in range(i):
        sum = sum + c[i, j]*d[j, 0]
    sum = Const[i,0] - sum
    d[i, 0] = sum
    sum = 0
    
print("\nThe D is: ")
print(d)

# Find Roots
sum1 = 0

for i in range(m-1, -1, -1):
    for j in range(n-2, i, -1):
        sum1 = sum1 + b[m-1, i, j]*roots[j, 0]
    sum1 = (d[i,0] - sum1)/b[m-1, i, i]
    roots[i, 0] = sum1
    sum1 = 0

print("\nThe roots are: ")    
print(roots)