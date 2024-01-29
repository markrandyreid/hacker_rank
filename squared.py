#for all non-negative integers (i), print(i^2)
#contraints input is <=20

n = int(input())

for num in range(1,n):
    if num >= 0 and num <= 20:
        print(f'{num**2}')
