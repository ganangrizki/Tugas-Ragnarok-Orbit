from abc import abstractmethod, ABC


class hewan(object):
    def __init__(self, jenis, tempat, makanan):
        self.jenis = jenis
        self.tempat = tempat
        self.makanan = makanan
    
    def h(self, durasi):
        for i in range(durasi):
            print("jenis hewan")
            
    def info(self):
        print(f"jenis: {self.jenis}\nTempat tinggal: {self.tempat}\nMakanan: {self.makanan}")

        
class Harimau(hewan):
    def __init__(self, jenis, tempat, makanan,keturunan):
        super().__init__(jenis, tempat, makanan)
        self.keturunan= keturunan
        
        
    def ab(self, durasi):
        for i in range(durasi):
            print("ini adalah harimau.")
            
            
class Komputer(object):
    
    def __init__(kp, input_merk, input_so, input_ram, input_dayalistrik):
        kp.merk = input_merk
        kp.so = input_so
        kp.ram = input_ram
        kp.dayalistrik=input_dayalistrik

    def ddr(kp, kmp):
        for x in range(kmp):
            print(" 8memory")

    def info(kp):
        print(f"merk: {kp.merk}, so: {kp.so}, ram:{kp.ram}, dayalistrik :{kp.dayalistrik}")


computers1 = Komputer("Acer", "windows", "8gb", "220-250w")

computers1.info()
        

merk= "LG"
warna= "hitam"
barang = "Televisi"
dayalistrik = " 50-100watt"

def tv():
    print("Televisi 30in...")
    
def info_tv(merk,warna,barang,dayalistrik):
    print(f"merk: {merk}, warna: {warna}, barang:{barang}, dayalistrik :{dayalistrik}") 

info_tv(merk,warna,barang,dayalistrik)
tv()


class Hewan(ABC):
    
    @abstractmethod
    def caramemakan(self):
        pass
    
class Harimau(Hewan):
    def caramemakan(self):
        print("Menjatuhkan ke tanah dan mematahkan atau menggigit lehernya hingga mati.\n")
        
class Buaya(Hewan):
    def caramemakan(self):
        print("cara makanya dengan menerkam sekaligus menggigit mangsanya kemudian menarik dengan kuat dan tiba-tiba ke air.")
harimau1=Harimau()
buaya1=Buaya()

harimau1.caramemakan()
buaya1.caramemakan()