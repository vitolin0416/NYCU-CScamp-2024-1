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
    
    def change_name(self, new_name): # new_name 為新的名字
        # Todo...

# # 建立名為Kumamon的物件
# Kumamon = Bear("熊本熊", 9)
# Kumamon.happy_birthday()
# Kumamon.say_hello()

# 建立名為Kumamon的物件
Kumamon = Bear("熊本熊", 9)
Kumamon.happy_birthday()
Kumamon.say_hello()
