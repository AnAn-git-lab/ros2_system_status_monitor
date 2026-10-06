# 算法一：冒泡排序
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # 从头遍历到未排序的部分，如果当前元素大于下一个元素，则交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 假设输入的10个随机数
numbers = [55, 23, 89, 12, 7, 45, 98, 34, 67, 2]
print("原始数组:", numbers)
sorted_numbers = bubble_sort(numbers)
print("冒泡排序后:", sorted_numbers)