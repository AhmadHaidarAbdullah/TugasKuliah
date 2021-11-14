"""
Controller Metode Numerik digunakan 
untuk mengolah data sesuai opsi yang dipilih
"""
# Material
import os
from prettytable.prettytable import PrettyTable


def f(x, persamaan):
    return eval(persamaan)

def cek_pers(persamaan, x=1):
    """
    Input   : Parameter x untuk pemeriksaan persamaan
              dan persamaan
    Output  : True atau False, tergantung kesesuaian
    Proses  : Memeriksa SyntaxError
              Memeriksa persamaan dengan isinstance(persamaan, tipe)
    
    Kesesuaian :
    Saat ini baru bisa mengeksekusi
    persamaan yang memiliki 1 variabel
    dan hanya variabel x saja
    """
    try:
        h = 0
        for i in persamaan:
            if i == 'x':
                h += 1
        if h == 0:
            raise NameError
        if isinstance(f(x, persamaan), (int, float)):
            return True
        elif NameError:
            raise NameError
        elif SyntaxError:
            raise SyntaxError
    
    except NameError:
        print("\nError !!")
        print("Perhatikan kembali inputan anda")
        return -1

    except SyntaxError:
        print("\nError !!")
        print("Perhatikan kembali inputan anda")
        return False


def cari_selang(persamaan, a, b):
    """
    Input   : persamaan, batas atas, batas bawah
    Output  : True atau False, dan list selang yang tersedia
    Proses  : Memeriksa ketersediaan selang yang memiliki akar
    """
    # Deklarasi Variabel
    x = a               # Varibel untuk pengecekan
    s_list = list()     # Mengumpulkan data untuk pemeriksaan ketersediaan akar
    s_akar = list()     # Variabel untuk menyimpan selang-selang yang memiliki akar
    cek_ada = 0

    # Menyimpan koordinat selang pada rentang a sampai b
    while x <= b:
        x += 1
        s_list.append((x,f(x, persamaan)))
    
    # Memeriksa dan menyimpan selang yang memiliki akar
    for i in range(len(s_list)-1):
        # Syarat selang mengandung akar penyelesaian
        # Jika fx pada index i dan fx pada index i+1 terjadi perubahan tanda +/-
        # Yang diperiksa adalah f(x) nya dan yang disimpan adalah x nya
        if s_list[i][1] <= 0 and s_list[i+1][1] >= 0 or s_list[i+1][1] <= 0 and s_list[i][1] >= 0:
            cek_ada += 1
            s_akar.append((s_list[i][0], s_list[i+1][0]))
        else:
            continue
    
    if cek_ada != 0:
        return tuple(s_akar)
    else:
        return None

def cek_selang(persamaan, a, b):
    cek = cari_selang(persamaan, a, b)
    
    if cek is None:
        print("Akar penyelesaian tidak tersedia pada selang", a, "sampai", b)
        return False

# Metode Numerik
## Bagi Dua
def bisec_meth(persamaan, a, b, epsilon):
    tabel = PrettyTable(['r', 'a', 'b', 'c', 'f(a)', 'f(c)', 'lebar selang', 'keterangan'])
    r = 0
    ar = a
    br = b
    ket = 'Lanjut'
    
    while True:
        c = round((ar+br)/2, 6)
        ls = round(abs(ar - br), 6)
        try :
            fa = round(f(ar, persamaan), 6)
            fc = round(f(c, persamaan), 6)
        except ZeroDivisionError:
            print(ZeroDivisionError)
            break
        except TypeError:
            print(TypeError)
            break

        # Ketentuan iterasi
        if ls > epsilon and fa != 0 and fc != 0:
            tabel.add_row([r, ar, br, c, fa, fc, ls, ket])
        else:
            ket = 'Berhenti'
            tabel.add_row([r, ar, br, c, fa, fc, ls, ket])
            break

        # Mengganti varibel ar atau br dengan nilai baru
        if fa*fc == 0:
            break
        elif fa*fc < 0:
            # ar tetap sama dengan ar sebelumya
            br = c
        elif fa*fc > 0:
            ar = c
            # br tetap sama dengan br sebelumnya
        
        r += 1
    
    print(tabel)
    print('Hampiran akarnya adalah', c)
    print("\n-----------------------------------------\n")

