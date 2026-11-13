
import tkinter as tk
from tkinter import ttk, messagebox


class PendaftaranKegiatanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pendaftaran Kegiatan Mahasiswa")
        self.root.state("zoomed")
        self.root.minsize(850, 700)

        self.nama_var = tk.StringVar()
        self.prodi_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="")

        self.kegiatan_vars = {}

        self.daftar_kegiatan = [
            "Seminar Teknologi",
            "Workshop Pemrograman",
            "Lomba Karya Tulis",
            "Pelatihan Desain Grafis",
            "Kegiatan Organisasi"
        ]

        self.buat_menu()
        self.buat_antarmuka()

        self.root.bind("<Return>", self.submit)

    def buat_menu(self):
        menu_bar = tk.Menu(self.root)

        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(
            label="Keluar",
            command=self.keluar
        )

        menu_bar.add_cascade(
            label="File",
            menu=menu_file
        )

        menu_bantuan = tk.Menu(menu_bar, tearoff=0)
        menu_bantuan.add_command(
            label="About",
            command=self.tampilkan_about
        )

        menu_bar.add_cascade(
            label="Bantuan",
            menu=menu_bantuan
        )

        self.root.config(menu=menu_bar)

    def buat_antarmuka(self):
        judul = ttk.Label(
            self.root,
            text="FORMULIR PENDAFTARAN KEGIATAN MAHASISWA",
            font=("Arial", 16, "bold")
        )
        judul.pack(pady=(12, 4))

        keterangan = ttk.Label(
            self.root,
            text="Silakan isi data diri dan pilih kegiatan yang ingin diikuti."
        )
        keterangan.pack(pady=(0, 8))

        frame_scroll = ttk.Frame(self.root)
        frame_scroll.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(
            frame_scroll,
            highlightthickness=0
        )
        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            frame_scroll,
            orient="vertical",
            command=self.canvas.yview
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        frame_utama = ttk.Frame(
            self.canvas,
            padding=10
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=frame_utama,
            anchor="nw"
        )

        frame_utama.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(
                self.canvas_window,
                width=event.width
            )
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.scroll_mouse
        )

        frame_form = ttk.LabelFrame(
            frame_utama,
            text="Data Pendaftaran",
            padding=10
        )
        frame_form.pack(
            fill="x",
            pady=(0, 8)
        )

        frame_form.columnconfigure(1, weight=1)

        ttk.Label(
            frame_form,
            text="Nama Mahasiswa"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.entry_nama = ttk.Entry(
            frame_form,
            textvariable=self.nama_var
        )
        self.entry_nama.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_form,
            text="Program Studi"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        combo_prodi = ttk.Combobox(
            frame_form,
            textvariable=self.prodi_var,
            values=[
                "Teknik Informatika",
                "Sistem Informasi",
                "Manajemen",
                "Pendidikan Agama Islam"
            ],
            state="readonly"
        )
        combo_prodi.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        ttk.Label(
            frame_form,
            text="Jenis Kelamin"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        frame_gender = ttk.Frame(frame_form)
        frame_gender.grid(
            row=2,
            column=1,
            sticky="w",
            padx=5,
            pady=5
        )

        ttk.Radiobutton(
            frame_gender,
            text="Laki-laki",
            variable=self.gender_var,
            value="Laki-laki"
        ).pack(
            side="left",
            padx=(0, 15)
        )

        ttk.Radiobutton(
            frame_gender,
            text="Perempuan",
            variable=self.gender_var,
            value="Perempuan"
        ).pack(side="left")

        ttk.Label(
            frame_form,
            text="Pilihan Kegiatan"
        ).grid(
            row=3,
            column=0,
            sticky="nw",
            padx=5,
            pady=5
        )

        frame_kegiatan = ttk.Frame(frame_form)
        frame_kegiatan.grid(
            row=3,
            column=1,
            sticky="w",
            padx=5,
            pady=5
        )

        for index, kegiatan in enumerate(self.daftar_kegiatan):
            var = tk.BooleanVar(value=False)
            self.kegiatan_vars[kegiatan] = var

            ttk.Checkbutton(
                frame_kegiatan,
                text=kegiatan,
                variable=var,
                command=self.perbarui_listbox
            ).grid(
                row=index // 2,
                column=index % 2,
                sticky="w",
                padx=(0, 20),
                pady=2
            )

        ttk.Label(
            frame_form,
            text="Alasan Mengikuti"
        ).grid(
            row=4,
            column=0,
            sticky="nw",
            padx=5,
            pady=5
        )

        self.text_alasan = tk.Text(
            frame_form,
            height=3,
            wrap="word"
        )
        self.text_alasan.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        frame_list = ttk.LabelFrame(
            frame_utama,
            text="Daftar Kegiatan yang Dipilih",
            padding=7
        )
        frame_list.pack(
            fill="x",
            pady=5
        )

        self.listbox_kegiatan = tk.Listbox(
            frame_list,
            height=3,
            selectmode=tk.BROWSE
        )
        self.listbox_kegiatan.pack(
            fill="x",
            padx=5,
            pady=3
        )

        frame_tombol = ttk.Frame(frame_utama)
        frame_tombol.pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            frame_tombol,
            text="Submit",
            command=self.submit
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame_tombol,
            text="Reset",
            command=self.reset
        ).pack(
            side="left",
            padx=5
        )

        frame_info = ttk.LabelFrame(
            frame_utama,
            text="Informasi / Ringkasan Pendaftaran",
            padding=8
        )
        frame_info.pack(
            fill="x",
            pady=(5, 0)
        )

        self.text_ringkasan = tk.Text(
            frame_info,
            height=10,
            wrap="word",
            state="disabled"
        )
        self.text_ringkasan.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.entry_nama.focus_set()

    def scroll_mouse(self, event):
        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    def perbarui_listbox(self):
        self.listbox_kegiatan.delete(0, tk.END)

        for kegiatan, var in self.kegiatan_vars.items():
            if var.get():
                self.listbox_kegiatan.insert(
                    tk.END,
                    kegiatan
                )

    def submit(self, event=None):
        nama = self.nama_var.get().strip()

        if not nama:
            messagebox.showwarning(
                "Peringatan",
                "Nama mahasiswa tidak boleh kosong."
            )
            self.entry_nama.focus_set()
            return

        prodi = self.prodi_var.get() or "-"
        gender = self.gender_var.get() or "-"

        kegiatan_dipilih = [
            kegiatan
            for kegiatan, var in self.kegiatan_vars.items()
            if var.get()
        ]

        alasan = self.text_alasan.get(
            "1.0",
            tk.END
        ).strip() or "-"

        if kegiatan_dipilih:
            daftar = "\n".join(
                f"- {item}"
                for item in kegiatan_dipilih
            )
        else:
            daftar = "- Belum memilih kegiatan"

        ringkasan = (
            "PENDAFTARAN BERHASIL\n"
            "====================================\n"
            f"Nama            : {nama}\n"
            f"Program Studi   : {prodi}\n"
            f"Jenis Kelamin   : {gender}\n\n"
            f"Kegiatan:\n{daftar}\n\n"
            f"Alasan Mengikuti:\n{alasan}\n"
            "====================================\n"
        )

        self.text_ringkasan.config(
            state="normal"
        )

        self.text_ringkasan.delete(
            "1.0",
            tk.END
        )

        self.text_ringkasan.insert(
            tk.END,
            ringkasan
        )

        self.text_ringkasan.config(
            state="disabled"
        )

        self.canvas.update_idletasks()
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

        messagebox.showinfo(
            "Pendaftaran Berhasil",
            f"Terima kasih, {nama}. "
            "Data pendaftaran berhasil diproses."
        )

    def reset(self):
        self.nama_var.set("")
        self.prodi_var.set("")
        self.gender_var.set("")

        for var in self.kegiatan_vars.values():
            var.set(False)

        self.text_alasan.delete(
            "1.0",
            tk.END
        )

        self.listbox_kegiatan.delete(
            0,
            tk.END
        )

        self.text_ringkasan.config(
            state="normal"
        )

        self.text_ringkasan.delete(
            "1.0",
            tk.END
        )

        self.text_ringkasan.config(
            state="disabled"
        )

        self.entry_nama.focus_set()
        self.canvas.yview_moveto(0)

    def tampilkan_about(self):
        jendela_about = tk.Toplevel(self.root)

        jendela_about.title("About Aplikasi")
        jendela_about.geometry("400x250")
        jendela_about.resizable(False, False)

        jendela_about.transient(self.root)
        jendela_about.grab_set()
        jendela_about.lift()
        jendela_about.focus_force()

        ttk.Label(
            jendela_about,
            text="APLIKASI PENDAFTARAN KEGIATAN MAHASISWA",
            font=("Arial", 11, "bold"),
            wraplength=350,
            justify="center"
        ).pack(
            pady=(25, 15),
            padx=10
        )

        ttk.Label(
            jendela_about,
            text=(
                "Praktikum Python Tkinter\n"
                "Sesi 11 - Advanced Widgets dan Event Handling\n\n"
                "Aplikasi ini dibuat untuk latihan penggunaan "
                "widget, validasi, menu, dan event handling."
            ),
            justify="center",
            wraplength=350
        ).pack(pady=10)

        ttk.Button(
            jendela_about,
            text="Tutup",
            command=jendela_about.destroy
        ).pack(pady=15)

    def keluar(self):
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Keluar",
            "Apakah Anda yakin ingin keluar dari aplikasi?"
        )

        if konfirmasi:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PendaftaranKegiatanApp(root)
    root.mainloop()
