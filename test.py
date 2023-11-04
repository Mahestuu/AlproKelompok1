# from prettytable import PrettyTable

# tabel = PrettyTable()
# tabel_jumlah = PrettyTable()
# tabel_harga = PrettyTable ()
print ("""======================= =======================
          SELAMAT DATANG DI PIZZA 
     KELOMPOK 1 MANAJEMEN INFORMATIKA 23F     
======================= ======================= \n""" )
print ("                 SILAHKAN PILIH MENU                 ")
print ("""| ========== Pizza ========= | ===== Harga ====== | 
|   1. Frankfurter BBQ       |     Rp. 43.636     |
|   2. Meat Monsta           |     Rp. 43.636     |
|   3. Super Supreme         |     Rp. 43.636     |
|   4. Super Supreme Chicken |     Rp. 43.636     |""")
print ("------ ------ ------- ------- ------ ------ ------")


def pizza () :
    global harga_pizza
    global namaPizza
    global jumlah_pesanan

    harga_pizza = 0

    jumlah_pesanan = int(input("\nMasukan Jumlah Pesanan : "))
    pesan = str(input("\nMasukan Nomer Menu Yang Diinginkan : "))

    if pesan == "1" :
        namaPizza = "Frankfurter BBQ"
        harga_pizza = 43636
    elif pesan == "2" :
        namaPizza = "Meat Monsta"
        harga_pizza = 43636
    elif pesan == "3" :
        namaPizza = "Super Supreme"
        harga_pizza = 43636
    elif pesan == "4" :
        namaPizza = "Super Supreme Chicken"
        harga_pizza = 43636
    else :
        print("----- Maaf Pesanan Tidak Ada Di Dalam Menu -----")
        pizza()

def crust():
    global namaCrust
    global harga_crust

    harga_crust = 0
    # pilihCrust = str(input("Apakah Ingin Menambah Crust (Y/N) : "))
    # if pilihCrust == "Y":
    print ("\n                SILAHKAN PILIH Crust              ")
    print ("| ========== Crust =========== |" " ====== Harga ====== | ")
    print ("|   1. Pan                      |     Rp.      0     |")
    print ("|   2. StuffedCrust Cheese      |     Rp. 11.819     |")
    print ("|   3. StuffedCrust Sausage     |     Rp.  9.091     |")
    print ("|   4. Cheessy Bites            |     Rp. 13.637     |")
    print ("  ------ ------ ------- ------- ------ ------ ------")

    pilihCrust = str(input("\nSilahkan Pilih : ")) 
    if pilihCrust == "1" :
        namaCrust = "Pan"
        harga_crust = 0
    elif pilihCrust == "2" :
        namaCrust = "StuffedCrust Cheese"
        harga_crust += 11819
    elif pilihCrust == "3" :
        namaCrust = "StuffedCrust Sausage"
        harga_crust += 9091
    elif pilihCrust == "4" :
        namaCrust = "Cheessy Bites"
        harga_crust += 13637
    else :
        print("----- Maaf Crust Tidak Ada Di Dalam Menu -----")
        crust()
    # elif pilihCrust == "N":
    #     print ("")
    # else :
    #     print ("")
def ukuran() :
    global ukurann
    global namaUkuran
    global harga_ukuran

    # pilihUkuran [1="Y" or "y", ]
    print ("\n                SILAHKAN PILIH UKURAN             ")
    print ("| ========== Ukuran ========= |" " ====== Harga ===== | ")
    print ("|   1. Personal                 |     Rp.      0     |")
    print ("|   2. Regular                  |     Rp. 57.273     |")
    print ("|   3. Large                    |     Rp. 89.091     |")
    print ("  ------ ------ ------- ------- ------ ------ ------")

    ukurann = str(input("\nSilahkan Pilih : ")) 
    if ukurann == "1" :
        namaUkuran = "Personal"
        harga_ukuran = 0
    elif ukurann == "2" :
        namaUkuran = "Reguler"
        harga_ukuran = 57273
    elif ukurann == "3" :
        namaUkuran = "Large"
        harga_ukuran = 89091
    else :
        print("----- Maaf Ukuran Tidak Ada Di Dalam Menu -----")
        ukuran()

def xtracheese() :
    global cheese
    global tambahCheese
    global harga_cheese

    harga_cheese = 0

    tambahCheese = (input("Apakah Ingin Menambahkan Ekstar Cheese? (Y/N) : ")).upper()
    if tambahCheese == 'Y' :
        print("Extra Cheese Telah Ditambahkan")
        if ukuran == "1" :
            harga_cheese = 13636
        elif ukuran == "2" :
            harga_cheese = 16364
        else :
            harga_cheese = 19091
    else :
        print("")


pizza()
crust()
ukuran()
xtracheese()

# for 

harga = (harga_pizza + harga_crust + harga_ukuran + harga_cheese)*jumlah_pesanan
total = ("{:,}".format(harga))

# tambahCheese
# if tambahCheese == "Y":
#     print("Extra Cheese")
# else :
#     print("")

print("\n-----------RINCIAN PESANAN----------")
print ("Pizza : ",namaPizza,namaCrust,namaUkuran)
print ("Total Harga : Rp. ",total)
