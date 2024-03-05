import math

def kecepatanAlternativTerminal(t, g):
    vt = g * t
    
    return vt

g = 9.8
t = float(input('Masukkan waktu tempuh (detik):'))

hasil = kecepatanAlternativTerminal(t,g)
print("Kecepatan benda setelah", t,'adalah', hasil,'m')
