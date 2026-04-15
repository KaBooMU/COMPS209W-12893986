
from __future__ import annotations


class MaxHeap:

    def __init__(self) -> None:
        self.heap: list[int] = []

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> int | None:
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index: int) -> None:
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def display(self) -> None:
        print("Heap:", self.heap)


def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr: list[int]) -> None:
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        # Move current maximum to its final sorted position.
        arr[i], arr[0] = arr[0], arr[i]
        # Restore the heap property on the reduced heap.
        heapify(arr, i, 0)


def main() -> None:
    print("Max Heap Demonstration")
    heap = MaxHeap()
    values = [45, 20, 14, 12, 31, 7, 11, 13, 7]

    for value in values:
        print(f"Inserting {value} into heap...")
        heap.insert(value)
        heap.display()

    print("\nExtract max value:", heap.extract_max())
    heap.display()

    print("\nMax Heap Demonstration")
    numbers = [34, 12, 56, 78, 23, 9, 45, 1]
    print("Original list:", numbers)
    heap_sort(numbers)
    print("Sorted list:", numbers)


if __name__ == "__main__":
    main()
