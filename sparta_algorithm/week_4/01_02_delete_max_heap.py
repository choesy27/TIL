class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소(원래 루트 노드)를 삭제한다. 마지막에 반환해야 하므로 저장해둔다.
    # 3. 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 비교해서 자신이 자식보다 크다면 자리를 바꿔준다.
    # 4. 자식 노드보다 부모 노드가 더 크거나 가장 바닥에 도달하지 않을 때까지 3번을 반복한다.
    # 5. 2번에서 제거한 원래 루트 노드를 반환한다.
    def delete(self):
        # 구현해보세요!
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            # 왼쪽 노드가 현재 이진 트리에 존재하고 max_index의 원소보다 크다면
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            # 오른쪽 노드가 현재 이진 트리에 존재하고 max_index의 원소보다 크다면
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 만약에 현재 위치한 원소가 가장 크다면
            if cur_index == max_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]