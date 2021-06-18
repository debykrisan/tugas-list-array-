'''
Deby Krisan Anggraeni
2G
'''
import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    clear()
    print('-------------------------------------------------------')   
    print('          TOKO SEPATU DEBY')
    print('-------------------------------------------------------')
    merk_sepatu = ['Converse','Vans','Assics','Adidas','Nike']
    harga = [850000,450000,1200000,700000,1020000]
    ppn = 0.05
    diskon = 0.15
    print('PILIHAN BARANG')
    print('-------------------------------------------------------')
    print('>> 1 = ',merk_sepatu[0],'Harga = ',format(harga[0],',.2f'))
    print('>> 2 = ',merk_sepatu[1],'Harga = ',format(harga[1],',.2f'))
    print('>> 3 = ',merk_sepatu[2],'Harga = ',format(harga[2],',.2f'))
    print('>> 4 = ',merk_sepatu[3],'Harga = ',format(harga[3],',.2f'))
    print('>> 5 = ',merk_sepatu[4],'Harga = ',format(harga[4],',.2f'))
    print('-------------------------------------------------------')
    pil = int(input("Masukan Pilihan = "))   
    jmlh = int(input("Masukkan Jumlah Pembelian = "))
    idx = 0
    while idx >=0 and idx < 5 :
        idx = idx + 1
        if (pil - 1) == idx :
            break 
        elif pil == 1 :
            idx = 0
            break
    totHrgsblmppn = jmlh * harga[idx]
    totppn = totHrgsblmppn * ppn
    totHrg = totHrgsblmppn + totppn
    if totHrgsblmppn >= 200000 :
        totdiskon = totHrg * diskon
        totHrgsesudahDiskon = totHrg - totdiskon
        print('-------------------------------------------------------')
        print('DISKON 15%')
        print('PPN 5%')
        print('-------------------------------------------------------')
        print('Merk Sepatu                  = ',merk_sepatu[idx])
        print('Harga                      = ',format(harga[idx],',.2f'))
        print('Total Harga                = ',format(totHrgsblmppn,',.2f'))
        print('Total Harga Setelah PPN    = ',format(totHrg,',.2f'))
        print('Total Harga Setelah Diskon = ',format(totHrgsesudahDiskon,',.2f'))
    else :
        print('-------------------------------------------------------')
        print('PPN 5%')
        print('-------------------------------------------------------')
        print('Merk Sepatu                  = ',merk_sepatu[idx])
        print('Harga                      = ',format(harga[idx],',.2f'))
        print('Total Harga                = ',format(totHrgsblmppn,',.2f'))      
        print('Total Harga Setelah PPN    = ',format(totHrg,',.2f'))
    print('-------------------------------------------------------')
    jwb = input('Beli Lagi? (y/t) : ')
    if jwb == 't' or jwb == 'T':
        break
    






    



        






    

