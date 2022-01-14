# 삽입(1) - 삽입(2) - 삽입(3) - 삭제() - 삽입(4) - 삽입(5) - 삭제()
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
queue.append(5)
queue.popleft()

print(queue) # 들어온 순서대로
queue.reverse()
print(queue) # 최신 삽입 순서대로