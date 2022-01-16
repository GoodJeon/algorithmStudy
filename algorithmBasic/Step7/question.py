n, k = map(int, input().split()) # N과 K를 입력   
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A < B
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # 원소 교체
    else:
        break

print(sum(a)) # 배열 a의 모든 원소 출력