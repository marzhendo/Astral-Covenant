# Astral-Covenant

<p align="center"><pre>
   █████╗ ███████╗████████╗██████╗  █████╗ ██╗     
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
    ███████║███████╗   ██║   ██████╔╝███████║██║     
    ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║     
    ██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

██████╗  ██████╗ ██╗   ██╗███████╗███╗   ██╗ █████╗ ███╗   ██╗████████╗
██╔════╝ ██╔═══██╗██║   ██║██╔════╝████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
██║      ██║   ██║██║   ██║█████╗  ██╔██╗ ██║███████║██╔██╗ ██║   ██║   
██║      ██║   ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
╚██████╗ ╚██████╔╝ ╚████╔╝ ███████╗██║ ╚████║██║  ██║██║ ╚████║   ██║   
 ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝

             
</pre></p>

<p align="center">
  <i>"Di antara retakan realitas dan debu bintang yang memudar, sebuah perjanjian kuno menunggu untuk dihidupkan kembali. Terikat oleh takdir, sang pengembara harus menenun kekuatan astral untuk memulihkan keseimbangan yang hancur."</i>
</p>

---

## 🌌 Overview

**Astral-Covenant** adalah sebuah RPG (Role-Playing Game) berbasis teks yang dikembangkan dengan Python. Game ini menggabungkan mekanisme strategi battle yang mendalam, sistem manajemen Servant yang unik, serta eksplorasi dunia fantasi yang misterius. Pemain berperan sebagai _Covenant Binder_ — seseorang yang terpilih untuk mengikat ikatan dengan para roh heroik dari alam Astral.

---

## 🛡️ Key Features

### 🎬 Story & Opening Cinematic

Game dibuka dengan narasi teks bertik (_typewriter effect_) yang memperkenalkan lore dunia Astral-Covenant. Pemain akan merasakan kekalahan naratif sebelum akhirnya mengikat Covenant dengan Servant pertama mereka — disertai animasi pemanggilan (_summon animation_) yang unik untuk tiap Servant.

### ⚔️ Tactical Battle System

Sistem pertarungan berbasis giliran (turn-based) dengan 4 opsi aksi per giliran:

- **Attack** — Serangan fisik dasar ke target pilihan.
- **Command Servant Skill** — Aktifkan skill khusus Servant (dengan sistem cooldown dan biaya Mana).
- **Use Item** — Gunakan item dari inventory selama pertempuran.
- **Check Status** — Lihat status HP, Mana, dan efek aktif semua pihak.

Servant juga melakukan **auto-attack** setiap giliran jika skill-nya tidak dipakai.

### 💎 Mana Transfer System

Ketika Mana Servant tidak cukup untuk skill, Mana pemain dapat di-_transfer_ ke Servant — dengan **penalti efisiensi** yang berkurang seiring meningkatnya **Bond Level**. Bond yang lebih tinggi = transfer lebih hemat.

### 🌀 Status Effects

Lima efek status yang memengaruhi jalannya pertempuran:

| Status              | Efek                                  |
| :------------------ | :------------------------------------ |
| **Burn** 🔥         | DOT 5% Max HP per giliran             |
| **Poison** ☠️       | DOT 3 HP flat per giliran             |
| **Stun** ⚡         | Melewatkan giliran                    |
| **Defense Down** 🛡️ | Mengurangi pertahanan 30%             |
| **Astral Mark** ✦   | Meningkatkan damage yang diterima 15% |

Entity hanya dapat membawa **maksimal 2 status** secara bersamaan.

### 👥 Servant System

Tiga Servant unik yang bisa dipilih pada awal permainan:

