'''
PROJECT 2
Generate 2 matrixes
(1. ask for matrix size A, then matrix size B)
(2.give sum)
(3.Subtraction)
(4.multiplication, keep in mind: a*b != b*a)

DISCLAIMER:
1.Code only generates same sized matrices...
2.if column size isn't the same, code
won't be able to run multiplication
'''

#Step 1, producing a matrix

i = 0
j = 0
A = []
B =[]


print("This program asks you to generate a matrix, \nthen it gives sum, difference and mult."
      + "\nProgram will ask you to put elements row by row")

A_WIDTH = int(input("\nFirst define column A width: "))

newRow = []
print("what are your " + str(A_WIDTH) + " elements?")

endRow = 0
while i < A_WIDTH and endRow == 0:
        newRow.append(int(input("element " + str(i+1) + ": ")))
        i = i + 1
        if i == A_WIDTH:
            i=0
            A.append(newRow)
            newRow = []
            endRow = int(input("end of matrix A? 1:yes, 0:no, go to other row.. "))
            


print("\nthis is matrix A: " + str(A))
    

B_WIDTH = int(input("\nNow define column B width (you're at the second matrix): "))


print("choose your " + str(A_WIDTH) + " elements now (for second matrix): ")
newRow = []
endRow = 0  
while i < B_WIDTH and endRow == 0:
        newRow.append(int(input("element " + str(i+1) + ": ")))
        i = i + 1
        if i == B_WIDTH:
            i=0
            B.append(newRow)
            newRow = []
            endRow = int(input("end of matrix B? 1:yes, 0:no, go to other row.. "))
        
    

print("\nthis is matrix B: " + str(B))


#if statements which fill a region with 0's
if A_WIDTH < B_WIDTH:
        C = B_WIDTH - A_WIDTH
        for i in range(0, C + 1):
                A[i].append(0)
if B_WIDTH < A_WIDTH:
        C = A_WIDTH - B_WIDTH
        for i in range(0, C + 1):
                B[i].append(0)
'''
gives error on multiplication
because rows in A and B are
same size as columns
'''

#Step 2: Matrix Addition 

def Addition(A, B):
        add = []
        for i in range(0, len(A)):
                add.append(A[i] + B[i])
        return add

SUM = []

for i in range(0, len(A)):
        SUM.append(Addition(A[i], B[i]))
        
        


print("\nNow that you've generated these matrices...\n"
      + "\nMatrix A: " + str(A) + "\n+\n" + "Matrix B: "
      + str(B) + "\nis")
for i in SUM:
        print(i)



#Step 3: Matrix Subtraction (A-B)

def Subtraction(A, B):
        sub = []
        for i in range(0, len(A)):
                sub.append(A[i] - B[i])
        return sub

SUB1 = []

for i in range(0, len(A)):
        SUB1.append(Subtraction(A[i], B[i]))
        
print("\n"
      + "Matrix A: " + str(A) + "\n-\n" + "Matrix B: "
      + str(B) + "\nis")
for i in SUB1:
        print(i)
#Step 4: Matrix Subtraction (B-A)

def Subtraction(B, A):
        sub = []
        for i in range(0, len(A)):
                sub.append(A[i] - B[i])
        return sub

SUB2 = []

for i in range(0, len(A)):
        SUB2.append(Subtraction(A[i], B[i]))
        
print("\n"
      + "Matrix B: " + str(B) + "\n-\n" + "Matrix A: "
      + str(A) + "\nis")
for i in SUB2:
        print(i)

#Step 5: Matrix multiplication (A x B)
'''
DISCLAIMER:
only works if for ixj, where j != 0
only works if for jxk, where k !=0
'''
# matrix A row length, column length...
mul = []
cols = len(A[0])
rows = len(A)


# A:i x j B: j -k

for i in range(0,rows):
        temp_list = []
        for k in range(0,rows):
                sum1 = 0
                for j in range(0, cols):
                    sum1 = sum1 +(A[i][j]*B[j][k])
        
                temp_list.append(sum1) #result of 1 element process
        mul.append(temp_list) #add each multiplication on list

print("\n"
      + "Matrix A: " + str(A) + "\n*\n" + "Matrix B: "
      + str(B) + "\nis")
for i in mul:
        print(i)

#Step 6: Matrix multiplication (B x A)

mul = []
cols = len(B[0])
rows = len(B)

        
# B:i x j A: j x k

for i in range(0,rows):
        temp_list = []
        for k in range(0,rows):
                sum1 = 0
                for j in range(0, cols):
                    sum1 = sum1 +(B[i][j]*A[j][k])
        
                temp_list.append(sum1) #result of 1 element process
        mul.append(temp_list) #add each multiplication on list

            
print("\n"
      + "Matrix B: " + str(B) + "\n*\n" + "Matrix A: "
      + str(A) + "\nis")
for i in mul:
        print(i)
