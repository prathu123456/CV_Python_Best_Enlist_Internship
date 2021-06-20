#1) Write a program to create a list of n integer values and do the following
#• Add an item in to the list (using function)
#• Delete (using function)
#• Store the largest number from the list to a variable
#• Store the Smallest number from the list to a variable
a = ["5","10","15","40","70"]
print("List :",a)
a.append("50")
print("List after adding 50:",a)
a.remove("15")
print("List after removing 15 :",a)
b = max(a)
c = min(a)
print("Largest number b :",b)
print("Smallest number c :",c)

#2) Create a tuple and print the reverse of the created tuple
Tuple_1 = ["do","run","went","is"]
print("Tuple 1 :",Tuple_1)
REV = reversed(Tuple_1)
print("Reverse of Tuple 1 :",tuple(REV))

#3) Create a tuple and convert tuple into list
T = ('a','d','f','t')
d = list(T)
print(d)
