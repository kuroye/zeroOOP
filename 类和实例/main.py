
# 类的定义方式
class Student:
    
    # 初始化 constructor
    def __init__(self, name, grade):
        
        # 属性
        self.name = name
        self.grade = grade
        self.email = name + '@student.com'

    # 注意 每一个函数必须传输实例(自己)
    def student_info(self):
        return '{}|{}|{}'.format(self.name, self.grade, self.email)




