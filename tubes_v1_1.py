from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from time import *
import random
import os


# Inisialisasi semua kelas, objek, dan variabel


class Produk:
    def __init__(self, nama, kuantitas, harga, diskon=0.0):
        self.nama = nama
        self.kuantitas = kuantitas
        self.harga = harga
        self.diskon = diskon


class Promo:
    def __init__(self, nama, minProduk, minHarga , reduksiHarga, durasi):
        self.nama = nama
        self.minProduk = minProduk
        self.minHarga = minHarga
        self.reduksiHarga = reduksiHarga
        self.durasi = durasi


def initialize():
    global nilai_uang, jumlah_uang, list_uang, jumlah_produk, counter1, counter2, counter3, counter4

    nilai_uang = {"seratus_ribu": 100000, "limapuluh_ribu": 50000, "duapuluh_ribu": 20000,
                  "sepuluh_ribu": 10000, "lima_ribu": 5000, "dua_ribu": 2000,
                  "satu_ribu": 1000, "lima_ratus": 500, "dua_ratus": 200, "satu_ratus": 100}

    jumlah_uang = {"seratus_ribu": 24, "limapuluh_ribu": 21, "duapuluh_ribu": 25,
                   "sepuluh_ribu": 23, "lima_ribu": 25, "dua_ribu": 20,
                   "satu_ribu": 21, "lima_ratus": 23, "dua_ratus": 21, "satu_ratus": 25}

    list_uang = list()
    for a in jumlah_uang:
        list_uang.append(a)

    counter1, counter2, counter3, counter4 = 0, 0, 0, 0


def set_produk():
    global kode_produk, list_produk
    global indomie, abon_sapi, kacang, coklat_meisis, strawberry_jam, sardine, minyak_goreng, gula_aren, margarine, keju
    global tepung_terigu, corned_beef, tuna, pringles, olive_oil, beras, yoghurt, saus_tiram, kecap_manis, santan_kelapa
    indomie = Produk("Indomie Goreng", 50, 3000)
    abon_sapi = Produk("Abon Sapi", 20, 12500)
    beras = Produk("Beras", 10, 50000, 0.2)
    coklat_meisis = Produk("Coklat Meisis", 50, 4900)
    strawberry_jam = Produk("Strawberry Jam", 20, 11500)
    sardine = Produk("Sardine Saus Tomat", 10, 9000, 0.08)
    minyak_goreng = Produk("Minyak Goreng", 50, 36800, 0.1)
    gula_aren = Produk("Gula Aren", 20, 15600)
    margarine = Produk("Margarine", 10, 13100, 0.24)
    tepung_terigu = Produk("Tepung Terigu", 50, 16800, 0.17)
    corned_beef = Produk("Corned Beef", 20, 34400)
    tuna = Produk("Tuna Chunks", 10, 28900, 0.14)
    pringles = Produk("Pringles", 50, 25600)
    olive_oil = Produk("Olive Oil", 20, 49000, 0.23)
    kacang = Produk("Kacang Almond", 10, 17100)
    yoghurt = Produk("Yoghurt", 50, 9100)
    saus_tiram = Produk("Saus Tiram", 20, 38900, 0.2)
    kecap_manis = Produk("Kecap Manis", 10, 21700)
    santan_kelapa = Produk("Santan Kelapa", 50, 3200, 0.16)
    keju = Produk("Keju Easy Melt", 20, 25000)

    kode_produk = dict()
    list_produk = (indomie, abon_sapi, beras, coklat_meisis, strawberry_jam, sardine, minyak_goreng, gula_aren,
                   margarine, tepung_terigu, corned_beef, tuna, pringles, olive_oil, kacang, yoghurt, saus_tiram,
                   kecap_manis, santan_kelapa, keju)

    for b in list_produk:
        kode_produk[f"{b.nama[0:3]}{str(b.harga)[0:2]}"] = b

    for c in list_produk:
        c.kuantitas = random.randint(5, 75)


def set_promo():
    global list_promo, promo1, promo2, promo3, promo4, promo5
    promo1 = Promo("Promo Waktu Terbatas!", {beras: 2, gula_aren: 3}, 225000, 26000, 42)
    promo2 = Promo("Promo Bersuka Ria!", {sardine: 3, abon_sapi: 2, corned_beef: 2}, 65000, 15000, 64)
    promo3 = Promo("Promo Paling Hemat!", {minyak_goreng: 1, olive_oil: 1}, 165000, 45500, 84)
    promo4 = Promo("Promo Tanggal Merah!", {keju: 4, margarine: 3}, 54000, 8000, 23)
    promo5 = Promo("Promo Bulan Berkah!", {yoghurt: 3, santan_kelapa: 2, keju: 1}, 46000, 6500, 96)
    list_promo = (promo1, promo2, promo3, promo4, promo5)


filepath = os.path.dirname(os.path.realpath(__file__))

initialize()
set_produk()
set_promo()

# ----------------------------------------------------------------------------------------------------------------------


# Inisialisasi main window

main_window = Tk()
main_window.geometry("1136x640"
                     f"+{(main_window.winfo_screenwidth() - 1136) // 2}"
                     f"+{(main_window.winfo_screenheight() - 640) // 2}")
main_window.title("Kasir STEI-Mart!")

bg_canvas = Canvas(main_window)
bg_canvas.pack(fill=BOTH, expand=1)

# ----------------------------------------------------------------------------------------------------------------------


# Window loops

