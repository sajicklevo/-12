Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене

class Tovar:
    def __init__(self, itemname, storename, price):
        self.itemname = itemname
        self.storename = storename
        self.price = price

    def getitemname(self):
        return self.itemname

    def getstorename(self):
        return self.storename

    def getprice(self):
        return self.price
    def setprice(self, newprice):
        self.price = newprice
        return self.price
class Sklad:
    def __init__(self):
        self.tovars = []


    def addproduct(self, product):
        self.tovars.append(product)
        return self.tovars

    def findproductbyindex(self, index):
        if index < len(self.tovars):
            return self.tovars[index]
        else:
            return None

    def findproductbyname(self, name):
        for product in self.tovars:
            if product.getitemname() == name:
                return product
            else:
                return None

    def allproducts(self):
        for prod in self.tovars:
            print(f'Product: {prod.getitemname()}, Store: {prod.getstorename()}, Price: {prod.getprice()}')

    def removeproductbyindex(self, index):
        if index < len(self.tovars):
            self.tovars.pop(index)
            return True
        else:
            return False

    def removeproductbyname(self, name):
        for product in self.tovars:
            if product.getitemname() == name:
                self.tovars.remove(product)
                return True
            else:
                return False
sklad = Sklad()
tovar1 = Tovar("Pizza", " cafe", 500)
tovar2 = Tovar("CAT", " Shop", 1200)
tovar3 = Tovar("DOG", "shop", 300)

sklad.addproduct(tovar1)
sklad.addproduct(tovar2)
sklad.addproduct(tovar3)

print(sklad.findproductbyindex(0).getitemname())
print(sklad.findproductbyindex(1).getstorename())
print(sklad.findproductbyindex(2).getprice())

sklad.allproducts()

sklad.removeproductbyindex(1)
sklad.allproducts()
