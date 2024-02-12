import itertools

number_set = set(map(str, input().split(" ")))
n = len(number_set)
k = int(input())
print(list(itertools.combinations(number_set,k)))