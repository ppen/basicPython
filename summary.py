print("------------------")
print("# sum")
print("# type exit")
print("------------------")

sumdata = 0
count = 1
while True:
    data = input(f"Enter number{count}:")
    if data == "exit":
        break

    sumdata += int(data)
    count = count + 1

print(f"Sum value is {sumdata}")
