# Berikut adalah analisis algoritma Bubble Sort dan Insertion Sort untuk kasus terburuk (worst case), kasus terbaik (best case), dan kasus rata-rata (average case):

## Analisis Algoritma Bubble Sort:

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

## Analisis Algoritma Insertion Sort:

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