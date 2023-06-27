import time

# Fungsi untuk menampilkan elemen list
def display_list(arr):
    print("List: ", end="")
    for i in arr:
        print(i, end=" ")
    print()

# Algoritma Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    print("Bubble Sort:")
    display_list(arr[:5]) # 5 iterasi pertama
    display_list(arr[-5:]) # 5 iterasi terakhir
    print("Waktu komputasi:", execution_time, "detik")
    print("Setelah pengurutan:")
    display_list(arr)
    print()

    # Analisis algoritma Bubble Sort
    print("Analisis Algoritma Bubble Sort:")
    print("Worst case: O(n^2)")
    print("Best case: O(n) jika list sudah terurut dengan benar")
    print("Average case: O(n^2)")
    print()

# Algoritma Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    print("Insertion Sort:")
    display_list(arr[:5]) # 5 iterasi pertama
    display_list(arr[-5:]) # 5 iterasi terakhir
    print("Waktu komputasi:", execution_time, "detik")
    print("Setelah pengurutan:")
    display_list(arr)
    print()

    # Analisis algoritma Insertion Sort
    print("Analisis Algoritma Insertion Sort:")
    print("Worst case: O(n^2)")
    print("Best case: O(n) jika list sudah terurut dengan benar")
    print("Average case: O(n^2)")
    print()

# List yang diberikan
arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

print("Sebelum pengurutan:")
display_list(arr)
print()

while True:
    print("Pilihan pengurutan:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == "1":
        bubble_sort(arr.copy())
        break
    elif choice == "2":
        insertion_sort(arr.copy())
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

