# Analisis Soal Nomor 1

## Berikut adalah analisis Algoritma Bubble Sort dan Algoritma Insertion Sort untuk kasus terburuk (worst case), kasus terbaik (best case), dan kasus rata-rata (average case):

### Analisis Algoritma Bubble Sort:

1. Worst case:
	- Kompleksitas waktu: O(n^2)
	- Terjadi ketika list dalam keadaan terbalik, sehingga setiap elemen harus melakukan penukaran dengan elemen-elemen sebelumnya pada setiap iterasi.
	- Jumlah iterasi adalah n-1 pada iterasi pertama, n-2 pada iterasi kedua, dan seterusnya hingga 1 pada iterasi terakhir.
	- Total jumlah iterasi adalah (n-1) + (n-2) + ... + 1 = (n * (n-1)) / 2.
	- Oleh karena itu, kompleksitas waktu adalah O(n^2).
2. Best case:
	- Kompleksitas waktu: O(n)
	- Terjadi ketika list sudah terurut dengan benar sejak awal.
	- Pada setiap iterasi, tidak ada pertukaran elemen yang dilakukan karena semua elemen sudah dalam urutan yang benar.
	- Jumlah iterasi adalah n-1, di mana n adalah jumlah elemen dalam list.
	- Oleh karena itu, kompleksitas waktu adalah O(n).
3. Average case:
	- Kompleksitas waktu: O(n^2)
	- Dalam kasus rata-rata, kita mengasumsikan bahwa setiap permutasi elemen muncul dengan probabilitas yang sama.
	- Untuk setiap elemen, ada 50% kemungkinan perlu dilakukan penukaran dengan elemen sebelumnya pada setiap iterasi.
	- Jumlah rata-rata iterasi adalah sekitar (n * (n-1)) / 4.
	- Oleh karena itu, kompleksitas waktu adalah O(n^2).

### Analisis Algoritma Insertion Sort:

1. Worst case:
	- Kompleksitas waktu: O(n^2)
	- Terjadi ketika list dalam keadaan terbalik, sehingga setiap elemen harus digeser ke posisi yang benar pada setiap iterasi.
	- Pada setiap iterasi, elemen saat ini harus dibandingkan dengan semua elemen sebelumnya dan digeser ke posisi yang benar jika diperlukan.
	- Jumlah iterasi adalah n-1 pada iterasi pertama, n-2 pada iterasi kedua, dan seterusnya hingga 1 pada iterasi terakhir.
	- Total jumlah iterasi adalah (n * (n-1)) / 2.
	- Oleh karena itu, kompleksitas waktu adalah O(n^2).
2. Best case:
	- Kompleksitas waktu: O(n)
	- Terjadi ketika list sudah terurut dengan benar sejak awal.
	- Pada setiap iterasi, elemen saat ini hanya perlu dibandingkan dengan elemen sebelumnya yang paling dekat yang tidak dalam urutan yang benar, dan tidak ada pergeseran yang dilakukan.
	- Jumlah iterasi adalah n-1, di mana n adalah jumlah elemen dalam list.
	- Oleh karena itu, kompleksitas waktu adalah O(n).
3. Average case:
	- Kompleksitas waktu: O(n^2)
	- Dalam kasus rata-rata, kita mengasumsikan bahwa setiap permutasi elemen muncul dengan probabilitas yang sama.
	- Jumlah rata-rata iterasi adalah sekitar (n * (n-1)) / 4.
	- Oleh karena itu, kompleksitas waktu adalah O(n^2).

# Analisis Soal Nomor 2

## Berikut adalah analisis Algoritma TSP dan Algoritma Dijkstra untuk kasus terburuk (worst case), kasus terbaik (best case), dan kasus rata-rata (average case):

1. Worst case:
    - Algoritma TSP (Brute Force): O(n!)
        Pada kasus terburuk, di mana n adalah jumlah simpul/graf, algoritma TSP (Brute Force) akan memeriksa semua kemungkinan permutasi simpul. Jumlah permutasi adalah n!, sehingga kompleksitas waktu menjadi faktorial dari jumlah simpul. Ini menghasilkan kompleksitas waktu yang sangat tinggi dan tidak efisien, terutama saat jumlah simpul meningkat.
    - Algoritma Dijkstra: O((V + E) log V)
        Pada kasus terburuk, di mana V adalah jumlah simpul dan E adalah jumlah tepi/graf, algoritma Dijkstra memiliki kompleksitas waktu sebanding dengan (V + E) log V. Ini terjadi ketika semua simpul dan tepi perlu diperiksa untuk menemukan jalur terpendek. Algoritma ini menggunakan heap untuk mempercepat pencarian jalur terpendek.
2. Best case:
    - Algoritma TSP (Brute Force): O(n!)
        Pada kasus terbaik, kompleksitas waktu algoritma TSP (Brute Force) tetap sama dengan worst case. Hal ini disebabkan karena algoritma ini secara eksplisit memeriksa semua kemungkinan permutasi simpul tanpa memperhitungkan urutan atau struktur graf. Oleh karena itu, tidak ada perbaikan pada kasus terbaik.
    - Algoritma Dijkstra: O((V + E) log V)
        Pada kasus terbaik, kompleksitas waktu algoritma Dijkstra tetap sama dengan worst case. Hal ini disebabkan karena algoritma ini harus memeriksa semua simpul dan tepi untuk menemukan jalur terpendek dari simpul awal ke semua simpul lainnya. Oleh karena itu, tidak ada perbaikan pada kasus terbaik.
3. Average case:
   - Algoritma TSP (Brute Force): O(n!)
        Pada kasus rata-rata, kompleksitas waktu algoritma TSP (Brute Force) tetap sama dengan worst case. Karena algoritma ini memeriksa semua kemungkinan permutasi simpul dengan probabilitas yang sama, tidak ada perbedaan dalam kompleksitas waktu rata-rata.
   - Algoritma Dijkstra: O((V + E) log V)
        Pada kasus rata-rata, kompleksitas waktu algoritma Dijkstra tetap sama dengan worst case. Algoritma ini memeriksa semua simpul dan tepi dalam graf dengan menggunakan heap untuk mencari jalur terpendek. Karena jumlah simpul dan tepi memiliki peran dalam kompleksitas waktu, tidak ada perbedaan yang signifikan dalam kasus rata-rata.

