import math

def waktuJatuhBebas(ketinggian):
    
    gravitasi = 9.8
    
    waktuJatuh =math.sqrt((2 * ketinggian) / gravitasi)
    
    return waktuJatuh

ketinggianObject = float(input('Masukkan ketinggian object (meter) :'))
hasil = waktuJatuhBebas(ketinggianObject)
print("Waktu jatuh bebas adalah:", hasil, "detik")