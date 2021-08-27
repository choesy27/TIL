class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1

        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!