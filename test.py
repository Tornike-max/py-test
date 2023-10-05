arr = []
for x in range(5):
    arr.append(input('string: '))


print(arr)

longest = 0
for l in arr:
    curLenght = len(l)
    if curLenght > longest:
        longest = curLenght
print(longest)