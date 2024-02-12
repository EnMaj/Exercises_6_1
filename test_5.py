n = int(input())
array = []
for i in range(n+1):
    array.append(i)

i = 2
while i <= n ** 0.5:
    if array[i] != 0:
        j = i ** 2
        while j<=n:
            array[j] = 0
            j+=i
    i = i +1

array = set(array)
array.remove(0)
print(array)
