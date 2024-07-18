#list allow to store multiple items ina single variable
#list items are: indexed,ordered,mutable,Duplicates allowed, Any datatype, Mix of different data types  
fruits = ["apple", "banana","Cherry"]
print(fruits)
# print(type(fruits))
type(fruits)
# print(len(fruits))
len(fruits)

#check item is present
if "banana" in fruits:
    print("banana is part of the list")

if "kivi" not in fruits: #item not present in list
    print("kivi is not part of the list")

    #indexing in list
    print(fruits[1])
    print(fruits[-1])
    print(fruits[0:2])
    print(fruits[-3:-1])