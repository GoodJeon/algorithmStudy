# 내장함수
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공(수열, 조합)

# heapq : 힙(heap) 자료구조 제공, 일반적으로 우선순위 큐 기능 구현을 위해 사용

# bisect :  이진탐색(binary search) 기능 제공

# collections : 덱(deque), 카운터(Counter) 등 유용한 자료구조 포함

# math : 필수적 수학기능 제공(팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이 등)

# sum()
result = sum([1,2,3,4,5])
print(result) # 15

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result) # 2 7

# eval()
result = eval('(3+5)*7')
print(result) # 56

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result, reverse_result)

# sorted() with key
array = [('홍길동',35),('이순신',75),('아무개',50)]
result = sorted(array, key = lambda x: x[1], reverse=True)
print(result) # 숫자 위주로 내림차순해서 반환



# 순열
from itertools import permutations

data = ['A','B','C']

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# 조합
from itertools import combinations

data = ['A','B','C']

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# 중복 순열
from itertools import product

data = ['A','B','C']

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

# 중복 조합 
from itertools import combinations_with_replacement

data = ['A','B','C']

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)




# Counter
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(dict(counter)) # 사전 자료형으로 반환





# 최대공약수, 최소공배수 gcd
import math

# 최소공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a=21
b=14

print(math.gcd(21,14)) # 최대 공약수(GDC) 계산
print(lcm(21,14)) # 최소 공배수(LCM) 계산

