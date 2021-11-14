"""
View Metode Numerik
"""
import time
from C_mn import *
from M_mn import *



# Meminta Inputan / Input Request
def input_pers():
    """
    Input   : Tanpa parameter
    Output  : Mengembalikan persamaan inputan
    Proses  : Meminta input persamaan bertipe data str,
              yang akan dicek dulu apakah bisa diuraikan 
              atau tidak, saat ini masih terbatas pada
              persamaan dengan 1 variabel.
    """
    print("Input Persamaan")
    persamaan = str.lower(input("Persamaan : "))
    cek = cek_pers(persamaan)
    if cek is True:
        return persamaan
    elif cek == -1:
        print("Persamaan harus memiliki 1 variabel dan hanya variabel x saja")
        time.sleep(6)
        print("\033[A"*6 + chr(27)+"[0J",end='')
        return input_pers()
    else:
        print("Harap isikan operator dengan benar")
        time.sleep(6)
        print("\033[A"*6 + chr(27)+"[0J",end='')
        return input_pers()
    

def input_selang(persamaan):
    """
    Input   : Tanpa parameter
    Output  : Mengembalikan 2 selang inputan
    Proses  : Menginputkan 2 batas selang
    """
    print("\nInput Rentang Selang")
    try:
        s0 = int(input("Batas atas : "))
    except ValueError :
        print(ValueError, "Nilai selang harus berisi dan bertipe int")
        time.sleep(3)
        print("\033[A"*4 + chr(27)+"[0J",end='')
        return input_selang(persamaan)
    
    try:
        s1 = int(input("Batas bawah : "))
    except ValueError :
        print(ValueError, "Nilai selang harus berisi dan bertipe int")
        time.sleep(3)
        print("\033[A"*5 + chr(27)+"[0J",end='')
        return input_selang(persamaan)

    # Menukar posisi jika s0 > s1 agar s0 < s1
    if s0 > s1:
        s0, s1 = s1, s0
    
    # Memeriksa ketersedian akar pada selang s0 sampai s1
    if cek_selang(persamaan, s0, s1) == False:
        
        return input_selang(persamaan)

    return s0, s1

def input_tebakan(metode=''):
    print("\nInput tebakan awal")
    try:
        if metode == '':
            a = int(input("Tebakan : "))
            return a
        else:
            a = int(input("Tebakan 1 : "))
            b = int(input("Tebakan 2 : "))
            return a, b
    except ValueError:
        print(ValueError, "Nilai tebakan harus berisi dan bertipe int")
        time.sleep(3)
        print("\033[A"*4 + chr(27)+"[0J",end='')
        return input_tebakan()
    

def input_max():
    print("\nInput jumlah iterasi maksimum")
    try:
        a = int(input("Iterasi maksimum : "))
    except ValueError:
        print(ValueError, "Nilai harus berisi dan bertipe int")
        time.sleep(3)
        print("\033[A"*4 + chr(27)+"[0J",end='')
        return input_max()
    return a

def input_eps():
    print("\nInput nilai toleransi error (epsilon)")
    try:
        epsilon = float(input("Epsilon : "))
        if epsilon > 0.1:
            raise AssertionError
        elif epsilon <= 0:
            raise AssertionError

    except ValueError:
        print(ValueError ,"Nilai epsilon harus berisi dan bertipe float")
        time.sleep(3)
        print("\033[A"*4 + chr(27)+"[0J",end='')
        return input_eps()

    except AssertionError:
        print(AssertionError, "Nilai epsilon harus <= 0.1 dan > 0 !!")
        time.sleep(3)
        print("\033[A"*4 + chr(27)+"[0J",end='')
        return input_eps()

    return epsilon

def bisec_req(persamaan):
    """
    Inputan yang diperlukan untuk
    metode bagi dua
    """
    a, b = input_selang(persamaan)
    epsilon = input_eps()
    return a, b, epsilon

