
# Praktikum Tkinter Sesi 11
## Aplikasi Pendaftaran Kegiatan Mahasiswa

### 1. Deskripsi

Aplikasi Pendaftaran Kegiatan Mahasiswa merupakan aplikasi berbasis GUI (Graphical User Interface) yang dibuat menggunakan Python Tkinter. Aplikasi ini digunakan untuk memasukkan data mahasiswa, memilih program studi, menentukan jenis kelamin, memilih kegiatan, serta menampilkan hasil pendaftaran dalam bentuk ringkasan.

Aplikasi ini dibuat sebagai penerapan materi Advanced Widgets dan Event Handling pada praktikum Python Sesi 11.

### 2. Tujuan

- Memahami penggunaan berbagai widget pada Tkinter.
- Menerapkan event handling pada aplikasi GUI.
- Membuat validasi input pengguna.
- Menggunakan menu dan dialog pada aplikasi.
- Menampilkan hasil pengolahan data melalui GUI.

### 3. Teknologi yang Digunakan

- Python 3
- Tkinter
- ttk
- Messagebox
- Visual Studio Code

### 4. Fitur

1. **Entry** untuk memasukkan nama mahasiswa.
2. **Combobox** untuk memilih program studi.
3. **Radiobutton** untuk memilih jenis kelamin.
4. **Checkbutton** untuk memilih satu atau beberapa kegiatan.
5. **Text** untuk memasukkan alasan mengikuti kegiatan.
6. **Listbox** untuk menampilkan kegiatan yang dipilih.
7. **Submit** untuk memproses data dan menampilkan ringkasan pendaftaran.
8. **Reset** untuk mengosongkan seluruh isian.
9. **Messagebox** untuk menampilkan peringatan, konfirmasi, dan notifikasi.
10. Menu **File > Keluar** untuk menutup aplikasi.
11. Menu **Bantuan > About** untuk membuka jendela informasi menggunakan Toplevel.
12. Tombol **Enter** pada keyboard untuk menjalankan Submit.
13. Validasi agar nama mahasiswa tidak boleh kosong.

### 5. Widget yang Digunakan

| Widget | Fungsi |
|---|---|
| Entry | Memasukkan nama mahasiswa |
| Combobox | Memilih program studi |
| Radiobutton | Memilih jenis kelamin |
| Checkbutton | Memilih kegiatan |
| Text | Memasukkan alasan mengikuti kegiatan |
| Listbox | Menampilkan kegiatan yang dipilih |
| Button | Menjalankan Submit dan Reset |
| Scrollbar | Menggulir tampilan aplikasi |
| Menu | Menampilkan menu File dan Bantuan |
| Toplevel | Membuat jendela About |
| Messagebox | Menampilkan pesan kepada pengguna |

### 6. Data Input Aplikasi

Data yang dimasukkan ke dalam aplikasi meliputi:

1. **Nama Mahasiswa:** Nama mahasiswa yang melakukan pendaftaran.
2. **Program Studi:** Teknik Informatika, Sistem Informasi, Manajemen, atau Pendidikan Agama Islam.
3. **Jenis Kelamin:** Laki-laki atau perempuan.
4. **Pilihan Kegiatan:**
   - Seminar Teknologi
   - Workshop Pemrograman
   - Lomba Karya Tulis
   - Pelatihan Desain Grafis
   - Kegiatan Organisasi
5. **Alasan Mengikuti:** Alasan mahasiswa ingin mengikuti kegiatan.

### 7. Kode-Kode Penting

#### A. Import Library

```python
import tkinter as tk
from tkinter import ttk, messagebox
```

**Penjelasan:**
Mengimpor library Tkinter untuk membuat tampilan GUI, ttk untuk menggunakan widget tambahan, dan messagebox untuk menampilkan pesan.

#### B. Membuat Variabel Input

```python
self.nama_var = tk.StringVar()
self.prodi_var = tk.StringVar()
self.gender_var = tk.StringVar(value="")
self.kegiatan_vars = {}
```

**Penjelasan:**
Digunakan untuk menyimpan data nama, program studi, jenis kelamin, dan pilihan kegiatan yang dimasukkan pengguna.

#### C. Membuat Validasi Nama

```python
nama = self.nama_var.get().strip()

if not nama:
    messagebox.showwarning(
        "Peringatan",
        "Nama mahasiswa tidak boleh kosong."
    )
    self.entry_nama.focus_set()
    return
```

**Penjelasan:**
Memeriksa apakah nama mahasiswa sudah diisi. Jika nama masih kosong, sistem akan menampilkan peringatan dan proses Submit dihentikan.

#### D. Mengambil Kegiatan yang Dipilih

```python
kegiatan_dipilih = [
    kegiatan
    for kegiatan, var in self.kegiatan_vars.items()
    if var.get()
]
```

**Penjelasan:**
Mengambil seluruh kegiatan yang dipilih pengguna berdasarkan status Checkbutton.

