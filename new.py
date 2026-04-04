import numpy as np

List = [1,2,3,4]
List *= 2 
print(List)

array = np.array([1,2,3,4])
array *= 3
print(array)
print(type(array))

# ZERO-DIMENTIONAL ARRAY

array_1 = np.array('A')
print("Zero dimentional Array : ",array_1)
print(array_1.ndim)

# ONE-DIMENTIONAL ARRAY 

array_2 = np.array([1,2,3,4,5])
print("One dimentional Array : ",array_2)
print(array_2.ndim)

# TWO-DIMENTIONAL ARRAY 

array_3 = np.array([[1,2,3,4] , [5,6,7,8] , [5,6,7,8]])
print("Two dimentional Array : \n",array_3)
print(array_3.ndim)

# THREE-DIMENTIONAL ARRAY 

array_4 = np.array([[['A','B','C'] , ['D','E','F'] , ['G','H','I']] ,  
                   [['J','K','L'] ,  ['M','N','O'] , ['P','Q','R']] ,
                   [['S','T','U'] ,  ['V','W','X'] , ['Y','Z','_']]])
print(array_4)
print(array_4.ndim)
print(array_4.shape)

# CHAIN-INDEXING  : INDEX START FROM 0 , 1 , 2....
print(array_4[1][2][2])      # [Layer] , [Row] , [Column]

# MUTI-DIMENTIONAL INDEXING  : INDEX START FROM 0 , 1 , 2.... 
print(array_4[1 , 2 , 2])    # [Layer] , [Row] , [Column]

Ltr1 = array_4[0 , 0 , 0]    # A - access
print(Ltr1)
Ltr2 = array_4[2 , 0 , 0]    # S - access
print(Ltr2)
Ltr3 = array_4[0 , 1 , 2]    # F - access
print(Ltr3)
word = Ltr1 + Ltr2 + Ltr3
print("Word : ",word)        # ASF - access
word_2 = array_4[1 , 2 , 0] + array_4[2 , 0 , 1] + array_4[0 , 2 , 2]      # PTI - access
print(word_2)
word_3 = array_4[2 , 0 , 0] + array_4[0 , 0 , 0] + array_4[0 , 2 , 2] + array_4[0 , 1 , 2]  # SAIF - access
print(word_3)
# BOTH RETURN THE SAME ELEMENT BUT SYNTAX IS DIFFERENT

# SLICING USING NUMPY

array = np.array([[1,2,3] ,
                  [4,5,6] ,
                  [7,8,9] , 
                  [10,11,12]])

print("Array : \n\n",array)
print("\n")
print("Number of dimensions : ",array.ndim)
print("\n")
print("Access by Indexing : \n")
print("Row 1 : ",array[0])
print("Row 2 : ",array[1])
print("Row 3 : ",array[2])
print("Row 4 : ",array[3])

# SYNTAX :-> array [ St : end : step ]

print("Access by Slicing : ")     

print("\nSlice 1 [0 -> 3]: \n")
print(array[0 : 3])

print("\nSlice 2 [2 -> 4]: \n")
print(array[2 : 4])

print("\nSlice 3 [1 -> 4]: \n")
print(array[1 : 4])

print("\nSlice 4 [-4 -> -1]: \n")
print(array[-4 : -1])

# Also Steps : 

print("\nSlice 5 [1 -> 4]: \n")
print(array[1 : 4 : 1])

print("\nSlice 6 [1 -> 4]: \n")
print(array[1 : 4 : 2])

print("\nSlice 7 [0 -> 4]: \n")
print(array[0 : 4 : 2])

print("\nSlice 8 [0 -> 1]: \n")
print(array[0 : 1 : 1])

# TO SELECT ALL ROWS AND COLUMNS

print("\nTo select All the array : [ : , : ] \n")
print(array[ : , :])

# TO ACCESS THE COLUMNS OF ARRAY
print("\nTo Select the columns : \n")
print("C1 : ")
print(array[ : , 0])
print("\nC2 : ")
print(array[ : , 1])
print("\nC3 : ")
print(array[ : , 2])

# ALSO SLICING IN COLUMNS
print("\nFrom 0 --> 3 : \n")
print(array[ : , 0 : 3])
print("\nFrom 0 --> _ : \n")
print(array[ : , 0 :  ])
print("\nFrom _ --> 3 : \n")
print(array[ : ,   : 4])
print("\nFrom 0 --> 3 : \n")
print(array[ : , 0 : 3])
print("\nFrom 1 --> 3 : \n")
print(array[ : , 1 : 3])
print("\nFrom 1 --> 2 : \n")
print(array[ : , 1 : 2])
print("\nFrom  -->  : \n")
print(array[ : , : : -1])
print("\nFrom 0 --> 3 , Step = 2 : \n")
print(array[ : , : : 2])
print("\nFrom 1 --> 3 , Step = 2 : \n")
print(array[ : , 1 : 3 : 2])

# To Select A Quadrant

