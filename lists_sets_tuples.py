# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and changeable. Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits = []
more_fruit = input("Do you want to add fruits? Y/N: ")
while more_fruit == "Y":
    one_fruit = input("Please enter a fruit (E to exit): ")
    if one_fruit == "E":
        break
    fruits.append(one_fruit)
if fruits:
    print(f"You have {len(fruits)} fruit/s")
    listing = input("Do you want to know what fruits are in the list? Y/N: ")
    if listing == "Y":
        for fruit in fruits:
            print(fruit)
else:
    print("No fruits!")