| Servant               | HP  | ATK | DEF | Mana | Skill                           | Efek Skill                                        |
| :-------------------- | :-: | :-: | :-: | :--: | :------------------------------ | :------------------------------------------------ |
| **Artoria Pendragon** | 85  | 16  | 10  |  32  | Excalibur (cost 20, CD 3)       | AoE damage 1.4x · 30% chance Defense Down         |
| **Emiya**             | 75  | 17  |  8  |  36  | Broken Phantasm (cost 22, CD 3) | 2-4 random hits 0.9x · 25% chance Burn per hit    |
| **Mash Kyrielight**   | 100 | 12  | 15  |  40  | Lord Chaldeas (cost 18, CD 4)   | Cleanse Defense Down · Pulihkan 25% Max HP pemain |

Servant memiliki **sistem leveling sendiri** (EXP scaling `80 * level^1.5`) dan menerima 80% EXP dari kemenangan battle. Setiap level up meningkatkan Max HP +8, ATK +2, DEF +1, Max Mana +3.

### 🗺️ Area Exploration

Jelajahi area bebas dengan sistem _tile-step_ — setiap langkah memiliki **45% chance encounter**. Area mendukung pertarungan multi-musuh.

| Area                 | Rekomendasi Level | Musuh                                  |
| :------------------- | :---------------: | :------------------------------------- |
| **Whispering Woods** |      Lv 1–3       | Slime, Goblin, Wolf (bisa 2 sekaligus) |

### ⚔️ Dungeon System

Dungeon menawarkan tantangan linear berbasis **gelombang (wave)**. Tidak ada istirahat di dalam dungeon. Gelombang terakhir selalu berupa **miniboss**.

| Dungeon         | Rekomendasi | Waves                                                                               |
| :-------------- | :---------: | :---------------------------------------------------------------------------------- |
| **Shadow Rift** |    Lv 2+    | Wave 1: 2x Rift Slime → Wave 2: Goblin Raider + Wolf → Miniboss: Abyss Goblin Chief |

### 🎒 Inventory & Items

Pemain memulai dengan Potion x3 dan Mana Potion x2. Item dapat ditemukan sebagai loot pasca-pertempuran.

| Item            | Efek                  |
| :-------------- | :-------------------- |
| **Potion**      | Pulihkan 40% Max HP   |
| **Mana Potion** | Pulihkan 40% Max Mana |

### 💾 Save & Load System

Data game disimpan dalam format **JSON** di folder `saves/`. Semua data yang disimpan: stats pemain, inventory, gold, level, EXP, daftar Servant beserta bond, level, dan cooldown-nya.

---

## 📂 Project Structure

```text
Astral-Covenant/
├── core/                    # Base entity dan karakter utama
│   ├── entity.py            # [BASE CLASS] Base class untuk semua entitas (HP, Mana, status effects).
│   ├── player.py            # Karakter pemain: level, EXP, gold, inventory, servants.
│   ├── servant.py           # Servant: skill, cooldown, bond, sistem leveling sendiri.
│   ├── enemy.py             # Musuh: stats dan exp_reward.
│   └── status.py            # (Reserved) Manajemen tipe status effect.
│
├── data/                    # Data statis permainan (factory functions)
│   ├── areas.py             # Definisi area eksplorasi dan encounter function-nya.
│   ├── dungeons.py          # Definisi dungeon dan wave generator-nya.
│   ├── servants.py          # Factory function untuk membuat Artoria, Emiya, Mash.
│   └── enemies.py           # (Reserved) Data musuh tambahan.
│
├── systems/                 # Mekanik utama permainan
│   ├── battle.py            # Battle engine: turn logic, damage calc, status processing, battle log.
│   ├── skills.py            # Implementasi skill tiap Servant (artoria_skill, emiya_skill, mash_skill).
│   ├── items.py             # Logika penggunaan item (Potion, Mana Potion).
│   ├── area.py              # Loop eksplorasi area bebas dengan random encounter.
│   ├── dungeon.py           # Loop dungeon berbasis wave dengan miniboss di akhir.
│   ├── opening.py           # Alur cerita pembuka: prologue → kekalahan → pilih Servant → tutorial battle.
│   ├── save_load.py         # Serialisasi/deserialisasi data pemain ke/dari JSON.
│   └── town.py              # Hub utama: menu kota, istirahat, inventory, status, save.
│
├── ui/                      # Antarmuka visual
│   ├── title.py             # Layar judul ASCII art, intro cinematic (typewriter), main menu.
│   └── summon.py            # Animasi pemanggilan Servant yang unik per karakter (ASCII art + narasi).
│
├── utils/                   # Fungsi utilitas
│   ├── colors.py            # Konstanta warna ANSI (kelas C: RED, GREEN, BLUE, dst).
│   ├── ui.py                # HUD bar (HP/Mana), show_player_hud, clear screen.
│   └── helpers.py           # show_hud sederhana untuk tampilan di luar battle.
│
├── saves/                   # Folder save file (dibuat otomatis)
│   └── slot1.json           # Save file pemain (format JSON).
│
└── main.py                  # Entry point: title → cinematic → menu (New/Load/Exit).
```

