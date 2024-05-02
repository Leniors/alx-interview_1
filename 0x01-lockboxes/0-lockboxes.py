#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

boxes = [[1], [2], [3], []]  # Boxes contain keys to the next box in sequence
print(canUnlockAll(boxes))  # Output: True
