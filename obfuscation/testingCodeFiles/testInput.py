def greet(name):
    if name == "Alice":
        return "Hello, Alice!"
    elif name == "Bob":
        return "Hey Bob!"
    else:
        return "Hi there!"

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def process_numbers(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num ** 2)
        else:
            result.append(num)
    return result

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        if self.species == "dog":
            return "Woof!"
        elif self.species == "cat":
            return "Meow!"
        else:
            return "???"

def main():
    print("Greet Test:", greet("Alice"))
    print("Factorial Test:", factorial(5))
    print("Process Numbers Test:", process_numbers([1, 2, 3, 4]))
    print("Animal Test:", Animal("cat").speak())

main()