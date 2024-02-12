import itertools

number_set = set(map(str, input().split(" ")))
all_list = []
for i in range(1,len(number_set)+1):
    all_list+=list(itertools.combinations(number_set,i))
print(all_list)