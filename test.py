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

pizza()
# crust()
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
