class Dog():
    """简单的模拟小狗"""
    def __init__(self,name,age):
        """包含名字,年龄"""
        self.name=name
        self.age=age
    def sit(self):
        """小狗坐下"""
        print (self.name.title()+"is sitting now !")
    def roll_around(self):
        print (self.name.title()+"is roll aronud !")
    def get_age(self):
        print (self.name.title()+"已经 "+str(self.age)+" 岁了")
class Cat ():
    """ 简单的模拟小猫咪"""
    def __init__(self,name,age,type):
        """包含名字,年龄,种类"""
        self.name = name
        self.age = age 
        self.type = type
    def get_type(self):
        return self.type
