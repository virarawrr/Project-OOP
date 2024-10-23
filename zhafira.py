# praktek Ke-3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Interaksi antar Objek

class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga 
        
    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
    
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []
    
    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
        
    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total 
    
class Pelayan:
    def __init__(self, nama):
        self.nama = nama 
        
    def ambil_pesanan(self, pelanggan):
        print(f"{self.nama} mengambil pesanan dari {pelanggan.nama}")
        
    def antar_pesanan(self, pelanggan):
        total = pelanggan.bayar()
        print(f"{self.nama} mengantarkan pesanan kepada {pelanggan.nama}")
        print(f"Total tagihan: ${total:.2f}")
        
class Burger:
    def __init__(self):
        self.menu ={
            "Bakso Aci": MenuItem("Bakso Aci", 12.00),
            "Mie Jebew": MenuItem("Mie Jebew", 10.00),
            "Es coklat": MenuItem("Es coklat", 05.00)
        }
        
    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print(f"Menyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.nama} tidak ada dalam manu")
                
            
            pelanggan = Pelanggan("Viraa")
            pelayan = Pelayan("Ncuyy")
            dapur = dapur()
            
            Bakso_Aci = MenuItem("Bakso Aci", 12.00)
            Mie_Jebew = MenuItem("Mie Jebew", 10.00)
            
            Pelanggan.pesan(Bakso_Aci)
            Pelanggan.pesan(Mie_Jebew)
            
            Pelayan.ambil_pesanan(Pelanggan)
            dapur.siapkan_Pesanan(Pelanggan.Pesanan)
            
            Pelayan.antar_Pesanan(Pelanggan)                                                