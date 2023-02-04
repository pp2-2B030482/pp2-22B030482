#Add a placeholder where you want to display the price:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"

#If you want to use more values, just add more values to the format() method:
print(txt.format(price, itemno, count))

#
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))