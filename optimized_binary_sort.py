def binary_search(arr, item, low, high):
    while low <= high:
        mid = (low + high) // 2

        if item == arr[mid]:
            return mid + 1
        elif item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low


def optimized_binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Cari posisi dengan binary search
        pos = binary_search(arr, key, 0, i - 1)

        # Geser manual tanpa slicing berlebih
        j = i - 1
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1

        arr[pos] = key

    return arr


# Contoh penggunaan
data = [37, 23, 0, 17, 12, 72, 31]
hasil = optimized_binary_insertion_sort(data.copy())

print("Data sebelum sorting:", data)
print("Data setelah Optimized Binary Insertion Sort:", hasil)