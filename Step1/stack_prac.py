# 삽입(1) - 삽입(2) - 삽입(3) - 삭제() - 삭제() - 삽입(4) - 삽입(5) - 삭제
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.pop()
stack.append(4)
stack.append(5)
stack.pop()

print(stack[::-1]) # 입구 쪽 원소부터 출력
print(stack) # 안쪽 원소부터 출력