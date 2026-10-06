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
# 算法二：选择排序
def selection_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 记录未排序部分最小值的索引
        min_idx = i
        # 在未排序部分寻找更小的值
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # 将找到的最小值与未排序部分的第一个元素交换位置
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# 输入与上面相同的10个随机数
numbers2 = [55, 23, 89, 12, 7, 45, 98, 34, 67, 2]
print("原始数组:", numbers2)
sorted_numbers2 = selection_sort(numbers2)
print("选择排序后:", sorted_numbers2)