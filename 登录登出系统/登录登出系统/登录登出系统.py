import json
import sys
sys.path.append(r'E:\VS2017_GIT\test_1.1\test_1.1\shot_alien.py')
'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''
import shot_alien as sa


def write_json_file(filename,moudel,data):
    """将data写入json文件中"""
    with open (filename,moudel) as f_obj:
        json.dump (data,f_obj)

def read_json_file(filename,moudel):
    """读取json文件的信息"""
    try :
        with open(filename,moudel)as f_obj:
            data = json.load(f_obj)
        print (data)
        return data
    except FileNotFoundError:
        print ("没有找到你想要的文件")

def push_data(data):
    """将用户名提取到列表内,返回列表"""
    user_names=[]
    for user_name in data.keys():
        user_names.append(user_name)#在列表尾部添加用户名
    return user_names

def check_user_in(user_name,data):
    """检查用户名是否在用户名列表中"""
    user_names = push_data(data)
    if user_name in user_names:
        return True
    else :
        return False

def new_user(msg3,data):
    """创建用户及密码"""
    if msg3 == 'yes':
        name= input("用户名是: ")
        password = input ("密码是: ")
        data[name]= password
        write_json_file("测试.json",'w',data)
        if check_user_in(name,data) :
            print("新用户 " + name + " 创建成功")
        else :
            print ("新用户创建失败!!!")
    elif msg3== 'q':
        print ("退出系统")

def check_user_name(data):
    """登录用户及密码检查"""
    msg1=input("你的用户名是什么:")
    password = input("密码是: ")
    if check_user_in(msg1,data):
        if password == data[msg1]:
            print ("欢迎"+msg1)
            print ("密码正确!")
            sa.run_game()
        else:
            print ("密码或用户名错误!!!")
            print ("你是否想创建一个新的用户 ? ")
            msg3=input("创建输入yes,退出输入q: ")
            new_user(msg3,data)
    else:
        print ("你是否想创建一个新的用户 ? ")
        msg3=input("创建输入yes,退出输入q: ")
        new_user(msg3,data)



filename='测试.json'
data=read_json_file(filename,"r")
check_user_name(data)

