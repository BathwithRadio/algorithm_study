m = input();
a = int(m.split(" ")[0]);
b = int(m.split(" ")[1]);

## version 2
sieve = [True] * b;
for x in range(2 , int(b ** 0.5) +1):
    if sieve[x] == True: # x가 소수인 경우
        for y in range(x+x, b, x):
            sieve[y] = False

for aa in [x for x in range(a, b) if sieve[x] == True]:
    print(aa);

    
## version 1 -> 시간 초과
# for x in range(int(m.split(" ")[0]) , int(m.split(" ")[1])+1):
#     if x == 1:
#         print(x)
#     else :
#         i = 2;
#         while x % i:
#             i += 1
#         if i == x :
#             print(x)