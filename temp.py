name = "Bhavesh"

lis = list(name)

start = 0

ends = len(lis) - 1


while start < ends:
    lis[start], lis[ends] = lis[ends], lis[start]

    start +=  1
    ends -= 1

print(lis)
    
    