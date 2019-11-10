# Number which is divisible by 7 but not a multiple of 5
begin = int(input("Enter starting range:"))
end = int(input("Enter stoping range :"))

list = []
for value in range(begin, end):
    if value % 7 == 0:
        if value % 5== 0:
            continue
        else:
            list.append(str(value))

print(','.join(list))