def loop1():
    global counter1, counter2, counter3, counter4, loopcount
    try:
        if button_products.winfo_exists():
         
            main_window.update()
            bg_canvas.delete(ALL)
            bg_canvas.create_text(main_window.winfo_width()/2, main_window.winfo_height() / 2 - frame_mainButtons.winfo_height(), 
                                  font=("Maiandra GD", 75), text="STEI-MART!")

            button_exit.place(x=8, y=10)
            button_info.place(x=main_window.winfo_width() - button_info.winfo_width() - 8, y=8)
            button_help.place(x=8, y=main_window.winfo_height() - button_help.winfo_height() - 8)
            label_clock.place(x=main_window.winfo_width() - label_clock.winfo_width() - 8,
                              y=main_window.winfo_height() - label_clock.winfo_height() - 8)
            frame_mainButtons.place(x=(main_window.winfo_width() - frame_mainButtons.winfo_width()) // 2,
                                    y=(main_window.winfo_height() - frame_mainButtons.winfo_height()) // 2)
            label_clock.config(text=strftime("%H:%M WIB"))

            try:
                if not window_info.winfo_exists():
                    counter1 = 0
            except:
                pass
            try:
                if not window_help.winfo_exists():
                    counter2 = 0
            except:
                pass
            try:
                if not window_produk.winfo_exists():
                    counter3 = 0
            except:
                pass
            try:
                if not window_cash.winfo_exists():
                    counter4 = 0
            except:
                pass

            if loopcount > 10:
                if main_window.winfo_width() < 568 or main_window.winfo_height() < 450:
                    if messagebox.showerror("Error Size Window", "Size window terlalu kecil!") == "ok":
                        main_window.geometry("1136x640"
                                             f"+{(main_window.winfo_screenwidth() - 1136) // 2}"
                                             f"+{(main_window.winfo_screenheight() - 640) // 2}")
                        main_window.update()
            loopcount += 1

            main_window.after(50, loop1)

    except:
        try:
            if label_subTotal.winfo_exists():
                pass
            else:
                main_window.after(50, loop1)
        except:
            main_window.after(50, loop1)


def loop2():
    global counter1, counter2, loopcount
    try:
        if label_subTotal.winfo_exists():

            main_window.update()
            bg_canvas.delete(ALL)

            button_exit.place(x=8, y=10)
            button_info.place(x=main_window.winfo_width() - button_info.winfo_width() - 8, y=8)
            button_help.place(x=8, y=main_window.winfo_height() - button_help.winfo_height() - 8)
            label_clock.place(x=main_window.winfo_width() - label_clock.winfo_width() - 8,
                              y=main_window.winfo_height() - label_clock.winfo_height() - 8)
            label_clock.config(text=strftime("%H:%M WIB"))

            button_back.place(x=main_window.winfo_width() // 2-button_next.winfo_width() - 50,
                              y=main_window.winfo_height() - button_back.winfo_height() - 8,
                              width=button_next.winfo_width())
            button_next.place(x=main_window.winfo_width() // 2 + 50,
                              y=main_window.winfo_height() - button_next.winfo_height() - 8)


            frame_hitungHarga.place(x=(main_window.winfo_width() - frame_hitungHarga.winfo_width()) // 2,
                                    y=(main_window.winfo_height() - frame_hitungHarga.winfo_height()) // 2,
                                    width=main_window.winfo_width() - label_clock.winfo_width() * 2.5,
                                    height=main_window.winfo_height() - button_info.winfo_height() * 2.5)

            frame_calc.place(x=8, y=10, width=5 / 9 * frame_hitungHarga.winfo_width() - 20,
                             height=frame_hitungHarga.winfo_height() - 20)
            frame_console.place(x=5/9*frame_hitungHarga.winfo_width() + 8, y=10,
                                width=4/9*frame_hitungHarga.winfo_width()-20,
                                height=frame_hitungHarga.winfo_height()-20)

            frame_kodeProduk.place(x=(frame_calc.winfo_width()-frame_kodeProduk.winfo_width())//2,
                                   y=(frame_calc.winfo_height()-(frame_kodeProduk.winfo_height()+
                                   frame_hargaProduk.winfo_height()+frame_numpad.winfo_height()+40))//2)
            frame_hargaProduk.place(x=(frame_calc.winfo_width()-frame_hargaProduk.winfo_width())//2,
                                    y = (frame_calc.winfo_height() - (frame_kodeProduk.winfo_height() +
                                    frame_hargaProduk.winfo_height() + frame_numpad.winfo_height() + 40)) // 2 +
                                    frame_kodeProduk.winfo_height()+10)
            frame_numpad.place(x=(frame_calc.winfo_width()-frame_numpad.winfo_width())//2,
                               y = (frame_calc.winfo_height() - (frame_kodeProduk.winfo_height() +
                               frame_hargaProduk.winfo_height() + frame_numpad.winfo_height() + 40)) // 2 +
                               frame_kodeProduk.winfo_height() + frame_kodeProduk.winfo_height() + 40)

            bgframe_console.place(x=-2, y=label_judulConsole.winfo_height()+5, width=frame_console.winfo_width()+40,
                                  height=frame_console.winfo_height()-label_judulConsole.winfo_height()-14)
            label_judulConsole.place(x=-2, y=2, width=frame_console.winfo_width())
            label_subTotal.place(x=-2, y=frame_console.winfo_height()-label_subTotal.winfo_height()-5,
                                 width=frame_console.winfo_width())

            try:
                if window_produk.winfo_exists():
                    button_randomize.config(state=DISABLED)
                    window_produk.update()
            except:
                pass

            try:
                if window_info.winfo_exists() == 0:
                    counter1 = 0
            except:
                pass
            try:
                if window_help.winfo_exists() == 0:
                    counter2 = 0
            except:
                pass

            if loopcount > 10:
                if main_window.winfo_width() < 1060 or main_window.winfo_height() < 610:
                    if messagebox.showerror("Error Size Window", "Size window terlalu kecil!") == "ok":
                        main_window.geometry("1136x640"
                                             f"+{(main_window.winfo_screenwidth() - 1136) // 2}"
                                             f"+{(main_window.winfo_screenheight() - 640) // 2}")
                        main_window.update()
            loopcount += 1

            main_window.after(50, loop2)

    except:
        try:
            if button_products.winfo_exists() or frame_hitungKembalian.winfo_exists():
                pass
            else:
                main_window.after(50, loop2)
        except:
            main_window.after(50, loop2)


def loop3():
    global counter1, counter2, loopcount
    try:
        if frame_hitungKembalian.winfo_exists():

            main_window.update()
            bg_canvas.delete(ALL)
            
            button_exit.place(x=8, y=10)
            button_info.place(x=main_window.winfo_width() - button_info.winfo_width() - 8, y=8)
            button_help.place(x=8, y=main_window.winfo_height() - button_help.winfo_height() - 8)
            label_clock.place(x=main_window.winfo_width() - label_clock.winfo_width() - 8,
                              y=main_window.winfo_height() - label_clock.winfo_height() - 8)
            label_clock.config(text=strftime("%H:%M WIB"))

            button_back.place(x=main_window.winfo_width() // 2-button_back.winfo_width() - 50,
                              y=main_window.winfo_height() - button_back.winfo_height() - 8)
            button_next.place(x=main_window.winfo_width() // 2 + 50,
                              y=main_window.winfo_height() - button_back.winfo_height() - 8, width=button_back.winfo_width())

            frame_hitungKembalian.place(x=(main_window.winfo_width()-frame_hitungKembalian.winfo_width())//2,
                                        y=(main_window.winfo_height()-frame_hitungKembalian.winfo_height())//2,
                                       width=main_window.winfo_width()-label_clock.winfo_width()*2.5,
                                       height=main_window.winfo_height()-button_info.winfo_height()*2.5)

            frame_tampilTunai.place(x=(frame2_hitungKembalian.winfo_width() - frame_tampilTunai.winfo_width()) / 2,
                                    y=(frame2_hitungKembalian.winfo_height() - (frame_tampilTunai.winfo_height() +
                                    frame_kembalian.winfo_height() + 30))/2)

            frame2_hitungKembalian.place(x=18, y=18, width=frame_hitungKembalian.winfo_width() - 38,
                                         height=frame_hitungKembalian.winfo_height() - 38)
            frame_numpad.place(x=(frame2_hitungKembalian.winfo_width() - (frame_numpad.winfo_width() +
                               frame_kembalian.winfo_width() + 15)) / 2, y=frame_kembalian.winfo_y())
            frame_kembalian.place(x=(frame2_hitungKembalian.winfo_width() - (frame_numpad.winfo_width() +
                                  frame_kembalian.winfo_width() + 15)) / 2 + frame_numpad.winfo_width() + 13,
                                  y=((frame2_hitungKembalian.winfo_height() - (frame_tampilTunai.winfo_height() +
                                  frame_kembalian.winfo_height() + 30)) / 2 + frame_tampilTunai.winfo_height()) + 30,
                                  width=frame_numpad.winfo_width(), height=frame_numpad.winfo_height())

            try:
                if window_produk.winfo_exists():
                    button_randomize.config(state=DISABLED)
                    window_produk.update()
            except:
                pass

            try:
                if window_info.winfo_exists() == 0:
                    counter1 = 0
            except:
                pass
            try:
                if window_help.winfo_exists() == 0:
                    counter2 = 0
            except:
                pass

            if loopcount > 10:
                if main_window.winfo_width() < 1080 or main_window.winfo_height() < 520:
                    if messagebox.showerror("Error Size Window", "Size window terlalu kecil!") == "ok":
                        main_window.geometry("1136x640"
                                             f"+{(main_window.winfo_screenwidth() - 1136) // 2}"
                                             f"+{(main_window.winfo_screenheight() - 640) // 2}")
                        main_window.update()
            loopcount += 1

            main_window.after(50, loop3)

    except:
        try:
            if label_subTotal.winfo_exists() or button_print.winfo_exists():
                pass
            else:
                main_window.after(50, loop3)
        except:
            main_window.after(50, loop3)


def loop4():
    global counter1, counter2, loopcount
    try:
        if button_print.winfo_exists():
            
            main_window.update()
            bg_canvas.delete(ALL)
            bg_canvas.create_text(main_window.winfo_width() / 2, main_window.winfo_height() / 2 - frame_endButtons.winfo_height() / 1.2, 
                                  font=("Maiandra GD", 50), text="Terima Kasih Telah Berbelanja!")

            button_exit.place(x=8, y=8)
            button_info.place(x=main_window.winfo_width() - button_info.winfo_width() - 8, y=8)
            button_help.place(x=8, y=main_window.winfo_height() - button_help.winfo_height() - 8)
            label_clock.place(x=main_window.winfo_width() - label_clock.winfo_width() - 8,
                              y=main_window.winfo_height() - label_clock.winfo_height() - 8)
            frame_endButtons.place(x=(main_window.winfo_width() - frame_endButtons.winfo_width()) // 2,
                                    y=(main_window.winfo_height() - frame_endButtons.winfo_height()) // 2)
            label_clock.config(text=strftime("%H:%M WIB"))

            try:
                if window_produk.winfo_exists():
                    button_randomize.config(state=DISABLED)
                    window_produk.update()
            except:
                pass

            try:
                if not window_info.winfo_exists():
                    counter1 = 0
            except:
                pass
            try:
                if not window_help.winfo_exists():
                    counter2 = 0
            except:
                pass

            if loopcount > 10:
                if main_window.winfo_width() < 940 or main_window.winfo_height() < 610:
                    if messagebox.showerror("Error Size Window", "Size window terlalu kecil!") == "ok":
                        main_window.geometry("1136x640"
                                             f"+{(main_window.winfo_screenwidth() - 1136) // 2}"
                                             f"+{(main_window.winfo_screenheight() - 640) // 2}")
                        main_window.update()
            loopcount += 1

            main_window.after(50, loop4)

    except:
        try:
            if button_products.winfo_exists():
                pass
            else:
                main_window.after(50, loop4)
        except:
            main_window.after(50, loop4)


# ----------------------------------------------------------------------------------------------------------------------


# Window info dan help

def open_info():
    global counter1, window_info
    if counter1 != 1:
        counter1 = 1
        teksinfo = f"""Program ini dibuat oleh Kelompok 3 Kelas 22 KU1102 dengan anggota:
• Abel Aprilliani - 19622008;
• Irfan Nurhakim Hilmi - 16522028;
• Kharris Khisunica - 19622118;
• Lianna Grace Hana Margareta - 16522138; dan
• Nur Ainun - 10022210.

Tujuan dibuatnya program ini adalah untuk memenuhi kewajiban Tugas Besar 1 dari mata kuliah KU1102 Pengenalan Komputasi yang diampu oleh Dr. Nur Ulfa Maulidevi, S.T., M.Sc.
"""
        window_info = Toplevel()
        window_info.title("Info")
        window_info.geometry("568x320"  
                             f"+{(main_window.winfo_screenwidth() - 568) // 2}"
                             f"+{(main_window.winfo_screenheight() - 320) // 2}")
        window_info.resizable(False, False)

        bgcanvas_info = Canvas(window_info)
        bgcanvas_info.pack(fill=BOTH, expand=1)

        bgcanvas_info.create_text(568/2, 20, font=("Maiandra GD", 15), width=568, text="Program Model Kasir Supermarket v1.1", justify=CENTER)
        bgcanvas_info.create_text(7, 40, anchor=NW, font=("Maiandra GD", 13), width=568, text=teksinfo)


def open_help():
    global counter2, window_help, bgcanvas_help
    if counter2 != 1:
        counter2 = 1
        window_help = Toplevel()
        window_help.title("Help")
        window_help.geometry("568x320")
        window_help.resizable(False, False)

        window_help.update()
        bgcanvas_help = Canvas(window_help)
        bgcanvas_help.pack(side=LEFT, fill=BOTH, expand=1)
        scroll_help = Scrollbar(window_help, orient=VERTICAL, command=bgcanvas_help.yview)
        scroll_help.pack(side=RIGHT, fill=Y)
        bgframe2_help = Frame(bgcanvas_help)
        bgframe2_help.place(x=568/2, y=0)

        bgcanvas_help.config(yscrollcommand=scroll_help.set)
        bgcanvas_help.bind("<Configure>", lambda event:bgcanvas_help.config(scrollregion=bgcanvas_help.bbox(ALL)))
        bgcanvas_help.create_window((0, 0), window=bgframe2_help, anchor=NW)
        bgcanvas_help.bind("<MouseWheel>", scroll)
        bgcanvas_help.bind("<Enter>", bound)
        bgcanvas_help.bind("<Leave>", unbound)

        try:
            if button_products.winfo_exists():

                count= 0
                Label(bgframe2_help, font=("Maiandra GD", 20), text="Petunjuk Penggunaan Program", anchor=CENTER).grid(row=0, column=0, sticky=E + W, padx=5, pady=5)

                for ar in range(6):
                    if count == 0:
                        teks1 = "Tombol Exit:"
                        teks2 = "Tekan tombol ini untuk keluar dari program."
                    elif count == 1:
                        teks1 = "Tombol Info:"
                        teks2 = "Tekan tombol ini untuk melihat informasi program serta pembuatnya."
                    elif count == 2:
                        teks1 = "Tombol Help:"
                        teks2 = "Tekan tombol ini untuk melihat petunjuk penggunaan program."
                    elif count == 3:
                        teks1 = "Tombol Mulai:"
                        teks2 = "Tekan tombol ini untuk memulai perhitungan pembelian customer."
                    elif count == 4:
                        teks1 = "Tombol Uang:"
                        teks2 = """Tekan tombol ini untuk melihat informasi mengenai lembaran uang pada
kasir.
                        
Pada window ini, akan ditampilkan jumlah lembaran uang rupiah yang
tersedia pada kasir.

Dapat juga mengganti jumlah lembaran dengan menekan tombol Tambah
Uang."""
                    elif count == 5:    
                        teks1 = "Tombol Produk:"
                        teks2 = """Tekan tombol ini untuk melihat informasi mengenai produk dan promo
yang sedang berlaku.

Pada window ini, akan ditampilkan nama, harga, stok, dan kode dari 
masing-masing produk.

Untuk melihat list produk yang memiliki diskon saja, dapat menekan
tombol Diskon.

Untuk melihat list promo yang sedang berlaku serta persyaratannya, dapat
menekan tombol Promo.

Tombol Randomize dapat digunakan untuk mengacak ulang besar diskon
masing-masing produk dan promo-promo yang berlaku."""
                    
                    Label(bgframe2_help, font=("Maiandra GD", 15), text=teks1, anchor=CENTER, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 1, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help, font=("Maiandra GD", 12), text=teks2, anchor=W, justify=LEFT, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 2, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help).grid(row=3 * ar + 3, column=0)
                    count += 1
        except:
            pass

        try:
            if label_subTotal.winfo_exists():
                count= 0
                Label(bgframe2_help, font=("Maiandra GD", 20), text="Petunjuk Penggunaan Program", anchor=CENTER).grid(row=0, column=0, sticky=E + W, padx=5, pady=5)

                for ar in range(6):
                    if count == 0:
                        teks1 = "Entry Box:"
                        teks2 = """Pada bagian kiri atas, terdapat entry box untuk memasukkan kode produk.

Kode dari masing-masing produk dapat dilihat di window Produk pada
menu sebelumnya."""
                    elif count == 1:
                        teks1 = "Tombol Cek:"
                        teks2 = """Tekan tombol ini untuk menampilkan harga produk.

Pastikan kode yang  dimasukkan benar (termasuk penggunaan kapital)
karena harga produk hanya akan ditampilkan jika kode yang dimasukkan
valid."""
                    elif count == 2:
                        teks1 = "Numpad:"
                        teks2 = """Gunakan numpad untuk menggantikan jumlah produk yang dapat dilihat
di sebelah kanan tampilan harga produk.

Terdapat juga tombol Reset untuk mereset jumlah produk menjadi nol
jika salah memasukkan nilai."""
                    elif count == 3:
                        teks1 = "Tombol Enter:"
                        teks2 = """Tekan tombol ini untuk mengonfirmasi jenis dan jumlah produk yang dibeli
customer.

Pastikan informasi pembelian sudah benar karena jika terjadi kesalahan,
informasi pembelian hanya bisa direset dari awal dengan menekan tombol
Back to Main di bagian bawah.

Pastikan juga sudah menekan tombol Cek karena perhitungan harga hanya
akan dilakukan jika harga produk sudah ditampilkan."""
                    elif count == 4:
                        teks1 = "Console:"
                        teks2 = """Jika sudah menekan tombol Enter, informasi pembelian akan ditampilkan
pada console di bagian kanan."""
                    elif count == 5:    
                        teks1 = "Tombol Hitung Kembalian:"
                        teks2 = """Tekan tombol ini jika sudah selesai menghitung semua pembelian customer
dan ingin melanjutkan ke perhitungan selanjutnya, yaitu menghitung total
kembalian.

Perhitungan kembalian hanya bisa dilakukan jika terdapat setidaknya satu
produk yang dibeli."""
                    
                    Label(bgframe2_help, font=("Maiandra GD", 15), text=teks1, anchor=CENTER, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 1, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help, font=("Maiandra GD", 12), text=teks2, anchor=W, justify=LEFT, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 2, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help).grid(row=3 * ar + 3, column=0)
                    count += 1
        except:
            pass

        try:
            if frame_lembaran.winfo_exists():
                count= 0
                Label(bgframe2_help, font=("Maiandra GD", 20), text="Petunjuk Penggunaan Program", anchor=CENTER).grid(row=0, column=0, sticky=E + W, padx=5, pady=5)

                for ar in range(4):
                    if count == 0:
                        teks1 = "Harga Total:"
                        teks2 = """Hasil dari perhitungan sebelumnya akan ditampilkan pada bagian ini."""
                    elif count == 1:
                        teks1 = "Uang Tunai:"
                        teks2 = """Gunakan numpad untuk memasukkan besar uang tunai yang diberikan
customer.
                        
Terdapat juga tombol Reset untuk mereset uang tunai menjadi nol jika 
salah memasukkan besarnya."""
                    elif count == 2:
                        teks1 = "Tombol Enter:"
                        teks2 = """Tekan tombol ini untuk menghitung total kembaliannya serta jumlahnya
dalam bentuk lembaran uang rupiah.

Total kembalian hanya akan dihitung jika besar uang tunai lebih banyak
daripada harga total pembelian.

Perhitungan total kembalian dapat dilakukan berkali-kali dengan menekan
tombol ini, tetapi setiap kali tombol ini ditekan, stok lembaran uang
akan terus berkurang."""
                    elif count == 3:
                        teks1 = "Tombol Selesai Transaksi:"
                        teks2 = """Jika sudah selesai menghitung kembaliannya, dapat menekan tombol ini
untuk menyelesaikan transaksi dan membuat struk pembeliannya."""

                    Label(bgframe2_help, font=("Maiandra GD", 15), text=teks1, anchor=CENTER, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 1, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help, font=("Maiandra GD", 12), text=teks2, anchor=W, justify=LEFT, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 2, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help).grid(row=3 * ar + 3, column=0)
                    count += 1
        except:
            pass

        try:
            if button_print.winfo_exists():
                count= 0
                Label(bgframe2_help, font=("Maiandra GD", 20), text="Petunjuk Penggunaan Program", anchor=CENTER).grid(row=0, column=0, sticky=E + W, padx=5, pady=5)

                for ar in range(3):
                    if count == 0:
                        teks1 = "Tombol Back to Main:"
                        teks2 = """Tekan tombol ini untuk kembali ke menu utama."""
                    elif count == 1:
                        teks1 = "Tombol Print Receipt:"
                        teks2 = """Tekan tombol ini untuk menampilkan struk pembelian pada console."""
                    elif count == 2:
                        teks1 = "Tombol Save Receipt:"
                        teks2 = """Tekan tombol ini untuk menyimpan struk pembelian ke PC dalam bentuk
text file."""

                    Label(bgframe2_help, font=("Maiandra GD", 15), text=teks1, anchor=CENTER, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 1, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help, font=("Maiandra GD", 12), text=teks2, anchor=W, justify=LEFT, relief=RIDGE, padx=5, pady=5).grid(row=3 * ar + 2, column=0, sticky=E + W, padx=5)
                    Label(bgframe2_help).grid(row=3 * ar + 3, column=0)
                    count += 1
        except:
            pass


# ----------------------------------------------------------------------------------------------------------------------


# Window awal mulai program

def window_mulai():
    global button_exit, button_info, button_help, label_clock, frame_mainButtons, button_products
    global harga_total, produk_receipt, loopcount, count_receipt

    try:
        button_exit.destroy()
        button_info.destroy()
        button_help.destroy()
        label_clock.destroy()
        button_back.destroy()
        button_next.destroy()
        frame_hitungHarga.destroy()
    except:
        pass

    try:
        button_exit.destroy()
        button_info.destroy()
        button_help.destroy()
        label_clock.destroy()
        frame_endButtons.destroy()
    except:
        pass

    harga_total = 0
    produk_receipt = dict()
    loopcount = 0
    count_receipt = 0

    button_exit = Button(main_window, font=("Maiandra GD", 14), text="Exit", padx=5, pady=5,
                         command=main_window.destroy)
    button_info = Button(main_window, font=("Maiandra GD", 14), text="Info", padx=5, pady=5, command=open_info)
    button_help = Button(main_window, font=("Maiandra GD", 14), text="Help", padx=5, pady=5, command=open_help)
    label_clock = Label(main_window, font=("Maiandra GD", 14), relief=RAISED, padx=5, pady=5)
    button_exit.place()
    button_info.place()
    button_help.place()
    label_clock.place()

    frame_mainButtons = LabelFrame(main_window)
    button_start = Button(frame_mainButtons, font=("Maiandra GD", 24), text="Mulai", width=7, command=window_harga)
    button_cash = Button(frame_mainButtons, font=("Maiandra GD", 24), text="Uang", width=7, command=window_listcash)
    button_products = Button(frame_mainButtons, font=("Maiandra GD", 24), text="Produk", width=7,
                             command=window_listproduk)
    frame_mainButtons.place()
    button_start.grid(row=0, column=0, columnspan=2, pady=10)
    button_cash.grid(row=1, column=0, padx=35, pady=10)
    button_products.grid(row=1, column=1, padx=35, pady=10)

    loop1()


# ----------------------------------------------------------------------------------------------------------------------


# Window list produk

def window_listproduk():
    global counter3, window_produk, bgframe_produk, button_randomize, bgcanvas_produk

    if counter3 != 1:
        counter3 = 1
        window_produk = Toplevel()
        window_produk.title("List Produk")
        window_produk.geometry("568x640")
        window_produk.resizable(False, False)
        window_produk.update()

        button_randomize = Button(window_produk, font=("Maiandra GD", 18), text="Randomize", command=randomize)
        button_listProduk = Button(window_produk, font=("Maiandra GD", 18), text="Produk", command=tampil_produk)
        button_listDiskon = Button(window_produk, font=("Maiandra GD", 18), text="Diskon", command=tampil_diskon)
        button_listPromo = Button(window_produk, font=("Maiandra GD", 18), text="Promo", command=tampil_promo)
        button_randomize.place(x=0, y=0)
        button_listProduk.place(x=0, y=0)
        button_listDiskon.place(x=0, y=0)
        button_listPromo.place(x=0, y=0)

        window_produk.update()
        button_randomize.place(x=(window_produk.winfo_width()-button_randomize.winfo_width())//2, y=5)
        button_listProduk.place(x=40, y=window_produk.winfo_height()-button_listDiskon.winfo_height()-5,
                                width=button_randomize.winfo_width())
        button_listDiskon.place(x=(window_produk.winfo_width()-button_randomize.winfo_width())//2,
                                y=window_produk.winfo_height()-button_listDiskon.winfo_height()-5,
                                width=button_randomize.winfo_width())
        button_listPromo.place(x=window_produk.winfo_width()-button_randomize.winfo_width()-40,
                               y=window_produk.winfo_height()-button_listDiskon.winfo_height()-5,
                               width=button_randomize.winfo_width())

        window_produk.update()
        bgframe_produk = LabelFrame(window_produk)
        bgframe_produk.place(x=0, y=button_randomize.winfo_height()+10, width=window_produk.winfo_width(),
                             height=window_produk.winfo_height()-2*button_randomize.winfo_height()-20)
        bgcanvas_produk = Canvas(bgframe_produk)
        scroll_produk = Scrollbar(bgframe_produk, orient=VERTICAL, command=bgcanvas_produk.yview)
        scroll_produk.pack(side=RIGHT, fill=Y)
        bgcanvas_produk.pack(side=LEFT, fill=BOTH, expand=1)
        bgframe2_produk = Frame(bgcanvas_produk, padx=3, pady=3)

        bgcanvas_produk.config(yscrollcommand=scroll_produk.set)
        bgcanvas_produk.bind("<Configure>", lambda event:bgcanvas_produk.config(scrollregion=bgcanvas_produk.bbox(ALL)))
        bgcanvas_produk.create_window((0, 0), window=bgframe2_produk, anchor=NW)
        bgcanvas_produk.bind("<MouseWheel>", scroll)
        bgcanvas_produk.bind("<Enter>", bound)
        bgcanvas_produk.bind("<Leave>", unbound)

        for d in range(0, len(list_produk) + 1, 2):
            try:
                if list_produk[d].diskon == 0.0:
                    temptext = f"{list_produk[d].nama}\nHarga: Rp{list_produk[d].harga:,.02f}\nKode Produk: " \
                               f"{list_produk[d].nama[0:3]}{str(list_produk[d].harga)[0:2]}\nStock: " \
                               f"{list_produk[d].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=d // 2, column=0, padx=10, pady=7)
                else:
                    temptext = f"{list_produk[d].nama}\nHarga: Rp\u0336" + \
                               "\u0336".join(f"{list_produk[d].harga:,.02f}") + \
                               f" {int(list_produk[d].harga * (1 - list_produk[d].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[d].nama[0:3]}{str(list_produk[d].harga)[0:2]}\nStock: " \
                               f"{list_produk[d].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=d // 2, column=0, padx=10, pady=7)

            except:
                pass

        for e in range(1, len(list_produk) + 1, 2):
            try:
                if list_produk[e].diskon == 0.0:
                    temptext = f"{list_produk[e].nama}\nHarga: Rp{list_produk[e].harga:,.02f}\nKode Produk: " \
                               f"{list_produk[e].nama[0:3]}{str(list_produk[e].harga)[0:2]}\nStock: " \
                               f"{list_produk[e].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=(e-1) // 2, column=1, padx=10, pady=7)
                else:
                    temptext = f"{list_produk[e].nama}\nHarga: Rp\u0336" + \
                                "\u0336".join(f"{list_produk[e].harga:,.02f}") + \
                               f" {int(list_produk[e].harga * (1 - list_produk[e].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[e].nama[0:3]}{str(list_produk[e].harga)[0:2]}\nStock: " \
                               f"{list_produk[e].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=(e-1) // 2, column=1, padx=10, pady=7)

            except:
                pass


def tampil_produk():
    global bgframe_produk, bgframe2_produk, button_randomize, bgcanvas_produk
    try:
        bgframe_produk.destroy()

        try:
            if label_judulConsole.winfo_exists():
                button_randomize.config(state=DISABLED)
        except:
            pass

        window_produk.update()
        bgframe_produk = LabelFrame(window_produk)
        bgframe_produk.place(x=0, y=button_randomize.winfo_height() + 10, width=window_produk.winfo_width(),
                             height=window_produk.winfo_height() - 2 * button_randomize.winfo_height() - 20)
        bgcanvas_produk = Canvas(bgframe_produk)
        scroll_produk = Scrollbar(bgframe_produk, orient=VERTICAL, command=bgcanvas_produk.yview)
        scroll_produk.pack(side=RIGHT, fill=Y)
        bgcanvas_produk.pack(side=LEFT, fill=BOTH, expand=1)
        bgframe2_produk = Frame(bgcanvas_produk, padx=3, pady=3)

        bgcanvas_produk.config(yscrollcommand=scroll_produk.set)
        bgcanvas_produk.bind("<Configure>", lambda event:bgcanvas_produk.config(scrollregion=bgcanvas_produk.bbox(ALL)))
        bgcanvas_produk.create_window((0, 0), window=bgframe2_produk, anchor=NW)
        bgcanvas_produk.bind("<MouseWheel>", scroll)
        bgcanvas_produk.bind("<Enter>", bound)
        bgcanvas_produk.bind("<Leave>", unbound)

        for f in range(0, len(list_produk) + 1, 2):
            try:
                if list_produk[f].diskon == 0.0:
                    temptext = f"{list_produk[f].nama}\nHarga: Rp{list_produk[f].harga:,.02f}\nKode Produk: " \
                               f"{list_produk[f].nama[0:3]}{str(list_produk[f].harga)[0:2]}\nStock: " \
                               f"{list_produk[f].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=f // 2, column=0, padx=10, pady=7)
                else:
                    temptext = f"{list_produk[f].nama}\nHarga: Rp\u0336" + "\u0336".join(
                               f"{list_produk[f].harga:,.02f}") + \
                               f" {int(list_produk[f].harga * (1 - list_produk[f].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[f].nama[0:3]}{str(list_produk[f].harga)[0:2]}\nStock: " \
                               f"{list_produk[f].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=f // 2, column=0, padx=10, pady=7)

            except:
                pass

        for g in range(1, len(list_produk) + 1, 2):
            try:
                if list_produk[g].diskon == 0.0:
                    temptext = f"{list_produk[g].nama}\nHarga: Rp{list_produk[g].harga:,.02f}\nKode Produk: " \
                               f"{list_produk[g].nama[0:3]}{str(list_produk[g].harga)[0:2]}\nStock: " \
                               f"{list_produk[g].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=(g - 1) // 2, column=1, padx=10, pady=7)
                else:
                    temptext = f"{list_produk[g].nama}\nHarga: Rp\u0336" + "\u0336".join(
                               f"{list_produk[g].harga:,.02f}") + \
                               f" {int(list_produk[g].harga * (1 - list_produk[g].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[g].nama[0:3]}{str(list_produk[g].harga)[0:2]}\nStock: " \
                               f"{list_produk[g].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=(g - 1) // 2, column=1, padx=10, pady=7)

            except:
                pass


    except:
        pass


def tampil_diskon():
    global bgframe_produk, bgframe2_produk, button_randomize, bgcanvas_produk
    try:
        bgframe_produk.destroy()

        try:
            if label_judulConsole.winfo_exists():
                button_randomize.config(state=DISABLED)
        except:
            pass

        window_produk.update()
        bgframe_produk = LabelFrame(window_produk)
        bgframe_produk.place(x=0, y=button_randomize.winfo_height() + 10, width=window_produk.winfo_width(),
                             height=window_produk.winfo_height() - 2 * button_randomize.winfo_height() - 20)
        bgcanvas_produk = Canvas(bgframe_produk)
        scroll_produk = Scrollbar(bgframe_produk, orient=VERTICAL, command=bgcanvas_produk.yview)
        scroll_produk.pack(side=RIGHT, fill=Y)
        bgcanvas_produk.pack(side=LEFT, fill=BOTH, expand=1)
        bgframe2_produk = Frame(bgcanvas_produk, padx=3, pady=3)

        bgcanvas_produk.config(yscrollcommand=scroll_produk.set)
        bgcanvas_produk.bind("<Configure>", lambda event:bgcanvas_produk.config(scrollregion=bgcanvas_produk.bbox(ALL)))
        bgcanvas_produk.create_window((0, 0), window=bgframe2_produk, anchor=NW)
        bgcanvas_produk.bind("<MouseWheel>", scroll)
        bgcanvas_produk.bind("<Enter>", bound)
        bgcanvas_produk.bind("<Leave>", unbound)

        row1 = 0
        for h in range(0, len(list_produk) + 1, 2):
            try:
                if list_produk[h].diskon == 0.0:
                    continue
                else:
                    temptext = f"{list_produk[h].nama}\nHarga: Rp\u0336" + "\u0336".join(
                               f"{list_produk[h].harga:,.02f}") + \
                               f" {int(list_produk[h].harga * (1 - list_produk[h].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[h].nama[0:3]}{str(list_produk[h].harga)[0:2]}\nStock: {list_produk[h].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=row1, column=0, padx=10, pady=7)
                    row1 += 1
            except:
                pass

        row2 = 0
        for i in range(1, len(list_produk) + 1, 2):
            try:
                if list_produk[i].diskon == 0.0:
                    continue
                else:
                    temptext = f"{list_produk[i].nama}\nHarga: Rp\u0336" + "\u0336".join(
                               f"{list_produk[i].harga:,.02f}") + \
                               f" {int(list_produk[i].harga * (1 - list_produk[i].diskon)):,.02f}\nKode Produk: " \
                               f"{list_produk[i].nama[0:3]}{str(list_produk[i].harga)[0:2]}\nStock: {list_produk[i].kuantitas}"
                    Label(bgframe2_produk, font=("Maiandra GD", 13), text=temptext, anchor=CENTER, padx=10, pady=5,
                          relief=RAISED, width=23).grid(row=row2, column=1, padx=10, pady=7)
                    row2 += 1
            except:
                pass

    except:
        pass


def tampil_promo():
    global bgframe_produk, bgframe2_promo, button_randomize, bgcanvas_produk
    try:
        bgframe_produk.destroy()

        try:
            if label_judulConsole.winfo_exists():
                button_randomize.config(state=DISABLED)
        except:
            pass

        window_produk.update()
        bgframe_produk = LabelFrame(window_produk)
        bgframe_produk.place(x=0, y=button_randomize.winfo_height() + 10, width=window_produk.winfo_width(),
                             height=window_produk.winfo_height() - 2 * button_randomize.winfo_height() - 20)
        bgcanvas_produk = Canvas(bgframe_produk)
        scroll_promo = Scrollbar(bgframe_produk, orient=VERTICAL, command=bgcanvas_produk.yview)
        scroll_promo.pack(side=RIGHT, fill=Y)
        scroll2_promo = Scrollbar(bgframe_produk, orient=HORIZONTAL, command=bgcanvas_produk.xview)
        scroll2_promo.pack(side=BOTTOM, fill=X)
        bgcanvas_produk.pack(side=LEFT, fill=BOTH, expand=1)
        bgframe2_promo = Frame(bgcanvas_produk, padx=10, pady=10)

        bgcanvas_produk.config(yscrollcommand=scroll_promo.set, xscrollcommand=scroll2_promo.set)
        bgcanvas_produk.bind("<Configure>", lambda event:bgcanvas_produk.config(scrollregion=bgcanvas_produk.bbox(ALL)))
        bgcanvas_produk.create_window((0, 0), window=bgframe2_promo, anchor=NW)
        bgcanvas_produk.bind("<MouseWheel>", scroll)
        bgcanvas_produk.bind("<Enter>", bound)
        bgcanvas_produk.bind("<Leave>", unbound)

        for j in range(0, len(list_promo) + 1):

            teks_minProduk = ""
            for k in list_promo[j].minProduk:
                if teks_minProduk == "":
                    teks_minProduk += f"{k.nama}: {list_promo[j].minProduk[k]}"
                else:
                    teks_minProduk += f", {k.nama}: {list_promo[j].minProduk[k]}"

            if list_promo[j].durasi//24 == 0:
                teks_durasiWaktu = f"{list_promo[j].durasi % 24} jam"
            elif list_promo[j].durasi%24 == 0:
                teks_durasiWaktu = f"{list_promo[j].durasi // 24} hari"
            else:
                teks_durasiWaktu = f"{list_promo[j].durasi // 24} hari {list_promo[j].durasi % 24} jam"

            Label(bgframe2_promo, font=("Maiandra GD", 25), text=list_promo[j].nama,
                  anchor=W).grid(row=0 + 6 * j, column=0, sticky=W + E, padx=5, pady=3)
            Label(bgframe2_promo, font=("Maiandra GD", 14), text=f"{teks_minProduk}",
                  anchor=W).grid(row=1 +6 * j, column=0, sticky=W + E, padx=5, pady=3)
            Label(bgframe2_promo, font=("Maiandra GD", 14), text=f"Harga minimum: Rp{list_promo[j].minHarga:,.02f}",
                  anchor=W).grid(row=2 + 6 * j, column=0, sticky=W + E, padx=5, pady=3)
            Label(bgframe2_promo, font=("Maiandra GD", 14),
                  text=f"Total promo: Rp{list_promo[j].reduksiHarga:,.02f}",
                  anchor=W).grid(row=3 + 6 * j, column=0, sticky=W + E, padx=5, pady=3)
            Label(bgframe2_promo, font=("Maiandra GD", 14), text=f"Durasi Waktu: {teks_durasiWaktu}",
                  anchor=W).grid(row=4 + 6 * j, column=0, sticky=W + E, padx=5, pady=3)
            Label(bgframe2_promo, height=1).grid(row=5+6*j, column=0, sticky=W + E, padx=5, pady=3)


    except:
        pass


def randomize():
    try:
        if bgframe2_promo.winfo_exists() :
            list_namaPromo = ["Promo Spesial!", "Promo Waktu Terbatas!", "Promo Bulan Berkah!",
                              "Promo Hari Baru!", "Promo Paling Hemat!", "Promo Anak Kosan!",
                              "Promo Tanggal Merah!", "Promo Bersuka Ria!", "Promo Senang Bersama!"]
            for l in list_promo:
                l.minProduk = dict()
                for m in range(1, random.randint(2, 5)):
                    l.minProduk[random.choice(list_produk)] = random.randint(1, 5)
                l.minHarga = random.randint(50, 250)*1000
                l.reduksiHarga = random.randint(20, 100)*500
                l.durasi = random.randint(24, 720)
                l.nama = random.choice(list_namaPromo)
                list_namaPromo.remove(l.nama)

        if bgframe2_produk.winfo_exists():
            for n in kode_produk.values():
                n.diskon = 0.0

            for o in range(random.randint(3, 11)):
                random.choice(list_produk).diskon = random.randint(0, 20) * 0.02

    except:
            for p in kode_produk.values():
                p.diskon = 0.0

            for q in range(random.randint(3, 11)):
                random.choice(list_produk).diskon = random.randint(0, 20) * 0.02


# ----------------------------------------------------------------------------------------------------------------------


# Window lembaran uang

def window_listcash():
    global counter4, window_cash, bgframe_cash, button_addCash, bgcanvas_cash

    if counter4 != 1:
        counter4 = 1
        window_cash = Toplevel()
        window_cash.title("Stock Cash")
        window_cash.geometry("568x640")
        window_cash.resizable(False, False)
        window_cash.update()

        label_judulCash = Label(window_cash, font=("Maiandra GD", 24), text="Jumlah Lembaran Uang", padx=5, pady=5)
        button_addCash = Button(window_cash, font=("Maiandra GD", 18), text="Tambah Uang", command=opt_add_cash)
        button_tampilCash = Button(window_cash, font=("Maiandra GD", 18), text="Tampil Jumlah", command=tampil_cash)
        label_judulCash.place(x=0, y=0)
        button_addCash.place(x=0, y=0)
        button_tampilCash.place(x=0, y=0)

        window_cash.update()
        label_judulCash.place(x=(window_cash.winfo_width() - label_judulCash.winfo_width()) // 2, y=5)
        button_addCash.place(x=100, y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5)
        button_tampilCash.place(x=window_cash.winfo_width() - button_tampilCash.winfo_width() - 100,
                                y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5,
                                width=button_tampilCash.winfo_width())

        window_cash.update()
        bgframe_cash = LabelFrame(window_cash)
        bgframe_cash.place(x=0, y=button_tampilCash.winfo_height() + 10, width=window_cash.winfo_width(),
                           height=window_cash.winfo_height() - 2 * button_tampilCash.winfo_height() - 20)
        bgcanvas_cash = Canvas(bgframe_cash)
        bgcanvas_cash.pack(side=LEFT, fill=BOTH, expand=1)
        scroll_cash = Scrollbar(bgframe_cash, orient=VERTICAL, command=bgcanvas_cash.yview)
        scroll_cash.pack(side=RIGHT, fill=Y)
        bgframe2_cash = Frame(bgcanvas_cash, padx=15, pady=10)

        bgcanvas_cash.config(yscrollcommand=scroll_cash.set)
        bgcanvas_cash.bind("<Configure>",
                             lambda event: bgcanvas_cash.config(scrollregion=bgcanvas_cash.bbox(ALL)))
        bgcanvas_cash.create_window((0, 0), window=bgframe2_cash, anchor=NW)
        bgcanvas_cash.bind("<MouseWheel>", scroll)
        bgcanvas_cash.bind("<Enter>", bound)
        bgcanvas_cash.bind("<Leave>", unbound)

        for r in range(0, len(jumlah_uang), 2):
            Label(bgframe2_cash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[r]]:,.02f}",
                  padx=5, pady=2, width=13).grid(row=0+3*(r//2), column=0, sticky=W+E+N+S, padx=10)
            Label(bgframe2_cash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[r]]} lembar",
                  padx=5, pady=2, relief=GROOVE).grid(row=1+3*(r//2), column=0, sticky=W+E+N+S, padx=10)
            Label(bgframe2_cash, height=1).grid(row=2+3*(r//2), column=0, sticky=W+E+N+S, padx=10)

        for s in range(1, len(jumlah_uang), 2):
            Label(bgframe2_cash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[s]]:,.02f}",
                  padx=5, pady=2, width=13).grid(row=0+3*((s-1)//2), column=1, sticky=W+E+N+S, padx=10)
            Label(bgframe2_cash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[s]]} lembar",
                  padx=5, pady=2, relief=GROOVE).grid(row=1+3*((s-1)//2), column=1, sticky=W+E+N+S, padx=10)
            Label(bgframe2_cash, height=1).grid(row=2+3*((s-1)//2), column=1, sticky=W+E+N+S, padx=10)


def opt_add_cash():
    global bgframe_cash, button_addCash, bgframe2_addCash, bgcanvas_cash
    bgframe_cash.destroy()

    label_judulCash = Label(window_cash, font=("Maiandra GD", 24), text="Jumlah Lembaran Uang", padx=5, pady=5)
    button_addCash = Button(window_cash, font=("Maiandra GD", 18), text="Tambah Uang", command=opt_add_cash)
    button_tampilCash = Button(window_cash, font=("Maiandra GD", 18), text="Tampil Jumlah", command=tampil_cash)
    label_judulCash.place(x=0, y=0)
    button_addCash.place(x=0, y=0)
    button_tampilCash.place(x=0, y=0)

    window_cash.update()
    label_judulCash.place(x=(window_cash.winfo_width() - label_judulCash.winfo_width()) // 2, y=5)
    button_addCash.place(x=100, y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5)
    button_tampilCash.place(x=window_cash.winfo_width() - button_tampilCash.winfo_width() - 100,
                             y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5,
                             width=button_tampilCash.winfo_width())

    window_cash.update()
    bgframe_cash = LabelFrame(window_cash)
    bgframe_cash.place(x=0, y=button_tampilCash.winfo_height() + 10, width=window_cash.winfo_width(),
                       height=window_cash.winfo_height() - 2 * button_tampilCash.winfo_height() - 20)
    bgcanvas_cash = Canvas(bgframe_cash)
    bgcanvas_cash.pack(side=LEFT, fill=BOTH, expand=1)
    scroll_cash = Scrollbar(bgframe_cash, orient=VERTICAL, command=bgcanvas_cash.yview)
    scroll_cash.pack(side=RIGHT, fill=Y)
    bgframe2_addCash = Frame(bgcanvas_cash, padx=15, pady=10)

    bgcanvas_cash.config(yscrollcommand=scroll_cash.set)
    bgcanvas_cash.bind("<Configure>", lambda event: bgcanvas_cash.config(scrollregion=bgcanvas_cash.bbox(ALL)))
    bgcanvas_cash.create_window((0, 0), window=bgframe2_addCash, anchor=NW)
    bgcanvas_cash.bind("<MouseWheel>", scroll)
    bgcanvas_cash.bind("<Enter>", bound)
    bgcanvas_cash.bind("<Leave>", unbound)

    for t in range(0, len(list_uang), 2):
        Label(bgframe2_addCash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[t]]:,.02f}",
              padx=5, pady=2, width=13).grid(row=0 + 3 * (t // 2), column=0, columnspan=4, sticky=W + E + N + S,padx=10)
        Label(bgframe2_addCash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[t]]} lembar",
              padx=5, pady=2, width=10, relief=GROOVE).grid(row=1 + 3 * (t // 2), column=0, sticky=N+S)
        Button(bgframe2_addCash, width=3, font=("Maiandra GD", 15), text="+",
               command=lambda t=t: add_cash(t)).grid(row=1 + 3 * (t // 2), column=1)
        Button(bgframe2_addCash, width=3, font=("Maiandra GD", 15), text="-",
               command=lambda t=t: decrease_cash(t)).grid(row=1 + 3 * (t // 2), column=2)
        Label(bgframe2_addCash, width=1).grid(row=1 + 3 * (t // 2), column=3, padx=10)
        Label(bgframe2_addCash).grid(row=2 + 3 * (t // 2), column=0, columnspan=4, sticky=W + E + N + S, padx=10)

    for u in range(1, len(list_uang), 2):
        Label(bgframe2_addCash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[u]]:,.02f}",
              padx=5, pady=2, width=13).grid(row=0 + 3 * ((u - 1) // 2), column=4, columnspan=4, sticky=W + E + N + S,
                                             padx=10)
        Label(bgframe2_addCash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[u]]} lembar",
              padx=5, pady=2, width=10, relief=GROOVE).grid(row=1 + 3 * ((u-1) // 2), column=4, sticky=N+S)
        Button(bgframe2_addCash, width=3, font=("Maiandra GD", 15), text="+",
               command=lambda u=u: add_cash(u)).grid(row=1 + 3 * ((u - 1) // 2), column=5)
        Button(bgframe2_addCash, width=3, font=("Maiandra GD", 15), text="-",
               command=lambda u=u: decrease_cash(u)).grid(row=1 + 3 * ((u - 1) // 2), column=6)
        Label(bgframe2_addCash, width=1).grid(row=1 + 3 * ((u-1) // 2), column=7, padx=10)
        Label(bgframe2_addCash, height=1).grid(row=2 + 3 * ((u - 1) // 2), column=4, columnspan=4, sticky=W + E + N + S,
                                               padx=10)


def tampil_cash():
    global bgframe_cash, button_addCash, bgcanvas_cash
    bgframe_cash.destroy()

    label_judulCash = Label(window_cash, font=("Maiandra GD", 24), text="Jumlah Lembaran Uang", padx=5, pady=5)
    button_addCash = Button(window_cash, font=("Maiandra GD", 18), text="Tambah Uang", command=opt_add_cash)
    button_tampilCash = Button(window_cash, font=("Maiandra GD", 18), text="Tampil Jumlah", command=tampil_cash)
    label_judulCash.place(x=0, y=0)
    button_addCash.place(x=0, y=0)
    button_tampilCash.place(x=0, y=0)

    window_cash.update()
    label_judulCash.place(x=(window_cash.winfo_width() - label_judulCash.winfo_width()) // 2, y=5)
    button_addCash.place(x=100, y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5)
    button_tampilCash.place(x=window_cash.winfo_width() - button_tampilCash.winfo_width() - 100,
                             y=window_cash.winfo_height() - button_tampilCash.winfo_height() - 5,
                             width=button_tampilCash.winfo_width())

    window_cash.update()
    bgframe_cash = LabelFrame(window_cash)
    bgframe_cash.place(x=0, y=button_tampilCash.winfo_height() + 10, width=window_cash.winfo_width(),
                       height=window_cash.winfo_height() - 2 * button_tampilCash.winfo_height() - 20)
    bgcanvas_cash = Canvas(bgframe_cash)
    bgcanvas_cash.pack(side=LEFT, fill=BOTH, expand=1)
    scroll_cash = Scrollbar(bgframe_cash, orient=VERTICAL, command=bgcanvas_cash.yview)
    scroll_cash.pack(side=RIGHT, fill=Y)
    bgframe2_cash = Frame(bgcanvas_cash, padx=15, pady=10)

    bgcanvas_cash.config(yscrollcommand=scroll_cash.set)
    bgcanvas_cash.bind("<Configure>", lambda event: bgcanvas_cash.config(scrollregion=bgcanvas_cash.bbox(ALL)))
    bgcanvas_cash.create_window((0, 0), window=bgframe2_cash, anchor=NW)
    bgcanvas_cash.bind("<MouseWheel>", scroll)
    bgcanvas_cash.bind("<Enter>", bound)
    bgcanvas_cash.bind("<Leave>", unbound)

    for v in range(0, len(list_uang), 2):
        Label(bgframe2_cash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[v]]:,.02f}",
              padx=5, pady=2, width=13).grid(row=0 + 3 * (v // 2), column=0, sticky=W + E + N + S, padx=10)
        Label(bgframe2_cash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[v]]} lembar",
              padx=5, pady=2, relief=GROOVE).grid(row=1 + 3 * (v // 2), column=0, sticky=W + E + N + S, padx=10)
        Label(bgframe2_cash, height=1).grid(row=2 + 3 * (v // 2), column=0, sticky=W + E + N + S, padx=10)

    for w in range(1, len(list_uang), 2):
        Label(bgframe2_cash, font=("Maiandra GD", 24), text=f"Rp{nilai_uang[list_uang[w]]:,.02f}",
              padx=5, pady=2, width=13).grid(row=0 + 3 * ((w - 1) // 2), column=1, sticky=W + E + N + S, padx=10)
        Label(bgframe2_cash, font=("Maiandra GD", 18), text=f"{jumlah_uang[list_uang[w]]} lembar",
              padx=5, pady=2, relief=GROOVE).grid(row=1 + 3 * ((w - 1) // 2), column=1, sticky=W + E + N + S, padx=10)
        Label(bgframe2_cash, height=1).grid(row=2 + 3 * ((w - 1) // 2), column=1, sticky=W + E + N + S, padx=10)


def add_cash(nilai):
    global jumlah_uang, list_uang
    jumlah_uang[list_uang[nilai]] += 1


def decrease_cash(nilai):
    global jumlah_uang, list_uang
    if jumlah_uang[list_uang[nilai]] > 0:
        jumlah_uang[list_uang[nilai]] -= 1


# ----------------------------------------------------------------------------------------------------------------------


# Window hitung harga total

def window_harga():
    global loopcount, button_exit, button_info, button_help, label_clock, button_back, button_next, frame_hitungHarga
    global label_judulConsole, frame_calc, frame_console, frame_hargaProduk, frame_kodeProduk, tampil_jumlahProduk
    global jumlah_produk, harga_produk, tampil_hargaProduk, entry_kodeProduk, label_subTotal, tempcode, tampil_subTotal
    global bgframe_console, count_hitung, bgframe2_console, bgcanvas_console

    try:
        button_back.destroy()
        button_next.destroy()
        frame_hitungKembalian.destroy()
    except:
        pass

    loopcount = 0
    frame_mainButtons.destroy()

    count_hitung = 0
    tempcode = None
    harga_produk = None
    jumlah_produk = 1
    tampil_hargaProduk = StringVar()
    tampil_jumlahProduk = StringVar()
    tampil_subTotal = StringVar()
    tampil_jumlahProduk.set(f"{int(jumlah_produk):03d}")

    button_back = Button(main_window, font=("Maiandra GD", 14), text="Back to Main", padx=5, pady=5,
                         command=window_mulai)
    button_next = Button(main_window, font=("Maiandra GD", 14), text="Hitung Kembalian", padx=5, pady=5,
                         command=window_kembalian)

    frame_hitungHarga = LabelFrame(main_window, relief=RAISED, bg="#9395a3")

    frame_calc = LabelFrame(frame_hitungHarga, relief=SUNKEN, bg="#b3b5c7")

    frame_kodeProduk = Frame(frame_calc, bg="#b3b5c7")
    label_kodeProduk = Label(frame_kodeProduk, font=("Maiandra GD", 15), text="Kode:", relief=RAISED, padx=6)
    entry_kodeProduk = Entry(frame_kodeProduk, font=("Maiandra GD", 15), width=15)
    button_cekKode = Button(frame_kodeProduk, font=("Maiandra GD", 15), text="Cek", command=cek_harga)
    label_kodeProduk.grid(row=0, column=0, padx=3, sticky=N+S)
    entry_kodeProduk.grid(row=0, column=1, padx=3, sticky=N+S)
    button_cekKode.grid(row=0, column=2, padx=3, sticky=N+S)

    frame_hargaProduk = Frame(frame_calc, relief=SUNKEN, bg="#b3b5c7")
    label_hargaProduk = Label(frame_hargaProduk, font=("digital-7", 40), textvariable=tampil_hargaProduk, width=11,
                              bg="black", fg="white", relief=SUNKEN, anchor=CENTER)
    label_x = Label(frame_hargaProduk, font=("digital-7", 40), text="x", width=1, bg="#b3b5c7")
    label_jumlahProduk = Label(frame_hargaProduk, font=("digital-7", 40), textvariable=tampil_jumlahProduk, bg="black",
                               fg="white", width=3, relief=SUNKEN, anchor=CENTER)
    label_hargaProduk.grid(row=0, column=0, padx=5)
    label_x.grid(row=0, column=1, padx=7)
    label_jumlahProduk.grid(row=0, column=2, padx=5)
    create_numpad(1)

    frame_console = LabelFrame(frame_hitungHarga, bg="black", relief=SUNKEN)
    bgframe_console = LabelFrame(frame_console, bg="black", relief=SUNKEN)
    label_judulConsole = Label(frame_console, font=("digital-7", 30), text="Console:", bg="black", fg="white",
                               anchor=CENTER, relief=SUNKEN)
    label_subTotal = Label(frame_console, font=("digital-7", 20), textvariable=tampil_subTotal, bg="black", fg="white",
                           anchor=W, padx=5, relief=SUNKEN)

    bgcanvas_console = Canvas(bgframe_console, bg="black", bd=0, highlightthickness=0)
    bgcanvas_console.pack(side=LEFT, fill=BOTH, expand=1)
    scroll_console = Scrollbar(bgframe_console, orient=VERTICAL, command=bgcanvas_console.yview)
    scroll_console.pack(side=RIGHT, fill=Y)
    bgframe2_console = Frame(bgcanvas_console, bg="black")

    bgcanvas_console.config(yscrollcommand=scroll_console.set)
    bgcanvas_console.bind("<Configure>", lambda event:bgcanvas_console.config(scrollregion=bgcanvas_console.bbox(ALL)))
    bgcanvas_console.create_window((0, 0), window=bgframe2_console, anchor=NW)
    bgcanvas_console.bind("<MouseWheel>", scroll)
    bgcanvas_console.bind("<Enter>", bound)
    bgcanvas_console.bind("<Leave>", unbound)

    loop2()


def cek_harga():
    global harga_produk, jumlah_produk, tempcode

    # Jika kode yang dimasukkan terdapat pada kamus kode_produk.
    if entry_kodeProduk.get() in kode_produk:
        tempcode = entry_kodeProduk.get()

        # Ambil nilai atribut harga dari sebuah objek Produk yang telah didapatkan berdasarkan kamus kode_produk dan
        # kode yang dimasukkannya. Nilai atribut harga ini kemudian disimpan dalam variabel harga_produk.
        harga_produk = kode_produk[entry_kodeProduk.get()].harga

        tampil_hargaProduk.set(f"Rp{harga_produk:,.02f}")

        jumlah_produk = 1
        tampil_jumlahProduk.set(f"{int(jumlah_produk):03d}")

    # Jika kode tidak ditemukan pada kamus kode_produk.
    else:
        print("Maaf user, kode produk Anda salah!")


def hitung_harga():
    global harga_produk, harga_total, jumlah_produk, count_hitung

    # Perhitungan dilakukan hanya jika jumlah produk yang dibeli lebih kecil dari stok produknya.
    if kode_produk[entry_kodeProduk.get()].kuantitas >= int(jumlah_produk):

        # Hitung nilai harga total berdasarkan jumlah produk yang dibeli dan atribut diskon yang dimiliki produk
        harga_total += (1 - kode_produk[entry_kodeProduk.get()].diskon) * kode_produk[entry_kodeProduk.get()
        ].harga * int(jumlah_produk)

        # Simpan informasi pembelian untuk membuat struk pembelian.
        if kode_produk[entry_kodeProduk.get()] not in produk_receipt:
            produk_receipt[kode_produk[entry_kodeProduk.get()]] = [int(jumlah_produk),
                                                                        kode_produk[entry_kodeProduk.get()].harga,
                                                                        kode_produk[entry_kodeProduk.get()
                                                                        ].harga * int(jumlah_produk)]
        else:
            produk_receipt[kode_produk[entry_kodeProduk.get()]][0] += int(jumlah_produk)
            produk_receipt[kode_produk[entry_kodeProduk.get()]][2] += kode_produk[entry_kodeProduk.get()
                                                                           ].harga * int(jumlah_produk)

        Label(bgframe2_console, font=("digital-7", 15), text=f"{kode_produk[entry_kodeProduk.get()].nama}   "
              f"{int(jumlah_produk)} x Rp{kode_produk[entry_kodeProduk.get()].harga:,.02f}", bg="black",
              fg="white", anchor=W, padx=5, pady=3).grid(row=count_hitung, column=0, sticky=W + E)

        tampil_subTotal.set(f"Sub Total: Rp{harga_total:,.02f}")

        kode_produk[entry_kodeProduk.get()].kuantitas -= int(jumlah_produk)
        jumlah_produk = 1
        count_hitung += 1

        tampil_jumlahProduk.set(f"{int(jumlah_produk):03d}")

    else:
        print("Pembelian produk melebihi stok yang tersedia!")


def hitung_promo():
    global harga_total, promo_aktif

    promo_aktif = set()

    # Pengecekan dilakukan untuk setiap promo di list promo.
    for v in list_promo:

        # Set templist_cekPromo digunakan untuk menyimpan sementara produk-produk yang memenuhi kriteria minProduk dari
        # setiap promo.
        templist_cekPromo = set()
        cek_promo = True

        # Cek kriteria minProduk yang dibutuhkan agar promo aktif.
        for w in v.minProduk:

            # Jika pada setiap produk yang terdapat pada struk pembelian memenuhi kriteria minProduk dari promo,
            # produk akan ditambahkan ke dalam set templist_cekPromo.
            if w in produk_receipt and produk_receipt[w][0] >= v.minProduk[w]:
                templist_cekPromo.add(w)

        # Karena kriteria minProduk dari setiap promo bisa lebih dari satu, perlu dilakukan pengecekan kembali dari
        # templist_cekPromo agar bisa memenuhi semua kriteria minProduknya.
        for x in v.minProduk:
            if x not in templist_cekPromo:
                cek_promo = False

        # Jika nilai cek_promo True dan harga total pembelian melebihi kriteria minHarga dari setiap promo, promo itu
        # sudah aktif dan dimasukkan dalam set promo_aktif.
        if cek_promo and harga_total >= v.minHarga:
            promo_aktif.add(v)

    # Kurangi harga total berdasarkan promo yang berlaku.
    for y in promo_aktif:
        harga_total -= y.reduksiHarga


# ----------------------------------------------------------------------------------------------------------------------


# Window hitung kembalian

def window_kembalian():
    global loopcount, button_exit, button_info, button_help, label_clock, button_back, button_next, frame_hitungHarga
    global harga_total, promo_aktif, frame_hitungKembalian, frame_tampilTunai, frame_kembalian, frame2_hitungKembalian
    global tampil_tunai, uang_tunai, tampil_kembalian, frame_lembaran

    if harga_total != 0:

        hitung_promo()

        loopcount = 0
        button_back.destroy()
        button_next.destroy()
        frame_hitungHarga.destroy()

        uang_tunai = 0
        tampil_tunai = StringVar()
        tampil_kembalian = StringVar()

        button_back = Button(main_window, font=("Maiandra GD", 14), text="Kembali Hitung Harga", padx=5, pady=5,
                            command=window_harga)
        button_next = Button(main_window, font=("Maiandra GD", 14), text="Selesai Transaksi", padx=5, pady=5,
                            command=window_selesai)

        frame_hitungKembalian = LabelFrame(main_window, relief=RAISED, bg="#9395a3")
        frame2_hitungKembalian = LabelFrame(frame_hitungKembalian, relief=SUNKEN, bg="#b3b5c7")

        frame_tampilTunai = Frame(frame2_hitungKembalian, bg="#b3b5c7")
        frame_tunai = Frame(frame_tampilTunai, bg="#b3b5c7")
        label_judulTunai = Label(frame_tunai, font=("Maiandra GD", 15), text="Uang Tunai:", anchor=W, bg="black",
                                fg="white", relief=GROOVE, padx=5, pady=5)
        label_tunai = Label(frame_tunai, font=("digital-7", 40), textvariable=tampil_tunai, width=15,
                            bg="black", fg="white", relief=GROOVE, anchor=CENTER)
        label_min = Label(frame_tampilTunai, font=("digital-7", 40), text="-", width=1, anchor=S, bg="#b3b5c7")
        frame_harga = Frame(frame_tampilTunai, bg="#b3b5c7")
        label_judulHarga = Label(frame_harga, font=("Maiandra GD", 15), text="Harga Total:", anchor=W, bg="black",
                                fg="white", relief=GROOVE, padx=5, pady=5)
        label_hargaTotal = Label(frame_harga, font=("digital-7", 40), text=f"Rp{harga_total:,.02f}", width=15,
                                bg="black", fg="white", relief=GROOVE, anchor=CENTER)
        frame_tunai.grid(row=0, column=0, sticky=N+S)
        label_judulTunai.grid(row=0, column=0, sticky=W+E)
        label_tunai.grid(row=1, column=0, sticky=W+E)
        label_min.grid(row=0, column=1, padx=10, sticky=N+S)
        frame_harga.grid(row=0, column=2, sticky=N+S)
        label_judulHarga.grid(row=0, column=0, sticky=W+E)
        label_hargaTotal.grid(row=1, column=0, sticky=W+E)

        create_numpad(2)

        frame_kembalian = LabelFrame(frame2_hitungKembalian, relief=RAISED)
        label_totalKembalian = Label(frame_kembalian, font=("Maiandra GD", 18), textvariable=tampil_kembalian, anchor=W,
                                    relief=SUNKEN, padx=5, pady=5)
        frame_lembaran = Frame(frame_kembalian)
        label_totalKembalian.pack(side=TOP, fill=X, padx=5, pady=5)
        frame_lembaran.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        loop3()

    else:
        print("Customer tidak membeli apa pun!")


def hitung_kembalian():
    global harga_produk, harga_total, jumlah_produk, count_hitung, frame_lembaran

    try:
        frame_lembaran.destroy()
        frame_lembaran = Frame(frame_kembalian)
        frame_lembaran.pack(side=TOP, fill=BOTH, padx=5, pady=5)
    except:
        pass

    try:        
        if int(uang_tunai) == harga_total:
            kembalian_total = int(uang_tunai) - harga_total
            tampil_kembalian.set(f"Total Kembalian: Rp{kembalian_total:,.02f}")
            Label(frame_lembaran, font=("Maiandra GD", 13), text="Tidak ada kembalian.").grid(row=0, column=0)

        elif int(uang_tunai) > harga_total:
            kembalian_total = int(uang_tunai) - harga_total
            tampil_kembalian.set(f"Total Kembalian: Rp{kembalian_total:,.02f}")

            # Variabel dictionary untuk menyimpan informasi nilai dan jumlah lembaran uang.
            lembaran_kembalian = dict()

            # Loop akan terus dilakukan hingga kembalian totalnya kurang dari nilai uang terkecil (100).
            while kembalian_total >= 100:

                tempdict_kembalian = dict()

                # Cari jumlah lembaran uang yang paling banyak.
                max_jumlahUang = None
                for z in jumlah_uang:
                    if jumlah_uang[z] < 5 or nilai_uang[z] > kembalian_total or \
                            (z != ("seratus_ribu" or "limapuluh_ribu") and kembalian_total // nilai_uang[z] > 5):
                        continue
                    if max_jumlahUang is None:
                        max_jumlahUang = z
                    elif jumlah_uang[z] > jumlah_uang[max_jumlahUang]:
                        max_jumlahUang = z

                # Cari lembaran lainnya yang jumlahnya +- 5 dari maksimumnya.
                for aa in jumlah_uang:
                    if nilai_uang[aa] > kembalian_total:
                        continue
                    if jumlah_uang[max_jumlahUang] - 3 <= jumlah_uang[aa] <= jumlah_uang[max_jumlahUang]:
                        tempdict_kembalian[aa] = jumlah_uang[aa]

                # Cari nilai uang yang paling besar dari list jumlah uang terbanyak.
                max_nilaiUang = None
                for ab in tempdict_kembalian:
                    if max_nilaiUang is None:
                        max_nilaiUang = ab
                    elif nilai_uang[ab] > nilai_uang[max_nilaiUang]:
                        max_nilaiUang = ab

                # Simpan nilai dan jumlah lembaran uang yang didapatkan ke dalam dictionary.
                if max_nilaiUang not in lembaran_kembalian:
                    lembaran_kembalian[max_nilaiUang] = 1
                else:
                    lembaran_kembalian[max_nilaiUang] += 1

                # Kurangi jumlah lembaran pada stok cash.
                jumlah_uang[max_nilaiUang] -= 1

                # Kurangi kembalian total dengan nilai uang yang didapatkan.
                kembalian_total -= nilai_uang[max_nilaiUang]

            # Sortir isi dictionary agar rapih.
            sort(lembaran_kembalian)
            templist_lembaran = list()
            for ac in sorted_dict:
                templist_lembaran.append(ac)

            for ad in range(0, len(templist_lembaran), 2):
                Label(frame_lembaran, font=("Maiandra GD", 13), anchor=W,
                text=f"Rp{nilai_uang[templist_lembaran[ad]]:,.2f}: {sorted_dict[templist_lembaran[ad]]} lembar"
                ).grid(row=ad // 2, column=0, sticky=N + W + S + E, padx=5, pady=2)
            for ae in range(1,  len(templist_lembaran), 2):
                Label(frame_lembaran, font=("Maiandra GD", 13), anchor=W,
                text=f"Rp{nilai_uang[templist_lembaran[ae]]:,.2f}: {sorted_dict[templist_lembaran[ae]]} lembar"
                ).grid(row=(ae - 1) // 2, column=1, sticky=N + W + S + E, pady=2)

    except KeyError:
        Label(frame_lembaran, font=("Maiandra GD", 13), text="Stok lembaran uang tidak mencukupi!").grid(row=0, column=0)


# ----------------------------------------------------------------------------------------------------------------------


# Window selesai transaksi

def window_selesai():
    global button_exit, button_info, button_help, label_clock, label_judulAkhir, frame_endButtons, loopcount
    global button_print, fname

    if produk_receipt == dict():
        print("Customer tidak membeli apa pun!")

    elif uang_tunai == 0:
        print("Customer tidak memberikan uang tunai!")

    else:
        try:
            button_back.destroy()
            button_next.destroy()
            frame_hitungKembalian.destroy()
        except:
            pass

        frame_endButtons = LabelFrame(main_window)
        button_restart = Button(frame_endButtons, font=("Maiandra GD", 24), text="Back to Main", width=14,
                                command=window_mulai)
        button_save = Button(frame_endButtons, font=("Maiandra GD", 24), text="Save Receipt", width=14,
                             command=save_receipt)
        button_print = Button(frame_endButtons, font=("Maiandra GD", 24), text="Print Receipt", width=14,
                              command=print_receipt)
        frame_endButtons.place()
        button_restart.grid(row=0, column=0, columnspan=2, pady=25)
        button_save.grid(row=1, column=0, padx=35, pady=25)
        button_print.grid(row=1, column=1, padx=35, pady=25)

        fname = f"""{strftime("%H%M%S_%m%d%y")}"""
        create_receipt()
        loop4()


def create_receipt():
    global teks_receipt

    harga_jual = 0
    harga_diskon = 0
    for af in produk_receipt:
        harga_jual += produk_receipt[af][2]
        harga_diskon += int(af.harga * af.diskon * produk_receipt[af][0])

    temphargajual = f"{harga_jual:,}"
    temphargadiskon = f"{harga_diskon:,}"
    temphargatotal = f"{int(harga_total):,}"
    tempuangtunai = f"{int(uang_tunai):,}"
    tempkembalian = f"{int(uang_tunai) - int(harga_total):,}"

    teks_produk = ""
    maxname = None
    maxjumlah = None
    maxharga = None
    maxtotal = None

    for ag in produk_receipt:
        temphargaproduk = f"{produk_receipt[ag][1]:,}"
        temphargatotalproduk = f"{produk_receipt[ag][2]:,}"

        if maxname is None:
            maxname = len(ag.nama)
        elif len(ag.nama) > maxname:
            maxname = len(ag.nama)

        if maxjumlah is None:
            maxjumlah = len(str(produk_receipt[ag][0]))
        elif len(str(produk_receipt[ag][0])) > maxjumlah:
            maxjumlah = len(str(produk_receipt[ag][0]))

        if maxharga is None:
            maxharga = len(temphargaproduk)
        elif len(temphargaproduk) > maxharga:
            maxharga = len(temphargaproduk)

        if maxtotal is None:
            maxtotal = len(temphargatotalproduk)
        elif len(temphargatotalproduk) > maxtotal:
            maxtotal = len(temphargatotalproduk)

    if len(temphargadiskon) == maxtotal:
        maxtotal += 1

    if len(tempuangtunai) >= maxtotal:
        maxtotal = len(tempuangtunai)

    for ah in promo_aktif:
        temphargapromo = f"{ah.reduksiHarga:,}"
        if len(temphargapromo) == maxtotal:
            maxtotal += 1


    for ai in produk_receipt:
        temphargaproduk = f"{produk_receipt[ai][1]:,}"
        temphargatotalproduk = f"{produk_receipt[ai][2]:,}"

        line_produk = f"{left(ai.nama, maxname)}   {right(str(produk_receipt[ai][0]), maxjumlah)}  " \
                      f"{right(temphargaproduk, maxharga)}  {right(temphargatotalproduk, maxtotal)}\n"
        teks_produk += line_produk

    dashline = "-" * (len(line_produk) - 1)

    teks_harga = f"""{right("Harga Jual: ", len(dashline) - maxtotal)}{right(f"{temphargajual}", maxtotal)}
{right("Total Diskon: ", len(dashline) - maxtotal)}{right(f"-{temphargadiskon}", maxtotal)}
"""

    for aj in promo_aktif:
        temphargapromo = f"{aj.reduksiHarga:,}"
        teks_harga += f"""{right(f"{aj.nama}: ", len(dashline) - maxtotal)}{right(f"-{temphargapromo}", maxtotal)}\n"""

    teks_hargaTotal = f"""{right("Harga Total: ", len(dashline) - maxtotal)}{right(f"{temphargatotal}", maxtotal)}
{right("Uang Tunai: ", len(dashline) - maxtotal)}{right(f"{tempuangtunai}", maxtotal)}
{right("Kembalian: ", len(dashline) - maxtotal)}{right(f"{tempkembalian}", maxtotal)}"""

    line1 = "STEI-Mart 210028138008118"
    line2 = "Jl. Ganesa No.10, Lb. Siliwangi"
    line3 = "Kecamatan Coblong, Kota Bandung, 40132"
    teks_awal = f"{center(line1, len(dashline))}\n{center(line2, len(line_produk))}\n{center(line3, len(dashline))}"

    teks_waktu = center(strftime("%a %b %d %H:%M:%S WIB %Y"), len(dashline))

    line4 = "TERIMA KASIH TELAH BERBELANJA DI STEI-MART!"
    line5 = "Jika terdapat kecacatan pada program,"
    line6 = "harap segera hubungi 0813829553"
    teks_akhir = f"{center(line4, len(dashline))}\n{center(line5, len(dashline))}\n{center(line6, len(dashline))}"

    if len(dashline) < len(line4):

        teks_produk = ""
        for ak in produk_receipt:
            temphargaproduk = f"{produk_receipt[ak][1]:,}"
            temphargatotalproduk = f"{produk_receipt[ak][2]:,}"

            line_produk = f"{left(ak.nama, maxname)}   {right(str(produk_receipt[ak][0]), maxjumlah)}  " \
                          f"{right(temphargaproduk, maxharga)}  {right(temphargatotalproduk, maxtotal)}\n"
            line_produk = right(line_produk, len(line4) + 1)
            teks_produk += line_produk

        teks_harga = f"""{right("Harga Jual: ", len(line4) - maxtotal)}{right(f"{temphargajual}", maxtotal)}
{right("Total Diskon: ", len(line4) - maxtotal)}{right(f"-{temphargadiskon}", maxtotal)}
"""

        for al in promo_aktif:
            temphargapromo = f"{al.reduksiHarga:,}"
            teks_harga += f"""{right(f"{al.nama}: ", len(line4) - maxtotal)}{right(f"-{temphargapromo}", maxtotal)}\n"""

        teks_hargaTotal = f"""{right("Harga Total: ", len(line4) - maxtotal)}{right(f"{temphargatotal}", maxtotal)}
{right("Uang Tunai: ", len(line4) - maxtotal)}{right(f"{tempuangtunai}", maxtotal)}
{right("Kembalian: ", len(line4) - maxtotal)}{right(f"{tempkembalian}", maxtotal)}"""

        teks_awal = f"{center(line1, len(line4))}\n{center(line2, len(line4))}\n{center(line3, len(line4))}"

        dashline = "-" * len(line4)
        teks_waktu = center(strftime("%a %b %d %H:%M:%S WIB %Y"), len(line4))

        teks_akhir = f"{center(line4, len(line4))}\n{center(line5, len(line4))}\n{center(line6, len(line4))}"

    teks_receipt = f"""
{teks_awal}
{dashline}
{teks_waktu}
{dashline}
{teks_produk}{dashline}
{teks_harga}{dashline}
{teks_hargaTotal}
{dashline}
{teks_akhir}
"""


def save_receipt():
    receiptpath = filedialog.asksaveasfile(initialdir=filepath, initialfile=f"{fname}.txt", defaultextension=".txt",
                                           filetypes=[("Text File", "*txt")])
    if receiptpath is None:
        return

    with open(receiptpath.name, "w") as f:
        f.write(teks_receipt)


def print_receipt():
    global count_receipt
    if count_receipt != 1:
        count_receipt = 1
        print(teks_receipt)
        

def center(teks, length):
    if len(teks) <= length:
        tempteks = " "*((length-len(teks))//2) + f"{teks}" + " "*((length-len(teks))//2) 
        return tempteks


def right(teks, length):
    if len(teks) <= length:
        tempteks = " "*(length-len(teks)) + f"{teks}"
        return tempteks


def left(teks, length):
    if len(teks) <= length:
        tempteks = f"{teks}" + " "*(length-len(teks))
        return tempteks


# ----------------------------------------------------------------------------------------------------------------------


# Numpads and binds

def create_numpad(type):
    global frame_numpad
    if type == 1:
        frame_numpad = Frame(frame_calc, bg="#b3b5c7")
        num = 9
        for am in range(0, 3):
            for an in range(2, -1, -1):
                Button(frame_numpad, font=("Times New Roman", 30), text=str(num), width=5, command=lambda
                       num=num: press_numpad(str(num))).grid(row=am, column=an, padx=2, pady=2)
                num -= 1

        Button(frame_numpad, font=("Times New Roman", 30), text="0", width=5, command=lambda: press_numpad("0")
               ).grid(row=3, column=0, padx=2, pady=2)
        Button(frame_numpad, font=("Times New Roman", 30), text="Reset", width=5, command=press_reset
               ).grid(row=3, column=1, padx=2, pady=2)
        Button(frame_numpad, font=("Times New Roman", 30), text="Enter", width=5, command=press_enter
               ).grid(row=3, column=2, padx=2, pady=2)

    if type == 2:
        frame_numpad = Frame(frame2_hitungKembalian, bg="#9395a3")
        num = 9
        for ao in range(0, 3):
            for ap in range(2, -1, -1):
                Button(frame_numpad, font=("Times New Roman", 25), text=str(num), width=5, command=lambda
                       num=num: press_numpad(str(num))).grid(row=ao, column=ap, padx=1, pady=1)
                num -= 1

        Button(frame_numpad, font=("Times New Roman", 25), text="0", width=5, command=lambda:
               press_numpad("0")).grid(row=3, column=0, padx=1, pady=1)
        Button(frame_numpad, font=("Times New Roman", 25), text="00", width=5, command=lambda:
               press_numpad("00")).grid(row=3, column=1, padx=1, pady=1)
        Button(frame_numpad, font=("Times New Roman", 25), text="000", width=5, command=lambda:
               press_numpad("000")).grid(row=3, column=2, padx=1, pady=1)
        Button(frame_numpad, font=("Times New Roman", 25), text="Reset", width=5, command=press_reset
               ).grid(row=0, column=3, rowspan=2, padx=1, pady=1, sticky=N+S)
        Button(frame_numpad, font=("Times New Roman", 25), text="Enter", width=5, command=press_enter
               ).grid(row=2, column=3, rowspan=2, padx=1, pady=1, sticky=N+S)


def press_numpad(num):
    global jumlah_produk, uang_tunai
    try:
        if label_judulConsole.winfo_exists() and len(str(int(jumlah_produk))) < 3:
            jumlah_produk = str(jumlah_produk) + num
            tampil_jumlahProduk.set(f"{int(jumlah_produk):03d}")
    except:
        pass

    try:
        if frame_lembaran.winfo_exists() and len(str(int(uang_tunai))) < 8:
            if (num == "000" and len(str(int(uang_tunai))) > 5) or (num == "00" and len(str(int(uang_tunai))) > 6):
                pass

            else:
                uang_tunai = str(uang_tunai) + str(num)
                tampil_tunai.set(f"Rp{int(uang_tunai):,.02f}")
    except:
        pass


def press_reset():
    global jumlah_produk, uang_tunai
    try:
        if label_subTotal.winfo_exists():
            jumlah_produk = 0
            tampil_jumlahProduk.set(f"{int(jumlah_produk):03d}")
    except:
        pass

    try:
        if frame_hitungKembalian.winfo_exists():
            uang_tunai = 0
            tampil_tunai.set(f"Rp{int(uang_tunai):,.02f}")
    except:
        pass


def press_enter():
    try:
        if label_subTotal.winfo_exists() and entry_kodeProduk.get() == tempcode:
            hitung_harga()
    except:
        pass

    try:
        if frame_lembaran.winfo_exists():
            hitung_kembalian()
    except:
        pass


def scroll(event):
    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_produk):
            bgcanvas_produk.yview_scroll(-1 * (event.delta // 120), "units")
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_cash):
            bgcanvas_cash.yview_scroll(-1 * (event.delta // 120), "units")
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_help):
            bgcanvas_help.yview_scroll(-1 * (event.delta // 120), "units")
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(main_window):
            bgcanvas_console.yview_scroll(-1 * (event.delta // 120), "units")
    except:
        pass


def bound(event):
    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_produk):
            bgcanvas_produk.bind_all("<MouseWheel>", scroll)
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_cash):
            bgcanvas_cash.bind_all("<MouseWheel>", scroll)
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(window_help):
            bgcanvas_help.bind_all("<MouseWheel>", scroll)
    except:
        pass

    try:
        if main_window.focus_displayof() == main_window.nametowidget(main_window):
            bgcanvas_console.bind_all("<MouseWheel>", scroll)
    except:
        pass


def unbound(event):
    try:
        if bgframe_produk.winfo_exists():
            bgcanvas_produk.unbind_all("<MouseWheel>")
    except:
        pass

    try:
        if bgframe_cash.winfo_exists():
            bgcanvas_cash.unbind_all("<MouseWheel>")
    except:
        pass

    try:
        if bgcanvas_help.winfo_exists():
            bgcanvas_help.unbind_all("<MouseWheel>")
    except:
        pass

    try:
        if bgframe_console.winfo_exists():
            bgcanvas_console.unbind_all("<MouseWheel>")
    except:
        pass


def sort(tbs):
    global sorted_dict
    sorted_dict = dict()
    while True:
        maxkeys = None
        for aq in tbs.items():
            if maxkeys is None:
                maxkeys = aq[0]
            elif nilai_uang[aq[0]] > nilai_uang[maxkeys]:
                maxkeys = aq[0]

        sorted_dict[maxkeys] = tbs[maxkeys]
        tbs.pop(maxkeys)

        if tbs == {}:
            break


# ----------------------------------------------------------------------------------------------------------------------


window_mulai()

main_window.mainloop()