def rfals_req(persamaan):
    """
    Inputan yang diperlukan untuk
    metode titk palsu
    """
    a, b = input_selang(persamaan)
    epsilon = input_eps()
    return a, b, epsilon

def itt_req():
    """
    Inputan yang diperlukan untuk
    metode iterasi titik tetap
    """
    x = input_tebakan()
    eps = input_eps()
    max_iter = input_max()
    return x, eps, max_iter

def nr_req():
    """
    Inputan yang diperlukan untuk
    metode newton-raphson
    """
    x = input_tebakan()
    eps = input_eps()
    return x, eps


def sec_req():
    """
    Inputan yang diperlukan untuk
    metode secant
    """
    x0, x1 = input_tebakan(metode='secant')
    epsilon = input_eps()
    max_iter = input_max()
    return x0, x1, epsilon, max_iter


def aplikasi():
    os.system('cls || clear')
    main_tittle()
    main_menu()
    pilih = input("\nMasukkan pilihan anda : ")
    if pilih == '1':
        os.system('cls || clear')
        print("--------------------------------")
        print("||       Metode Bagi Dua      ||")
        print("--------------------------------")

        persamaan = input_pers()
        a, b, epsilon = bisec_req(persamaan)
        selang = cari_selang(persamaan,a,b)
        
        for p, q in selang:
            print(f"\nIterasi dengan selang [{p},{q}] pada persamaan {persamaan}\n")
            bisec_meth(persamaan,p,q,epsilon)


    elif pilih == '2':
        os.system('cls || clear')
        print("--------------------------------")
        print("||     Metode Posisi Palsu    ||")
        print("--------------------------------")

        persamaan = input_pers()
        a, b, epsilon = rfals_req(persamaan)
        selang = cari_selang(persamaan,a,b)
        
        for p, q in selang:
            print(f"\nIterasi dengan selang [{p},{q}] pada persamaan {persamaan}\n")
            rfals_meth(persamaan,p,q,epsilon)


    elif pilih == '3':
        os.system('cls || clear')
        print("--------------------------------")
        print("|| Metode Iterasi Titik Tetap ||")
        print("--------------------------------")
        print("Persamaan    : f(x) = x^2 - 10x - 20")
        print("Iterasi 1    : g(x) = (10x + 20)^(1/2)")
        print("Iterasi 2    : g(x) = (x^2 - 20) / 10")
        print("Iterasi 3    : g(x) = 20 / (x-10)")

        x, epsilon, max_iter = itt_req()
        persamaan = 'x**2 - 10*x - 20'
        iter1 = '(10*x + 20)**(1/2)'
        iter2 = '(x**2 - 20)/10'
        iter3 = '20/(x-10)'
        
        itt_meth(x, epsilon, max_iter, iter1, iter2, iter3)


    elif pilih == '4':
        os.system('cls || clear')
        print("--------------------------------")
        print("||   Metode Newton-Raphson    ||")
        print("--------------------------------")
        print("Persamaan    : f(x) = x^2 - 10x - 20")
        print("Turunan      : f'(x) = 2x - 10")

        persamaan = 'x**2 - 10*x - 20'
        turunan = '2*x - 10'

        
        while True:
            x, epsilon = nr_req()
            hasil = nr_meth(persamaan, turunan, x, epsilon)
            if hasil is -1:
                continue
            else:
                break
        

    elif pilih == '5':
        os.system('cls || clear')
        print("--------------------------------")
        print("||       Metode Secant        ||")
        print("--------------------------------")

        persamaan = input_pers()
        while True:
            x0, x1, epsilon, max_iter = sec_req()
            hasil = sec_meth(persamaan, x0, x1, epsilon, max_iter)
            if hasil is 'ulang':
                continue
            else:
                break

    else:
        return aplikasi()


if __name__ == "__main__":
    # Berjalan di Console / Terminal
    aplikasi()
