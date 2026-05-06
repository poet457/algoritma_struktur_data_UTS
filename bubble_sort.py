def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar elemen
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
hasil = bubble_sort(data.copy())

print("Data sebelum sorting:", data)
print("Data setelah Bubble Sort:", hasil)