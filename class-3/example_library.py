#建立一個類別名為 Bear
class Bear:
    # Bear 的預設屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定義say_hello函數
    def say_hello(self):
        print("Hello my name is " + self.name)
        print("Im " + str(self.age) + " years old")

    def happy_birthday(self):
        self.age = self.age + 1


def bark(n):
    for i in range(n):
        print("ㄨㄤˋ")