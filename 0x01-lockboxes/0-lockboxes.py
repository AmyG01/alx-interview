#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    keys = [0]  # Initial keys (starting with the first box)
    visited = set()

    while keys:
        current_box = keys.pop()
        if current_box not in visited:
            visited.add(current_box)
            keys.extend(boxes[current_box])

    return len(visited) == n

# Example usage:
if __name__ == "__main__":
    # Example boxes
    boxes = [[1], [2], [3], []]
    result = canUnlockAll(boxes)
    print(result)  # Output: True