---

## 🚀 Installation & Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/username/Astral-Covenant.git
   cd Astral-Covenant
   ```

2. **Requirements**

   Pastikan **Python 3.8+** sudah terinstal. Tidak ada dependensi eksternal — hanya menggunakan modul bawaan Python (`random`, `json`, `os`, `time`).

3. **Run the Game**

   ```bash
   python main.py
   ```

---

## 🎮 Gameplay Controls

Semua input berbasis teks (angka atau huruf sesuai menu yang tampil).

### Town Menu

| Input | Aksi                            |
| :---: | :------------------------------ |
|  `1`  | Explore Area                    |
|  `2`  | Enter Dungeon                   |
|  `3`  | Rest (pulihkan HP & Mana penuh) |
|  `4`  | Inventory                       |
|  `5`  | Check Status                    |
|  `6`  | Save Game                       |
|  `0`  | Exit Game                       |

### Battle Menu

| Input | Aksi                                                      |
| :---: | :-------------------------------------------------------- |
|  `1`  | Attack (pilih target)                                     |
|  `2`  | Command Servant Skill (konfirmasi Y/N, lalu pilih target) |
|  `3`  | Use Item (tampil inventory, pilih item)                   |
|  `4`  | Check Status (HUD lengkap semua pihak)                    |

### Navigation

|  Input  | Aksi                                    |
| :-----: | :-------------------------------------- |
| `Enter` | Lanjutkan dialog / langkah eksplorasi   |
|   `q`   | Kembali ke kota dari area eksplorasi    |
|   `0`   | Kembali / Cancel di menu dungeon & area |

---

## 🧮 Mechanics Reference

### Damage Formula

```
base    = attacker.attack - (defender.defense * 0.4)
variance = random(0.7 – 1.4)
damage  = max(1, int(base * variance))
```

- **Defense Down** → defense dikurangi 30% sebelum kalkulasi.
- **Astral Mark** → damage diterima ×1.15.
- **Critical Hit** (15% chance) → damage ×1.8 – ×2.5.
- **Servant Skill Damage** → `calc_damage(servant, target) * 1.5`.

### Mana Regenerasi

- Pemain: +3 Mana per akhir giliran.
- Servant: +2 Mana per akhir giliran.

### Player Level Up

```
exp_to_next = 100 * level^1.5
Stats per level: Max HP +12, ATK +2, DEF +1, Max Mana +4
```

### Servant Level Up

```
exp_to_next = 80 * level^1.5  (80% dari EXP player)
Stats per level: Max HP +8, ATK +2, DEF +1, Max Mana +3
```

### Bond & Mana Transfer Penalty

```
penalty = max(1.0, 1.3 - bond * 0.05)
transfer_cost = remaining_mana * penalty
```

Bond level 1 → penalty 1.25× | Bond level 6 → penalty 1.0× (no penalty).

---

_Astral-Covenant — Forge your Covenant. Face the Abyss._