print("\nFirst Quadrant : \n")
print(array[ 0 : 2 , 0 : 2])
print("\nSecond Quadrant : \n")
print(array[ 0 : 2 , 1 : 3])
print("\nThird Quadrant : \n")
print(array[ 2 : 4 , 0 : 2])
print("\nFourth Quadrant : \n")
print(array[ 2 : 4 , 1 : 3])

# ARITHMATIC IN NUMPY

Array = np.array([1,2,3,4,5])
Arrar_2 = np.array([5,6,7,8,9])

print("Sum : ",Array+10)
print("Subtraction : ",Array-2)
print("Multiply : ", Array * 5)
print("Divide : ", (Array/3))
print("Square : ",Array**2)
print(np.sqrt(Array))
print(np.round(Array))
print(np.pi)

# BETWEEN ARRAYS 

print("Sum : ", (Arrar_2 + Array))
print("Difference : ", (Arrar_2 - Array))
print("Multiply : ", (Arrar_2 * Array))
print("Division : ", (Arrar_2 / Array))
print("Power : ", (Arrar_2 ** Array))

# Assignment

# A = pi.r^2
r = np.array([1,2,3])
pi = np.pi
A = pi*(r)**2
print(A)

# TO RETURN BOOLEAN ARRAY - COMPARISON OPERATORS

Marks = np.array([67 , 79 , 90 , 93 , 100 , 33 , 46])

print(Marks >= 60)
print(Marks == 100)
print(Marks >= 90)
print(Marks != 100)
print(Marks < 40)

Marks[ Marks < 45] = 0
print(Marks)

# BROADCASTING IN NUMPY-ARRAYS

# Rules :
#       - No of C of Arr1 = No of C of Arr2           OR        One Of the columns numbers will be '1'  Eg (3 , 3)and(3 , 3) OR (3 , 3)and(3 , 1)
#       - No of R of Arr1 = No of R of Arr2           OR         One Of the Rows numbers will be '1'    Eg (3 , 3)and(3 , 3) OR (3 , 3)and(1 , 3)

Array1 = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
Array2 = np.array([[3,2,1] , [6,5,4] , [9,8,7]])

print(Array1.shape)
print(Array2.shape)

print((Array1 * Array2).shape)
print(Array1 * Array2)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([ [1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

# AGGREGATE FUNTIONS : SUMMARIZE THE DATA AND RETURN SOME VALUES

Array = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,12,13,14,15]])

print("Array : \n", Array)
print("\nSum : \n", Array.sum())
print("\nShape : \n", Array.shape)
print("\nMax_ele : \n", Array.max())
print("\nMin_ele : ", Array.min())
print("\nIdx_max : \n", Array.argmax())
print("\nIdx_min : \n", Array.argmin())
print("\nMean : \n", Array.mean())
print("\nStd_dev : \n", Array.std())
print("\nVariance : \n", Array.var())
print("\nTranspose : \n", Array.transpose())

print("First Row : ",Array[0].sum())
print("First Column : ",Array[ : , 0].sum())
print("Second Column : ",Array[ : , 1].sum())
print("Third Column : ",Array[ : , 2].sum())
print("Fourth Column : ",Array[ : , 3].sum())

FILTERING : THE PROCESS OF SELECTING THE DATA WHICH FOLLOW OR DONT FOLLOW SOME CONDITIONS ARE CALLED FILTERING 

ages = np.array([[20,31,24,45,21,15,18,17,16,98,80] , [43,25,66,52,27,73,43,53,67,81,55]])

teenagers = ages[ages < 18]
print("Teenagers : ",teenagers)
adults = ages[((ages >= 18) & (ages < 65))]
print("Adults : ",adults)
jawan = ages[(ages >= 18) & (ages <=30)]
print("Jawan : ",jawan)
seniors = ages[ages >= 65]
print("Seniors : ",seniors)
age_even = ages[ages % 2 == 0]
print("Stu with Even ages : ",age_even)
age_odd = ages[ages % 2 != 0]
print("Stu with odd ages : ",age_odd)

# where Funtion 
New = np.where(ages >= 18 , "adults" , "Teenagers")
print(New)

TO GENRATE RANDOM NUMBERS USING NUMPY

rng = np.random.default_rng()                                      # This Funtion Takes only one argument

print(rng.integers( low = 1 , high = 101 , size = 5))
print("\n")
print(rng.integers(low = 0 , high = 100 , size = (3 , 4)))
print("\n")
print(1 , 20 , 3)
print("\n")
print(rng.integers(1 , 200 , (3 , 3)))

print(rng.integers(low= -1 , high= 1 , size=(3 , 3)))               # High one is exclusive

# TO Genrate the decimal Values

print(np.random.uniform(low= -1 , high= 0 , size= (1 , 3)))

# TO SHUFFLE AN ARRAY
array = np.array([1,2,3,4,5])

rng = np.random.default_rng()
rng.shuffle(array)
print(array)

# RANDOM FUNTION QUESTION

rng = np.random.default_rng()
fruits = np.array(["Apple" , "Banana" , "Peach" , "Appricot" , "Orange" , "Guava"])

Fruit = rng.choice(fruits , size=(2, 3))
print(Fruit)