def merge_sort_nums(arr, left, right):
    if left >= right:
        return

    mid = int((left + right) / 2)

    arr = merge_sort_nums(arr, left, mid)
    arr = merge_sort_nums(arr, mid + 1, right)

    i = left
    j = mid + 1
    tmp = list()
    for step in range(0, right - left + 2):
        if j > right or (i < mid + 1 and arr[i] < arr[j]):
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    for step in range(0, right - left + 2):
        if arr[left + step] != tmp[step]:
            arr[left + step] = tmp[step]

    return arr


def merge_sort_strings(arr, left, right):
    if left >= right:
        return

    mid = int((left + right) / 2)

    arr = merge_sort_strings(arr, left, mid)
    arr = merge_sort_strings(arr, mid + 1, right)

    i = left
    j = mid + 1
    tmp = list()
    for step in range(0, right - left + 2):
        if j > right or (i < mid + 1 and arr[i].lower() < arr[j].lower()):
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    for step in range(0, right - left + 2):
        if arr[left + step].lower() != tmp[step].lower():
            arr[left + step] = tmp[step]

    return arr
