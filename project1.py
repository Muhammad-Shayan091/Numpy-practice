import numpy as np

# TO ANALYZE THE MARKS OF STUDENT

Marks = np.array([67,53,34,61,89,90,94,93,17,20,66,88,74,63])
print("Marks Of Student : ",Marks)
print("No Of Dimensions : ",Marks.ndim)
print("Average Marks : ",Marks.mean())
print("Highest Marks : ",Marks.max()," at Index : ",Marks.argmax())
print("Lowest Marks : ",Marks.min()," at Index : ",Marks.argmin())
print("Toppers : ",Marks[Marks >= 90])
print("Fail students : ",Marks[Marks <= 40])

Conditions = [
    Marks >= 90 , 
    (Marks >=80) & (Marks < 90) ,
    (Marks >= 65) & (Marks < 80) , 
    (Marks >= 40) & (Marks < 65)
]

Choices = [ "A+" , "A" , "B" , "C"]

grades = np.select(Conditions , Choices , default= "Fail")
print(grades)
