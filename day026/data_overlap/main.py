with open("file1.txt") as f1:
    list1 = f1.readlines()

with open("file2.txt") as f2:
    list2 = f2.readlines()

result = [int(i) for i in list1 if i in list2]
# Write your code above 👆

print(result)
