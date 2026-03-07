name = "Shivang"

#dynamic values
print(f"My name is {name}")#fstrings
temp = 31
if temp > 30:
  print("VERY HOT")
elif temp >25:
  print("HOT")
else:
  print("NOT HOT")


for i in range(7):
  print(i)

for i in range(1,7): #last idx is exclusive
  print(i)

for i in range(0,10,2):
  print(i)

#LISTS

isTrue = False
my_list = ["Parth", 25, True, isTrue]
name = my_list[0]
print(name);

#DICTIONARIES
my_dict = {
  "name": "Parth",
  "age": 25,
  "isAdult": True
}

# del my_dict["age"]

print(my_dict["age"])

#TUPLES -> Immutable

my_tuple = (3,5, "Parth")

#SETS

my_set = set(["hello", 1, False])
my_set2 = {"hello", 1, False}
scores = {40,40} # Duplicates not allowed

print(scores)

