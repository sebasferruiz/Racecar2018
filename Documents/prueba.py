<<<<<<< HEAD
import numpy as np
from matplotlib import pyplot as plt

MaxRen = 35
MaxCol = 35
=======
#!/usr/bin/env python
#ImageMove

import cv2
import numpy as np


B = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4],[5, 5, 5, 5, 5]]

>>>>>>> 18101b074938788bd55982eb31beb23f6e663bf6

felix = [[1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1],
[1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1],
[1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1],
[1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0],
[1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
[1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
[1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0],
[1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0],
[1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0],
[1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0],
[1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0],
[1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
[1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
[1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1],
[1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
[1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1],
[1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]]



<<<<<<< HEAD
def invertircolores(felix):
    for i in range(len(felix)):
        for j in range(len(felix[0])):
            if felix[i][j] == 1:
                felix[i][j] = 0
            else:
                felix[i][j] = 1
    return felix

def mirrorv(felix):
    ren = len(felix)-1
    for i in range(17):
        for j in range(len(felix[0])):
            felix[ren][j] = felix[i][j]
        ren -= 1
    return felix

def mirrorh(felix):
    col = len(felix)-1
    for i in range(len(felix)):
        for j in range(17):
            felix[i][col] = felix[i][j]
            col -= 1
        col = len(felix)-1 
    return felix

def flipv(felix):
    ren = len(felix)-1
    temp = np.zeros((35,35))
    for i in range(len(felix)):
        for j in range(len(felix[0])):
            temp[ren][j] = felix[i][j]
        ren -= 1
    return temp

def fliph(felix):
    col = len(felix[0])-1
    temp = np.zeros((35,35))
    for i in range(len(felix)):
        for j in range(len(felix[0])):
            temp[i][col] = felix[i][j]
            col -= 1
        col = len(felix[0])-1
    return temp

def rotd(felix):
    temp = np.zeros((35,35))
    ren = 0
    col = len(felix)-1
    for i in range(len(felix)):
        for j in range(len(felix[0])):
            temp[ren][col] = felix[i][j]
            ren += 1
        col -= 1
        ren = 0
    return temp

def roti(felix):
    temp = np.zeros((35,35))
    ren = 0
    col = len(felix)-1
    for i in range(len(felix)):
        for j in range(len(felix[0])):
            temp[i][j] = felix[ren][col]
            ren += 1
        col-=1
        ren = 0
    return temp


izq = roti(felix)
plt.imshow(izq)
plt.show()

derecha = rotd(felix)
plt.imshow(derecha)
plt.show()

fliphor = fliph(felix)
plt.imshow(fliphor)
plt.show()

flipver = flipv(felix)
plt.imshow(flipver)
plt.show()

mirrorhor = mirrorh(felix)
plt.imshow(mirrorhor)
plt.show

mirrorver = mirrorv(felix)
plt.imshow(felix)
plt.show()

inverso = invertircolores(felix)
plt.imshow(inverso)
plt.show

felix = np.matrix(felix)
plt.imshow(felix)
plt.show()
=======









def RotateLeft(A):
	New = [[0 for x in range(len(A))] for y in range(len(A[0]))]

	for num in range(len(New)):
		for element in range(len(New[num])):
			New[num].pop()


	for num in range(len(A[0])):
		for row in A:
			
			New[num].append(row[num])

	

	print ("Rotated: ")
	for line in New:
		print (line)


	return New

def VertFlip(A):
	New = []
	for num in range(len(New)):
		for element in range(len(New[num])):
			New[num].pop()


	for line in A[::-1]:
		New.append(line)

	print ("Vertical Flip: ")
	for line in New:
		print (line)

	return New


def VertMirror(A):
	New = []
	for num in range(len(New)):
		for element in range(len(New[num])):
			New[num].pop()


	for line in A[::-1]:
		New.append(line)

	print ("Vertical Mirror: ")
	for line in New:
		print (line)

	print ("___________________")

	for line in A:
		print (line)

	return New

def HorMirror(A):
	New = []
	for num in range(len(New)):
		for element in range(len(New[num])):
			New[num].pop()


	for line in A:
		New.append(line[::-1])

	print ("Horizontal Mirror: ")
	for num in range(len(A)):
		print (A[num] + ["|"] + New[num] )

	return New

def HorFlip(A):
	New = []
	for num in range(len(New)):
		for element in range(len(New[num])):
			New[num].pop()


	for line in A:
		New.append(line[::-1])

	print ("Horizontal Flip: ")
	for line in New:
		print (line)

	return New

def ColorChange(A):

	print("Inverted Colors: ")

	for line in range(len(A)):
		count = 0
		for number in A[line]:
			if number > 150:
				A[line].pop(count)
				A[line].insert(count, 0)
				count += 1
			elif number <= 150:
				A[line].pop(count)
				A[line].insert(count, 255)
				count += 1

	for line in A:
		print (line)

	return A

def RotateRight(A):
	return RotateLeft(A[::-1])


	
>>>>>>> 18101b074938788bd55982eb31beb23f6e663bf6
