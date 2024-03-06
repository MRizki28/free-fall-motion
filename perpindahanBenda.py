def perpindahanBenda(t,g):
    vt = 1/2 * g * t * t
    
    return vt

g = 9.8
t = float(input('Masukkan waktu tempuh (detik):'))

hasil = perpindahanBenda(t,g)
print("Sehingga perpindahan benda selama", t, '=', hasil,'m')