#### E. Menampilkan Ringkasan

```python
self.text_ringkasan.config(state="normal")
self.text_ringkasan.delete("1.0", tk.END)
self.text_ringkasan.insert(tk.END, ringkasan)
self.text_ringkasan.config(state="disabled")
```

**Penjelasan:**
Menghapus ringkasan sebelumnya, menampilkan hasil pendaftaran terbaru, kemudian mengunci Text agar tidak dapat diedit secara langsung.

#### F. Fungsi Reset

```python
def reset(self):
    self.nama_var.set("")
    self.prodi_var.set("")
    self.gender_var.set("")

    for var in self.kegiatan_vars.values():
        var.set(False)
```

**Penjelasan:**
Mengosongkan nama, program studi, jenis kelamin, dan seluruh pilihan kegiatan. Fungsi ini juga digunakan untuk menghapus alasan, daftar kegiatan, dan ringkasan pendaftaran.

#### G. Event Handling Tombol Enter

```python
self.root.bind("<Return>", self.submit)
```

**Penjelasan:**
Menghubungkan tombol Enter pada keyboard dengan fungsi Submit sehingga pengguna dapat memproses pendaftaran tanpa harus menekan tombol Submit menggunakan mouse.

#### H. Menu About

```python
def tampilkan_about(self):
    jendela_about = tk.Toplevel(self.root)
    jendela_about.title("About Aplikasi")
    jendela_about.geometry("400x250")
```

**Penjelasan:**
Membuat jendela baru menggunakan Toplevel untuk menampilkan informasi mengenai aplikasi.

#### I. Menjalankan Aplikasi

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = PendaftaranKegiatanApp(root)
    root.mainloop()
```

**Penjelasan:**
Membuat jendela utama, menjalankan class aplikasi, dan mempertahankan aplikasi agar tetap berjalan serta menerima interaksi pengguna.

### 8. Cara Menjalankan Aplikasi

1. Pastikan Python 3 sudah terpasang pada komputer.
2. Buka folder proyek melalui Visual Studio Code.
3. Buka file `main.py`.
4. Jalankan program menggunakan tombol Run Python File atau melalui terminal dengan perintah:

```bash
python main.py
```

5. Tunggu sampai tampilan aplikasi muncul.
6. Isi formulir pendaftaran sesuai data yang diminta.
7. Pilih kegiatan yang ingin diikuti.
8. Klik tombol Submit untuk memproses dan menampilkan ringkasan pendaftaran.

### 9. Hasil Pengujian

Pengujian dilakukan secara langsung pada aplikasi untuk memastikan setiap fitur berjalan sesuai dengan fungsinya.

| No. | Fitur yang Diuji | Hasil |
|---|---|---|
| 1 | Submit dan ringkasan pendaftaran | Berhasil |
| 2 | Tombol Reset | Berhasil |
| 3 | Validasi nama kosong | Berhasil |
| 4 | Tombol Enter | Berhasil |
| 5 | Menu Bantuan > About | Berhasil |
| 6 | Menu File > Keluar | Berhasil |
| 7 | Fungsi Scroll | Berhasil |

**Hasil Pengujian:**

Berdasarkan pengujian yang telah dilakukan, seluruh fitur berhasil berjalan sesuai dengan fungsinya. Data mahasiswa dapat diproses dan ditampilkan dalam bentuk ringkasan. Formulir juga dapat dikosongkan kembali menggunakan tombol Reset. Selain itu, validasi input, menu, dan fitur Scroll dapat digunakan dengan baik.

### 10. Screenshot Aplikasi

Screenshot digunakan sebagai bukti tampilan dan hasil pengujian aplikasi.

Simpan screenshot aplikasi ke dalam folder `screenshot` dengan nama file `screenshot-aplikasi.png`.

**Struktur Folder:**

```text
praktikum-tkinter-sesi-11/
│
├── main.py
├── README.md
│
└── screenshot/
    └── screenshot-aplikasi.png
```

### 11. Kesimpulan

Aplikasi Pendaftaran Kegiatan Mahasiswa berhasil dibuat menggunakan Python Tkinter dengan menerapkan berbagai widget, validasi input, dan event handling. Aplikasi ini dapat menerima data mahasiswa, memproses pilihan kegiatan, serta menampilkan hasil pendaftaran dalam bentuk ringkasan.

Berdasarkan hasil pengujian, seluruh fitur yang dibuat dapat berjalan sesuai dengan fungsinya. Melalui praktikum ini, dapat dipahami penerapan materi Advanced Widgets dan Event Handling dalam pembuatan aplikasi berbasis GUI menggunakan Python Tkinter.

### 12. Identitas Pembuat

- **Nama:** Septya Ramadhani
- **Program Studi:** Teknik Informatika A
- **NIM:** 2595114015
- **Mata Kuliah:** Pemrograman Berorientasi Objek