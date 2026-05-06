# algoritma_struktur_data_UTS
Jawaban UTS
2. Berikan penjelasan, contoh penggunaan

A. Bubble Sort

# Pengertian:

Bubble Sort adalah algoritma sorting sederhana yang bekerja dengan cara membandingkan dua elemen yang bersebelahan, lalu menukarnya jika urutannya salah. Proses ini diulang sampai seluruh data terurut.

# Langkah Kerja:

Contoh data:
3, 8, 4]


# Iterasi:

* Bandingkan 5 dan 3 → tukar → [3,5,8,4]
* Bandingkan 5 dan 8 → tidak tukar
* Bandingkan 8 dan 4 → tukar → [3,5,4,8]


B. Binary Insertion Sort

# Pengertian:

Binary Insertion Sort adalah pengembangan dari Insertion Sort dengan Binary Search untuk mencari posisi penyisipan lebih cepat.

# Cara Kerja:

Data:
[5, 3, 8, 4]


# Proses:

* Ambil 3 → cari posisi dengan binary search → letakkan sebelum 5
  [3,5,8,4]

* Ambil 8 → posisi benar
  [3,5,8,4]

* Ambil 4 → binary search posisi antara 3 dan 5
  [3,4,5,8]

# Contoh Penggunaan:

data = [5, 3, 8, 4]
print(binary_insertion_sort(data))

Output:
[3, 4, 5, 8]
