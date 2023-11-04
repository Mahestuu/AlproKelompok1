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

pizza()
crust()
# ukuran()
# xtracheese()

# for 

harga = (harga_pizza )*jumlah_pesanan
total = ("{:,}".format(harga))

# tambahCheese
# if tambahCheese == "Y":
#     print("Extra Cheese")
# else :
#     print("")

print("\n-----------RINCIAN PESANAN----------")
print ("Pizza : ",namaPizza)
print ("Total Harga : Rp. ",total)
