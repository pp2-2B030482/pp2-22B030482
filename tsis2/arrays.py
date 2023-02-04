#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]

#Get the value of the first array item:
x = cars[0]

#Modify the value of the first array item:
cars[0] = "Toyota"

#Return the number of elements in the cars array:
x = len(cars)

#Print each item in the cars array:
for x in cars:
  print(x)

#Add one more element to the cars array:
cars.append("Honda")

#Delete the second element of the cars array:
cars.pop(1)

#Delete the element that has the value "Volvo":
cars.remove("Volvo")

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list