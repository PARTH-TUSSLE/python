def greet(name="John Doe"):
    print(f"Hello {name}")
    pass # -> returns nothing
# greet("Parth")
greet(name="Parth")

def calculate_sum(a, b):
    return(a+b)

sum = calculate_sum(2,5)
print(sum+2)

def multiple_returns():
    my_list = [1,2,3,4,5]
    return my_list[0], my_list[-1]

first, last = multiple_returns()
print(first, last)