ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0.

class PheloSlon:
    def __init__(self, bee, elephant):
        self.bee = min(100, max(0, bee))
        self.elephant = min(100, max(0, elephant))

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            self.bee = min(100, max(0, self.bee + value))
        elif meal == "grass":
            self.bee -= value
            self.elephant = min(100, max(0, self.elephant + value))

pheloslon = PheloSlon(30, 70)
print(pheloslon.fly())
print(pheloslon.trumpet())
pheloslon.eat("nectar", 20)
print(f"Bee: {pheloslon.bee}, Elephant: {pheloslon.elephant}")
