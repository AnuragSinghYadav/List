#Adding elements to a list :
fruits = ["apple", "banana","Cherry"]
# #1 append() use to add item in the end of the list
fruits.append("kivi")
print(fruits)

#2 insert() use to isert an item at particular index(2,80)
fruits = ["apple", "banana","Cherry"]

fruits.insert(2,"kivi")
print(fruits)

#3 extend() use to add two list items 
fruits = ["apple", "banana","Cherry"]
more_fruits = ["kivi","Mango"]

fruits.extend(more_fruits)

print(fruits)
