# 🐍 Snake Game

<div align="center">

**Aplikasi permainan Snake berbasis desktop dengan PyQt5**

</div>

## 📋 Deskripsi Proyek

**Snake Game** adalah aplikasi permainan klasik Snake berbasis desktop yang dikembangkan menggunakan PyQt5 untuk antarmuka grafis. Proyek ini menghadirkan pengalaman bermain Snake modern dengan visual yang menarik, kontrol responsif, dan sistem peningkatan kecepatan seiring bertambahnya skor.

Permainan Snake dimainkan di papan 20x20. Pemain mengontrol ular untuk memakan makanan yang muncul secara acak. Setiap kali ular memakan makanan, panjang ular bertambah dan skor meningkat. Permainan berakhir ketika ular menabrak dinding atau tubuhnya sendiri.

Fitur utama aplikasi ini:
- Gameplay Klasik: Mekanisme Snake tradisional dengan kontrol panah
- Visual Menarik: Ular dengan kepala dan badan yang dibedakan, mata ular yang mengikuti arah
- Sistem Skor & Kecepatan: Skor bertambah setiap makan, kecepatan meningkat secara progresif
- Kontrol Lengkap: Tombol Mulai, Jeda, Reset, dan kontrol keyboard (panah, spasi, R)
- Tampilan Modern: Desain gelap dengan warna yang kontras dan elemen rounded

## 📑 Daftar Isi

