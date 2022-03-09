from abc import abstractmethod, ABC

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
       
    harimau1=Harimau
    (buaya1=Buaya()

   buaya1.buaya()
   buaya1.caramakan()
