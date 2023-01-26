ip = input();
m = int(ip.split(" ")[0]); # 3
n = int(ip.split(" ")[1]) + 1; # 16 + 1

## version 2
sieve = [True] * n; # True 17개인 리스트 - 0 ~ 16
for x in range(2 , int(n ** 0.5) + 1): # 2~ 5 사이의 x
    if sieve[x] == True: # x = 2 == True  // 3 // 4 // 5
        for y in range(x + x, n, x): # 4 ~ 17 사이에서 2씩 증가하는 y // 6 ~ 17 3씩 // 8 ~ 17 4씩 // 10 ~  17 5씩
            sieve[y] = False # 4, 6, 8, 10, 12, 14, 16은 false로 변환 // 6, 9, 12, 15 나가리 // 8 12 16 나가리 // 10 15 나가리
# sieve => 0 1 2 3  5  7  11  13   
# 모든 소수 출력
for i in range(m, n):
    if sieve[i]:
        if i != 1:
            print(i);

# for aa in [x for x in range(m, n) if sieve[x] == True]:
#     print(aa);

    
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