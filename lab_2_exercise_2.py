def sort(num):
    for item in range (1,len(num)):
        current_value = num[item]
        position = item
        while position > 0 and num[position-1] > current_value:
            num[position] = num[position-1]
            position -= 1
        num[position] = current_value
    return num

def bin_search(sorted_nums,sum_of_two,start,end):
    while start <= end:
        mid = (start + end) // 2
        if sorted_nums[mid] == sum_of_two:
            return mid
        if sorted_nums[mid] < sum_of_two:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def sum_of_three(numbers,P):
    if len(numbers) < 3 or len(numbers) > 1000:
        return False
    numbers = sort(numbers)
    n = len(numbers)
    for i in range(n-2):
        sum_of_two = P - numbers[i]
        for j in range(i+1,n-1):
            third_number = sum_of_two - numbers[j]
            found_index = bin_search(numbers,third_number,j + 1,n)
            if found_index != -1:
                return True

    return False


