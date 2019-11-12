""" Contains the functions for sorting implementation of lab 6
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

def selection_sort(arr):
    count = 0
    for i in range(len(arr) - 1):
        max_idx = 0
        for j in range(1, len(arr) - i):
            count += 1
            if arr[max_idx] <= arr[j]:
                max_idx = j
        arr[len(arr) - 1 - i], arr[max_idx] = arr[max_idx], arr[len(arr)- 1 - i]
    return arr, count
    

def bubble_sort(arr):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count

def insertion_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            count += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr, count

# print(selection_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))
# print(bubble_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))
# print(insertion_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))

def merge_sort(arr):
    pass

def quick_sort(arr):
    pass

def heap_sort(arr):
    """build max heap
    - dequeue (del func) items from the max_heap
    - prepend the dequeued item to the sorted part of the array
    - repeat 2 and 3 till youre done
    """
    max_heapify(arr)
    for i in range(len(arr) - 1):
        dequeue(arr, len(arr) - 1 - i)
    return arr

def max_heapify(arr):
    """ Turns an array into a max heap
    Args:
    arr (list) : a list of int
    """
    parent = ((len(arr) - 1) - 1 ) // 2
    while parent >= 0:
        shift_down(arr, parent)
        parent -= 1
    return 
    
def dequeue(arr, pop_idx):
    """pop the minimum valued item from the min heap
    Args:
    arr (list) : a list of int
    Return:
    int : the smallest integer value in the min heap
    Raises:
    IndexError : When the heap is empty or None.
    """
    if arr is None or len(arr) == 0:
        raise IndexError('Heap is Empty!')
    if len(arr) == 1:
        return arr.pop()
    max_item = arr[0]
    last_item = arr[pop_idx]
    arr[0] = last_item
    arr[pop_idx] = max_item
    shift_down(arr, 0, pop_idx - 1)

def shift_down(arr, i, end=None):
    """ Shift down an item in the list to keep the max heap order
    Args:
    arr (list) : a list of int
    i (int) : the index of the item of interest
    """
    length = len(arr)
    if end is None:
        end = length - 1
    max_idx = index_maxchild(arr, i, end)
    if max_idx < 0:
        return None
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return shift_down(arr, max_idx, end)

def index_maxchild(arr, i, end):
    """ Computes the index of the child node with a maximum key value
    Args:
    arr (list) : A list of int
    i (int) : index of the node
    end (int) : the last index of the heap
    Returns:
    int : the index of the child node with minimum key value, or -1 if the 
          children are not bigger than the parent or if both children don't
          exist.
    """
    ileft = 2 * i + 1
    iright = 2 * i + 2
    if (ileft > end or arr[i] >= arr[ileft])\
    and (iright > end or arr[i] >= arr[iright]):
        return -1
    if iright > end or arr[ileft] >= arr[iright]:
        return ileft
    return iright

# print(merge_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))
# print(quick_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))
print(heap_sort([19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]))

""" 
    Random array [19, 4, 1, 3, 5, 7, 5, 6, 2, 8, 10, 9]
                    19
                   /  \
                  4    1
                / \    / \
               3  5    7  5
              /\  /\  /
             6 2 8 10 9
"""