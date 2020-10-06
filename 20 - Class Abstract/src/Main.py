#membuat class abstract
# abc = abstract base class
from abc import ABC, abstractclassmethod
class Button(ABC):

    @abstractclassmethod
    def click(self):
        pass

class PushButton(Button):
    
    def click(self):
        print('push button clicked')

tombol2 = PushButton()

tombol2.click()
help(tombol2)