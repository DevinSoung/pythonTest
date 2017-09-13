def is_add(n):
    return n % 2 == 1

print(list(filter(is_add,[1,2,3,4,5,6,7,8,9])))