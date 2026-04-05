import numpy as np

Stu_table = np.array([["ID", "Name" , "Marks" ],
                     [101 , "Shayan" , 90],
                     [102 , "Ayan" , 82],
                     [103 , "Salman" , 65],
                     [104 , "Rahul" , 93],
                     [105 , "Mehra" , 88]] )

print("Student Table data : \n")
print(Stu_table)

print("\nSchema : \n")
print(Stu_table[0])
print("\nTable Rows \n")
print(Stu_table[1])
print(Stu_table[2])
print(Stu_table[3])
print(Stu_table[4])

print("\n Columns \n")
print("ID Column\n")
print(Stu_table[ : , 0 : 1 : 1])
print("\nName Column\n")
print(Stu_table[ : , 1 : 2 : 1])
print("\nMarks Column\n")
print(Stu_table[ : , 2 : 3 : 1])

# THROUGH STRUCTURED ARRAY BITTER WAY

Student = np.array( [(101 , "Shayan" , 90) , 
                     (102 , "Shradha" , 82) , 
                     (103 , "Rahul" , 65) , 
                     (104 , "Suneil" , 93) , 
                     (105 , "Mehra" , 88)
                     ] , dtype = [
                      ('ID' , 'i4') ,
                      ('Name' , 'U10') ,
                      ('Marks' , 'i4')   
                     ] )

print("All the data in Student Table : \n",Student)

# ROWS
print("\nRows In Table : \n")
print(Student[0])
print(Student[1])
print(Student[2])
print(Student[3])
print(Student[4])

# COLUMNS
print("\nColumns In Tables : \n")
print(Student['ID'])
print(Student['Name'])
print(Student['Marks'])

# AGGREGATE FUNTIONS

print("Average : ",Student['Marks'].mean())
print("Total : ",Student['Marks'].sum())
print( Student[Student['Marks'] == Student['Marks'].max()]['Name'], " Got Max marks : ",Student["Marks"].max())
print( Student[Student['Marks'] == Student['Marks'].min()]['Name'], " Got Min marks : ",Student["Marks"].min()) 

# SECOND WAY OF APPLYING AGGREGATE FUNTIONS

print(np.sort(Student , order= 'Marks'))
print(np.ndim(Student))

print(Student['Marks'] > 85 )
print(Student[0 : 3][['Name','Marks']])
# ACCESS ROWS AND COLUMNS TOGETHER  :->  TABLE_NAME[Slice_what_you_want][[col1 , col2]]

print(Student['Marks'])
print(Student[['Name','Marks']])
print(Student[0 : 3][['Name','Marks']])
print(Student)