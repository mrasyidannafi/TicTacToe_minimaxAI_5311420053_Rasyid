# Tic Tac Toe with Minimax Algorithm
![image](https://github.com/mrasyidannafi/TicTacToe_minimaxAI_5311420053_Rasyid/assets/149043860/968883b0-eedd-4833-a658-e81145d6dfae)



Kode di atas adalah implementasi permainan Tic-Tac-Toe dengan GUI menggunakan tkinter. Ini memungkinkan pemain bermain melawan komputer yang menggunakan algoritma minimax untuk membuat keputusan terbaik.



**Algoritma Minimax:**


Algoritma Minimax adalah algoritma yang digunakan oleh komputer (simbol "X") untuk membuat keputusan terbaik dalam permainan Tic-Tac-Toe. Algoritma ini bekerja dengan cara berikut:


1. Pencarian Rekursif: Algoritma Minimax melakukan pencarian rekursif dalam pohon permainan, mempertimbangkan semua kemungkinan gerakan yang mungkin dilakukan oleh pemain "X" (komputer) dan pemain "O" (manusia).


2. Penilaian Skor: Setiap simpul dalam pohon permainan dinilai dengan skor. Skor positif (+1) menunjukkan bahwa pemain "X" memiliki keunggulan, skor negatif (-1) menunjukkan keunggulan pemain "O", dan skor nol menunjukkan hasil imbang.


3. Maksimisasi dan Minimisasi: Algoritma Minimax bekerja dengan prinsip bahwa pemain "X" mencoba untuk memaksimalkan skornya, sedangkan pemain "O" mencoba untuk meminimalkan skornya. Dalam setiap langkah rekursif, pemain "X" mencoba memilih gerakan yang memberikan skor maksimal, sementara pemain "O" mencoba memilih gerakan yang memberikan skor minimal.


4. Pohon Permainan: Algoritma Minimax membangun pohon permainan dengan semua kemungkinan langkah, kemudian menilai setiap simpul dalam pohon tersebut. Ini melibatkan pemanggilan fungsi minimax secara rekursif untuk setiap cabang dalam pohon.


5. Keputusan Terbaik: Setelah pohon permainan selesai dieksplorasi, komputer "X" akan memilih gerakan terbaik berdasarkan skor yang diberikan oleh algoritma Minimax.



Jadi, algoritma minimax akan mencari semua kemungkinan gerakan yang mungkin oleh komputer, mengevaluasi skor untuk setiap gerakan, dan memilih gerakan terbaik yang akan diambil oleh komputer untuk mencoba memenangkan permainan.