## Posisi Palsu
def rfals_meth(persamaan, a, b, epsilon):
    tabel = PrettyTable(['r', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'lebar selang', 'keterangan'])
    r = 0
    ar = a
    br = b
    ket = 'Lanjut'
    
    while True:
        ls = round(abs(ar - br), 6)
        try :
            fa = round(f(ar, persamaan), 6)
            fb = round(f(br, persamaan), 6)
        except ZeroDivisionError:
            print(ZeroDivisionError)
            break
        except TypeError:
            print(TypeError)
            break

        # c (Banyak persamaan tetapi hasil sampai 6 angka dibelakang koma sama semua)
        c = br - fb*(br-ar) / (fb-fa)      # Menggunakan gradien garis AB dan BC
        # c = ar - fa*(br-ar) / (fb-fa)    # Menggunakan gradien garis AB dan AC
        # c = (fb*ar-fa*br) / (fb-fa)      # Dari modul Renaldi Munir
        
        try:
            fc = round(f(c, persamaan), 6)
        except ZeroDivisionError:
            print(ZeroDivisionError)
            break
        except TypeError:
            print(TypeError)
            break


        # Ketentuan iterasi
        if abs(fc) > epsilon and ls > epsilon:
            tabel.add_row([r, ar, br, c, fa, fb, fc, ls, ket])
        else:
            ket = 'Berhenti'
            tabel.add_row([r, ar, br, c, fa, fb, fc, ls, ket])
            break

        # Mengganti varibel ar atau br dengan nilai baru
        if fa*fc == 0:
            break
        elif fa*fc < 0:
            # ar tetap sama dengan ar sebelumya
            br = c
        elif fa*fc > 0:
            ar = c
            # br tetap sama dengan br sebelumnya
        
        r += 1
    
    print(tabel)
    print('Hampiran akarnya adalah', c)
    print("\n-----------------------------------------\n")


# ## Iterasi Titik Tetap
def itt_meth(x, eps, max_iter, *iterasi):
    tabel = PrettyTable(['r', 'Xr-1', 'Xr', '|Xr-1 - Xr|', 'Keterangan'])

    for itr in iterasi:
        flag = 0
        r = 0
        ket = 'Lanjut'
        a = x
        while True:
            try:
                a1 = round(f(a, itr), 6)
            except ZeroDivisionError:
                a1 = '(Kosong)'
                print(ZeroDivisionError, "pada iterasi", itr)
                print("\n-----------------------------------------\n")
                break
            ls = round(abs(a1 - a), 6)
            
            if r >= max_iter:
                flag += 1
                ket = 'Berhenti'
                tabel.add_row([r, a, a1, ls, ket])
                break
            if ls < eps:
                ket = 'Berhenti'
                tabel.add_row([r, a, a1, ls, ket])
                break

            tabel.add_row([r, a, a1, ls, ket])
            r += 1
            a = a1
        
        print("\nIterasi =", itr)
        if flag != 0:
            print(tabel)
            print("Iterasi Divergen")
            print('\n---------------------------------------\n')
            tabel.clear_rows()
        else:
            print(tabel)
            print("Hampiran akanya adalah", a1)
            print('\n---------------------------------------\n')
            tabel.clear_rows()
            

## Newton-Rahphson
def nr_meth(persamaan, turunan, x, eps):
    tabel = PrettyTable(['r', 'Xr', 'Xr+1', 'f(Xr)', 'f\'(Xr)', '|Xr+1 - Xr|', 'keterangan'])
    r = 0
    a = x
    ket = 'Lanjut'
    while True:
        fa = round(f(a, persamaan), 6)
        fa_d = round(f(a, turunan), 6)
        try:
            a1 = round(a - (fa/fa_d), 6)
        except ZeroDivisionError:
            print()
            print(ZeroDivisionError,', Silakan ganti tebakan lain')
            return -1

        ls = round(abs(a1-a), 6)

        if ls < eps:
            ket = 'Berhenti'
            tabel.add_row([r, a, a1, fa, fa_d, ls, ket])
            break
        
        tabel.add_row([r, a, a1, fa, fa_d, ls, ket])
        a = a1
        r += 1
    
    print(tabel)
    print("Hampiran akarnya adalah", a1)

## Secant
def sec_meth(pers, x0, x1, eps, max_itr):
    tabel = PrettyTable(['r', 'xr-1', 'f(xr-1)', 'xr', 'f(xr)', 'xr+1', '|xr+1 - xr|', 'ket'])
    r = 0
    ket = 'Lanjut'
    while True:
        fx0 = round(f(x0, pers), 6)
        fx1  = round(f(x1, pers), 6)
        try:
            x2 = round(x1 - (fx1*(x1-x0))/(fx1-fx0), 6)
        except ZeroDivisionError:
            print(tabel)
            print(ZeroDivisionError,", Silakan input tebakan lain")
            return 'ulang'
            
        ls = round(abs(x2 - x1), 6)
        
        if ls < eps and r >= max_itr:
            ket = 'Berhenti'
            tabel.add_row([r, x0, fx0, x1, fx1, x2, ls, ket])
            break
        
        tabel.add_row([r, x0, fx0, x1, fx1, x2, ls, ket])
        
        x0 = x1
        x1 = x2
        r += 1

    print(tabel)
    print("\nHampiran akarnya adalah %.5f"%x2)
    return 0
