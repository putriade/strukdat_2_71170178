import timeit

def prima_iteratif(awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima

def prima_rekursif(awal, akhir):
    for i in range(2, bilangan+1):
            if bilangan % i == 0:
                stat = 1
                jumlah_nol = jumlah_nol+stat
 
    if jumlah_nol == 1:
        teks = t_pri
    else:
        teks = t_npri
    
hasil1 = prima_iteratif(10)
print("Bilangan prima 10 dengan cara iteratif: ",hasil1)
hasil2 = prima_iteratif(10)
print("Bilangan prima 10 dengan cara rekursif: ",hasil2)

for i in range(1, x+1, 1):
# catat waktu mulai
    start = timeit.default_timer()
# Jalanin fungsi
    deraj(1)
# waktu hasil yg didapat
    end = timeit.default_timer()
# output
    print('Nilai ke-', i, ': ', end-start, ' second.')