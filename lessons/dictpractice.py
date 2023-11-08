"""Syntax and Practice with Dictionaries in class 10/23!"""

# Construct an empty dict
dict()

# Construct a populated dictionary. 
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# To view dictionary / print it. 
print("I made my dictionary.")
print(ice_cream)

# Adding elements using subscription notation (add 3 orders of mint). 
ice_cream["mint"] = 3
print(ice_cream)

# Rem,oving elements (remove orders of mint from ice_cream). 
ice_cream.pop("mint")
print(ice_cream)

# Accessing a value.(Print how many orders there are of chocolate). 
ice_cream["chocolate"]
print(ice_cream["chocolate"])

# Modifying a value. (Update number of orders in canilla to 10). 
ice_cream["vanilla"] = 10
print(ice_cream["vanilla"])

# To find the length of the dict ice_cream.
len(ice_cream)
print(len(ice_cream))

# Check if key in dictionary. (check if flavors mint and chocolate are in ice_cream).
if "mint" in ice_cream:
    print(ice_cream["mint"])
else: 
    print("There are no orders of mint.")

if "chocolate" in ice_cream:
    print(ice_cream["chocolate"])
else: 
    print("There are no orders of chocolate")

# Loop through and print out every flavor and its number of orders.
for key in ice_cream:
    #print flavor has "(num_orders>)""
    print(f"{key} has {ice_cream[key]} orders.")




