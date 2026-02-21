# Astral-Covenant

<p align="center">
  <img src="https://via.placeholder.com/600x200?text=Astral-Covenant+Logo" alt="Astral-Covenant Logo" width="600">
</p>

<p align="center">
  <i>"Di antara retakan realitas dan debu bintang yang memudar, sebuah perjanjian kuno menunggu untuk dihidupkan kembali. Terikat oleh takdir, sang pengembara harus menenun kekuatan astral untuk memulihkan keseimbangan yang hancur."</i>
</p>

---

## 🌌 Overview

**Astral-Covenant** adalah sebuah RPG (Role-Playing Game) berbasis teks yang dikembangkan dengan Python. Game ini menggabungkan mekanisme strategi battle yang mendalam, sistem manajemen Servant yang unik, serta eksplorasi dunia fantasi yang misterius. Pemain akan berperan sebagai _Covenant Binder_ yang berpetualang melewati berbagai area berbahaya untuk mengumpulkan kekuatan dan mengungkap rahasia Astral.

<p align="center">
  <img src="https://via.placeholder.com/800x450?text=Gameplay+Screenshot+Placeholder" alt="Gameplay Screenshot">
  <br>
  <i>Eksplorasi dan pertempuran taktis dalam dunia Astral.</i>
</p>

---

## 🛡️ Key Features

### ⚔️ Tactical Battle System

Sistem pertarungan berbasis giliran (turn-based) yang menuntut strategi matang. Kelola **Mana** Anda dengan bijak, gunakan skill unik Servant, dan perhatikan status efek seperti _Burn_, _Poison_, atau _Stun_ yang dapat membalikkan keadaan dalam sekejap.

### 👥 Servant Management

Anda tidak bertarung sendirian. Rekrut dan kembangkan **Servants**—makhluk astral yang memiliki kemampuan khusus. Bangun ikatan (_Bond_) dengan mereka untuk meningkatkan efisiensi transfer Mana dan membuka potensi tersembunyi selama pertempuran.

### 🗺️ Area Exploration

Jelajahi berbagai wilayah dari kota yang tenang hingga dungeon yang mencekam. Setiap area memiliki ekosistem musuh tersendiri dan tantangan yang unik, memberikan pengalaman perkembangan level yang dinamis.

---

## 📂 Project Structure

```text
Astral-Covenant/
├── core/                # Jantung permainan (Entitas & Logika Dasar)
│   ├── player.py        # Logika karakter utama, statistik, dan progresi EXP.
│   ├── enemy.py         # Definisi AI musuh dan perilaku dasar.
│   ├── servant.py       # Sistem pendukung tempur dan mekanisme ikatan (Bond).
│   └── status.py        # Manajemen status effect dan buff/debuff.
├── data/                # Database statis permainan
│   ├── areas.json       # Daftar lokasi dan monster yang menghuninya.
│   ├── enemies.json     # Blueprint statistik untuk setiap jenis monster.
│   └── servants.json    # Data dasar untuk rekan astral pemain.
├── systems/             # Mekanik utama permainan
│   ├── battle.py        # Engine pertarungan, kalkulasi damage, dan turn logic.
│   ├── skills.py        # Definisi kemampuan aktif dan pasif.
│   ├── save_load.py     # Sistem persistensi data pemain.
│   └── town.py          # Hub utama untuk istirahat dan persiapan.
├── utils/               # Fungsi pembantu dan utilitas sistem.
└── main.py              # Entry point utama untuk menjalankan game.
```

---

## 🚀 Installation & Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/username/Astral-Covenant.git
   cd Astral-Covenant
   ```

2. **Requirements**
   Pastikan Anda telah menginstal **Python 3.8+**. Tidak ada dependensi eksternal yang diperlukan untuk game inti.

3. **Run the Game**
   ```bash
   python main.py
   ```

---

## 🎮 Gameplay Controls

Game ini menggunakan input berbasis teks. Gunakan angka atau tombol yang sesuai dengan menu yang muncul di layar.

| Action             | Control (Input)     | Description                                        |
| :----------------- | :------------------ | :------------------------------------------------- |
| **Menu Selection** | `1`, `2`, `3`, etc. | Memilih opsi di menu utama atau menu battle.       |
| **Attack**         | `1` (Battle)        | Melakukan serangan fisik dasar.                    |
| **Servant Skill**  | `2` (Battle)        | Mengaktifkan skill khusus dari Servant yang aktif. |
| **Confirm / Next** | `Enter`             | Melanjutkan dialog atau teks narasi.               |
| **Cancel / No**    | `N`                 | Membatalkan pilihan atau menutup dialog tertentu.  |

---




