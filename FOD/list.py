# Printing list of square of numbers 1-30 except first five elements

lst = []

for i in range(1, 31):
    lst.append(i*i)

print(f"list = {lst}\n")
print("List of square of numbers 1-30 except first five elements : ")
print(lst[5:])
