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
        
