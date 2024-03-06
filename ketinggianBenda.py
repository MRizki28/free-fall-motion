def ketinggianBenda(t, g, h0):
    ht = h0 - 0.5 * g * t * t
    return ht

g = 9.8

h0 = float(input('Masukkan tinggi awal (meter): '))
t = float(input('Masukkan waktu (detik): '))

hasil = ketinggianBenda(t, g, h0)
print('Ketinggian benda setelah', t, 'detik adalah', abs(hasil), 'meter.')
