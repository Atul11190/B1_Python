x = 10  # Global variable


def outer_function():
    x = 20  # Enclosing variable
    def inner_function():
        x = 30  # Local variable
        print(x)  # Output: 30
    inner_function()
    print(x)  # Output: 20
outer_function()
print(x)  # Output: 10
print("----------------")

# MODIFICATION
counter = 0


def increment():
    global counter
    counter += 1
increment()
print(counter)  # Output: 1
print("-----------------")
#MUTUABLE AND IMMUTABLE
def modify_mutable(lst):
      lst.append(4)
      print(f"Inside function: {lst}")
      my_list = [1, 2, 3]
      modify_mutable(my_list)
      print(f"Outside function: {my_list}")  # Output: [1, 2, 3, 4] (modified)
  def modify(x):
      print(f"Before: {id(x)}")
      x += 1
      print(f"After: {id(x)}")
      a = 5
      modify(a)
  
