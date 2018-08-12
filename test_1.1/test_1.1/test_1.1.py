
import pygame1 as pyg_1

my_dog = pyg_1.Dog('lucky',11)
my_dog.get_age()
my_dog.roll_around()
#测试类的使用方法,,
my_cat = pyg_1.Cat('wiill',3,'美短')
my=my_cat.get_type()
print (my)#得到猫的种类
a={'cat_type':"美短",'age':"6"}
for name,age in a.items():#输出键值,使用items()
    print (name)
    print (age)
print("hello world !")
print("测试分支!")