pembelian = 0
diskon = 0

pembelian = int(input('masukan pembelian : '))
if(pembelian >= 50000):
     diskon = pembelian * 0.05
else:
      diskon = 0

print(f'diskon = {diskon}')