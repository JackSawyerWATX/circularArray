class Node:

    def __init__(self, element, next=None):
        self.element = element
        self.next = next


def create_circular(array):
    head = Node(array[0])
    tail = head

    for i in range(1, len(array)):
        new = Node(array[i])
        tail.next = new
        tail = new
    tail.next = head
    return head


def circular_printer(head):
    temp = head

    while temp.next is not head:
        print(temp.element)
        temp = temp.next
    print(temp.element)


def create(array):
    head = Node(array[0])
    tail = head

    for i in range(1, len(array)):
        new = Node(array[i])
        tail.next = new
        tail = new
    return head


def printer(head):
    temp = head

    while temp is not None:
        print(temp.element)
        temp = temp.next


def merger(circular, normal):
    circular_temp = circular
    normal_temp = normal

    while circular_temp.next is not circular:
        circular_temp = circular_temp.next
    temp = circular_temp
    temp.next = normal_temp

    while normal_temp.next is not None:
        normal_temp = normal_temp.next
    normal_temp.next = circular

    return circular


array_1 = (1, 2, 3)
array_2 = (4, 5)

circular_head = create_circular(array_1)
normal_head = create(array_2)
new_head = merger(circular_head, normal_head)
circular_printer(new_head)