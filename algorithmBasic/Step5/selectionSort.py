# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 앞쪽의 원소가 가장 작은 원소라고 가정
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            # 현재 작업 중인 값보다 작다면
            min_index = j
            # 가장작은 인덱스는 j가 된다.
    array[i], array[min_index] = array[min_index], array[i]
    # 자리를 바꿔준다.

print(array)

# 시간 복잡도
# 전체 연산 횟수
# : N + (N - 1) + (N - 2) + ... + 2
# = (N^2 + N - 2)/2
# 빅오 표기법 = O(N^2)