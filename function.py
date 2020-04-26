def hello(name):
    print(f"Hello {name}")


hello("PP")


def area(width, hight):
    total = width*hight
    return total


print(area(5, 8))
print(area(3, 2))


def show_info(name="", salary=0.00, lang="not defined"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


show_info()
print()
show_info()
