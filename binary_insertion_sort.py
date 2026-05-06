def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid

    return start


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i)

        # Geser elemen
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i+1:]

    return arr


# Contoh penggunaan
data = [37, 23, 0, 17, 12, 72, 31]
hasil = binary_insertion_sort(data.copy())

print("Data sebelum sorting:", data)
print("Data setelah Binary Insertion Sort:", hasil)