- [Deskripsi Proyek](#-deskripsi-proyek)
- [Latar Belakang](#-latar-belakang)
- [Fitur Utama](#-fitur-utama)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Cara Penggunaan](#-cara-penggunaan)
- [Peran Developer](#-peran-developer)
- [Pembelajaran dari Proyek](#-pembelajaran-dari-proyek-lessons-learned)
- [Ucapan Terima Kasih](#-ucapan-terima-kasih)

## 🎯 Latar Belakang

Proyek ini dibuat untuk mengembangkan keterampilan dalam:

- **Pengembangan GUI dengan PyQt5**: Mempelajari custom widget, QPainter untuk rendering kustom, dan event handling
- **Game Loop & Timer**: Implementasi game loop dengan QTimer untuk pergerakan ular yang halus
- **Real-time Rendering**: Menggambar elemen game (ular, makanan, grid) secara dinamis dengan QPainter
- **Event-Driven Programming**: Menangani input keyboard dan tombol UI secara simultan
- **State Management**: Mengelola status permainan (berjalan, jeda, game over) dengan baik

Kebutuhan yang melatarbelakangi proyek ini:
- **Menghadirkan game klasik** dengan sentuhan visual modern
- **Pembelajaran tentang custom painting** di PyQt5 dengan QPainter
- **Implementasi game loop** yang efisien dan responsif
- **Pengembangan portofolio** untuk menunjukkan kemampuan Python dan PyQt5

## 🌟 Fitur Utama

### 🎮 **Gameplay Klasik dengan Sentuhan Modern**

| Fitur | Deskripsi |
|-------|-----------|
| **Papan 20x20** | Ukuran papan yang optimal untuk gameplay menantang |
| **Makanan Bulat** | Makanan berbentuk lingkaran merah dengan posisi acak |
| **Ular Bertubuh** | Kepala hijau terang dengan mata, badan hijau gelap |
| **Mata Ular** | Mata putih yang mengikuti arah gerakan ular |
| **Grid Halus** | Garis border halus sebagai panduan visual |

### ⚡ **Sistem Skor & Kecepatan Dinamis**

| Komponen | Deskripsi |
|----------|-----------|
| **Skor per Makanan** | +10 poin setiap kali ular memakan makanan |
| **Peningkatan Kecepatan** | Kecepatan bertambah setiap 10 poin (2 kali makan) |
| **Kecepatan Awal** | 150ms per gerakan |
| **Kecepatan Minimum** | 50ms (batas maksimal kecepatan) |
| **Inkrement Kecepatan** | 5ms per 10 poin |

### 🎮 **Kontrol Permainan**

| Tombol / Keyboard | Fungsi |
|-------------------|--------|
| **Mulai** | Memulai permainan baru atau melanjutkan setelah game over |
| **Jeda / Lanjut** | Menghentikan sementara atau melanjutkan permainan |
| **Reset** | Mereset permainan ke kondisi awal |
| **↑ ↓ ← →** | Menggerakkan ular (panah keyboard) |
| **Spasi** | Jeda / lanjutkan permainan |
| **R** | Reset permainan |

### 🎨 **Visual & Antarmuka**

| Komponen | Deskripsi |
|----------|-----------|
| **Tema Gelap** | Background hitam (#1A1A1A) dengan kontras tinggi |
| **Papan** | Area abu-abu gelap dengan border rounded |
| **Skor** | Warna kuning emas dengan font besar |
| **Game Over Overlay** | Popup semi-transparan dengan skor akhir |
| **Tombol** | Efek hover dan pressed untuk umpan balik visual |

### 🧠 **Mekanisme Permainan**

| Mekanisme | Implementasi |
|-----------|--------------|
| **Pergerakan** | Ular bergerak otomatis dengan interval timer |
| **Tabrakan Dinding** | Game over jika kepala menyentuh batas papan |
| **Tabrakan Tubuh** | Game over jika kepala menyentuh tubuh sendiri |
| **Makanan** | Muncul di posisi acak yang tidak ditempati ular |
| **Pertumbuhan** | Panjang ular bertambah setelah memakan makanan |

## 🛠️ Teknologi yang Digunakan

### Core Technologies

| Teknologi | Fungsi | Alasan Penggunaan |
|-----------|--------|-------------------|
| **Python 3.7+** | Bahasa pemrograman utama | Mudah dipelajari, library melimpah |
| **PyQt5** | Framework GUI | Aplikasi desktop profesional, custom painting |
| **PyQt5.QtCore** | Timer dan event | QTimer untuk game loop, Qt.Key untuk keyboard |
| **PyQt5.QtGui** | Rendering | QPainter, QBrush, QPen, QColor untuk drawing |

### Library yang Digunakan

| Library | Fungsi | Penggunaan |
|---------|--------|------------|
| **PyQt5.QtWidgets** | Widget GUI | QMainWindow, QPushButton, QLabel |
| **PyQt5.QtCore** | Core functionality | QTimer, Qt.Key, QRect |
| **PyQt5.QtGui** | Graphics | QPainter, QBrush, QColor, QPen |
| **random** | Randomization | Posisi makanan acak |
| **sys** | System | Argumen command line, exit aplikasi |

### Penjelasan File

#### File Utama

| File | Fungsi |
|------|--------|
| **main.py** | Entry point aplikasi. Menginisialisasi QApplication dan menampilkan jendela utama. |

#### Package `game/` (Logika Permainan)

| File | Fungsi |
|------|--------|
| **game/snake.py** | Kelas `Snake` untuk merepresentasikan ular. Menangani pergerakan, pertumbuhan, pengecekan tabrakan, dan perubahan arah dengan pencegahan berbalik 180°. |
| **game/food.py** | Kelas `Food` untuk merepresentasikan makanan. Menangani respawn di posisi acak yang tidak bertabrakan dengan tubuh ular. |
| **game/game_logic.py** | Kelas `GameLogic` untuk logika utama. Menghubungkan snake dan food, menangani update game, skor, dan reset. |

#### Package `ui/` (Antarmuka Pengguna)

| File | Fungsi |
|------|--------|
| **ui/main_window.py** | Kelas `SnakeWindow` (QMainWindow) dan `GameCanvas` (QWidget untuk custom painting). Menampilkan papan, ular, makanan, skor, dan kontrol. Menangani input keyboard dan tombol UI. |
| **ui/styles.py** | Fungsi `apply_styles()` yang mengembalikan stylesheet CSS untuk semua widget (warna, font, efek hover). |

#### Package `utils/` (Utilitas)

| File | Fungsi |
|------|--------|
| **utils/constants.py** | Konstanta warna (COLORS), ukuran (WINDOW_WIDTH, BOARD_SIZE, CELL_SIZE), pengaturan game (INITIAL_SPEED, SPEED_INCREMENT, MIN_SPEED), dan arah (UP, DOWN, LEFT, RIGHT, OPPOSITE). |

## 🎮 Cara Penggunaan

### Memulai Permainan

Setelah aplikasi dijalankan, Anda akan melihat jendela utama dengan:

| Komponen | Fungsi |
|----------|--------|
| **Title** | "SNAKE GAME" di bagian atas |
| **Skor** | Menampilkan skor saat ini (awal: 0) |
| **Papan** | Area grid 20x20 tempat permainan berlangsung |
| **Tombol Mulai** | Memulai permainan |
| **Tombol Jeda** | Menjeda/melanjutkan permainan |
| **Tombol Reset** | Mereset permainan ke awal |
| **Info** | Petunjuk kontrol keyboard |

### Langkah-langkah Bermain

1. **Mulai Permainan**
   - Klik tombol **"Mulai"** atau tekan **Spasi**
   - Ular akan mulai bergerak ke kanan secara otomatis

2. **Mengontrol Ular**
   - Gunakan **tombol panah** (↑, ↓, ←, →) untuk mengubah arah
   - Ular tidak bisa berbalik 180° (tidak bisa langsung ke kiri jika ke kanan)

3. **Memakan Makanan**
   - Arahkan kepala ular ke makanan berbentuk lingkaran merah
   - Setiap kali makan, skor bertambah 10 dan panjang ular bertambah

4. **Peningkatan Kecepatan**
   - Setiap 10 poin (2 kali makan), kecepatan ular meningkat
   - Semakin tinggi skor, semakin cepat pergerakan ular

5. **Menjeda Permainan**
   - Klik **"Jeda"** atau tekan **Spasi** untuk menjeda
   - Klik **"Lanjut"** atau tekan **Spasi** lagi untuk melanjutkan

6. **Game Over**
   - Permainan berakhir jika ular menabrak dinding atau tubuh sendiri
   - Popup "GAME OVER!" menampilkan skor akhir
   - Klik **"Mulai"** untuk bermain lagi

### Kontrol Lengkap

| Aksi | Tombol |
|------|--------|
| Mulai / Lanjut | **Mulai** (tombol) atau **Spasi** (keyboard) |
| Jeda | **Jeda** (tombol) atau **Spasi** (keyboard) |
| Reset | **Reset** (tombol) atau **R** (keyboard) |
| Gerak ke Atas | **↑** (panah atas) |
| Gerak ke Bawah | **↓** (panah bawah) |
| Gerak ke Kiri | **←** (panah kiri) |
| Gerak ke Kanan | **→** (panah kanan) |

### Aturan Permainan

| Aturan | Penjelasan |
|--------|------------|
| **Arah Awal** | Ular bergerak ke kanan saat permainan dimulai |
| **Posisi Awal** | Ular dimulai di tengah papan (10,10) dengan panjang 1 |
| **Dilarang Berbalik** | Ular tidak bisa langsung berbalik arah 180° |
| **Makanan** | Muncul di posisi acak yang tidak ditempati ular |
| **Skor** | +10 setiap makan |
| **Game Over** | Tabrakan dinding atau tabrakan tubuh sendiri |

## 👨‍💻 Peran Developer

### Peran dalam Proyek

| Area | Kontribusi |
|------|------------|
| **Perencanaan** | Merancang fitur-fitur game Snake klasik dengan papan 20x20 |
| **Desain Arsitektur** | Mendesain struktur folder modular (game/, ui/, utils/) |
| **Pengembangan Game Logic** | Implementasi kelas `Snake` dan `Food` dengan aturan lengkap |
| **Pengembangan Rendering** | Custom painting dengan QPainter (ular, makanan, grid, mata) |
| **Pengembangan GUI** | Membangun antarmuka dengan PyQt5 (tombol, label, layout) |
| **UI/UX Design** | Mendesain tampilan modern dengan tema gelap, efek hover |
| **Game Loop** | Implementasi QTimer untuk pergerakan yang halus |
| **State Management** | Manajemen status game (running, paused, game over) |
| **Control System** | Keyboard dan tombol UI yang bekerja simultan |

### Fokus Pengembangan

1. **Fungsionalitas Inti**
   - Pergerakan ular yang responsif
   - Sistem tabrakan yang akurat (dinding & tubuh)
   - Posisi makanan yang tidak bertabrakan dengan ular

2. **User Experience**
   - Visual menarik dengan kepala/badan ular berbeda
   - Mata ular yang mengikuti arah gerakan
   - Popup game over dengan skor akhir
   - Informasi kontrol yang jelas

3. **Dynamic Difficulty**
   - Peningkatan kecepatan seiring skor
   - Batas kecepatan minimum (50ms)
   - Inkrement 5ms per 10 poin

4. **Arsitektur Modular**
   - Pemisahan UI, logika game, dan rendering
   - Konstanta terpusat di `constants.py`
   - Stylesheet terpisah untuk kemudahan kustomisasi

## 📚 Pembelajaran dari Proyek (Lessons Learned)

### Keterampilan Teknis yang Diperoleh

1. **PyQt5 Custom Widget dengan QPainter**
   - Menggambar bentuk (rectangle, ellipse) dengan QPainter
   - Mengatur brush dan pen untuk warna dan border
   - Render ulang dengan `update()` dan `paintEvent`

2. **Game Loop dengan QTimer**
   - Implementasi game loop non-blocking
   - Penjadwalan interval dengan `timer.start()`
   - Penghentian dan restart timer untuk jeda

3. **Event Handling**
   - Keyboard events dengan `keyPressEvent`
   - Button clicks dengan `clicked.connect`
   - Fokus keyboard dengan `setFocusPolicy`

4. **State Management**
   - Status game (berjalan, jeda, game over)
   - Flag `grow_flag` untuk pertumbuhan ular
   - Pencegahan arah berlawanan dengan dictionary `OPPOSITE`

5. **Collision Detection**
   - Deteksi tabrakan dinding (batas BOARD_SIZE)
   - Deteksi tabrakan tubuh (`head in body[1:]`)

6. **Randomized Positioning**
   - Respawn makanan di posisi tidak bertabrakan dengan ular
   - Loop while sampai menemukan posisi valid

### Soft Skills yang Dikembangkan

#### 1. **Problem Decomposition**
- Memecah game menjadi komponen: snake, food, game logic, UI, rendering
- Memisahkan logika permainan dari antarmuka
- Mendesain hirarki kelas yang jelas

#### 2. **Real-time Rendering**
- Memahami siklus paint event di Qt
- Memisahkan logika dari rendering untuk performa optimal

#### 3. **User Experience Design**
- Mendesain antarmuka yang intuitif
- Memberikan visual feedback (hover, pressed)
- Informasi kontrol yang jelas

#### 4. **Defensive Programming**
- Validasi input arah (mencegah berbalik 180°)
- Pengecekan posisi makanan yang valid
- Flag `grow_flag` untuk pertumbuhan yang tepat

## 🙏 Ucapan Terima Kasih

### Sumber Daya dan Referensi

#### Dokumentasi Resmi
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/) - Framework GUI
- [Qt for Python](https://doc.qt.io/qtforpython/) - Dokumentasi Qt untuk Python
- [Python Documentation](https://docs.python.org/3/) - Bahasa pemrograman

#### Tutorial dan Artikel
- **PyQt5 QPainter Tutorial** - Untuk custom painting dan rendering
- **Game Loop Implementation** - Konsep game loop dengan timer
- **Snake Game Mechanics** - Aturan klasik permainan Snake

#### Tools yang Membantu
- **Visual Studio Code** - Editor kode
- **Qt Designer** - (Referensi) Untuk desain UI visual

### Inspirasi Proyek
- **Game Snake klasik (Nokia)** - Mekanisme dasar permainan
- **Modern Snake Games** - Visual dan efek modern
- **Proyek Tic Tac Toe & Othello** - Format README yang terstruktur

---

<div align="center">

**⭐ Jika proyek ini menarik atau bermanfaat, berikan bintang! ⭐**

**"Snake: Game sederhana yang mengajarkan kompleksitas state management dan real-time rendering"**

</div>