def file_open(filename):
    try :
        with open (filename,'r+')as file_object:
            msg=file_object.read()
            print (msg.rstrip())
            return msg
    except FileNotFoundError:
        print ("无法找到文件"+filename)
def file_add_write(filename,add_msg):
    file_msg=file_open(filename)
    file_msg+=add_msg
    try :
        with open (filename,'w+')as file_object:
            """需要载入模式为W+,否则会没有read的权限"""
            file_object.write(file_msg)
            msg=file_object.read()
            print(msg)
    except FileNotFoundError:
        print ("无法找到文件"+filename)

class File_test():
    def __init__(self,filename):
        self.filename = filename

    def file_change(self):
        try :
            with open (self.filename)as file_object:
                msg=file_object.read()
        except FileNotFoundError:
            print ("无法找到文件"+self.filename)
        try :
            msg=int(msg)
        except ValueError:
            msg=float(msg)
        print (msg*10)
        return msg
    def file_write(self):
        msg = file_open(self.filename)
        msg =float(msg)+123
          
filename="test.txt"
file_open(filename)
a=File_test(filename)
file_add_write(filename,"\n123456789")