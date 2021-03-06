class Mangga:
    
    #magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):#saat debugging
        return "Debug --- Mangga: {} Jumlah: {}".format(self.nama,self.jumlah)

    def __str__(self):#saat release
        return "Mangga: {} Jumlah: {}".format(self.nama,self.jumlah)

    def __add__(self,objek):#untuk memproses aritmatika antar objek
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga('arumanis',10)
belanja2 = Mangga('mana lagi',5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)