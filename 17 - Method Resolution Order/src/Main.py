#Method resolution order // multiple inheritance

class A :
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adalah Show B")

class C(B,A):
    pass
    # def show(self):
    #     print('ini adalah show C')

objek = C()
objek.show()