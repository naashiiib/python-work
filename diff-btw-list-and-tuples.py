fruit_list = ["apple", "banana", "cherry"]
fruit_tuple = ("apple", "banana", "cherry")
fruit_list[1] = "mango"
print("List :", fruit_list)
try:
    fruit_tuple[1] = "mango"
except TypeError as e:
    print("Tuple:", e)