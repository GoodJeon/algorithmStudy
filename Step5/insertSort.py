# 삽입 정렬
# : 처리되지 않은 데이터를 골라 적절한 위치에 삽입
# : 선택 정렬에 비해 난이도가 높지만, 더 효율적으로 동작

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터가 왼쪽에 있다면 
            break # 그 위치에 멈춤

print(array)

# 시간 복잡도 = O(N^2)
# : 선택 정렬과 같이 반복문이 두 번 중첩 사용
# 만약 현재 리스트의 데이터가 정렬되어있다면,
# 최선의 경우 O(N)의 시간 복잡도를 가진다.

# array2 = list(range(0,10))

# for i in range(1, len(array2)):
#     for j in range(i, 0, -1):
#         # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
#         if array2[j] < array2[j - 1]: # 한 칸씩 왼쪽으로 이동
#             array2[j], array2[j - 1] = array2[j - 1], array2[j]
#         else: # 자기보다 작은 데이터가 왼쪽에 있다면 
#             break # 그 위치에 멈춤

# print(array2)
