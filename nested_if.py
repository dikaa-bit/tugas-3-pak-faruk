print('HASIL UJIAN')
nilai = int(input('Masukan nilai:'))
if nilai >= 70 :
    status = 'Lulus'
    if nilai >= 80 :
        predikat = 'Memuaskan'
    else :
        predikat = 'Cukup'
else :
    status = 'Gagal'
    predikat = 'Kurang'

print('Satus :',status)
print('Predikat :',predikat)
print('-------------')
