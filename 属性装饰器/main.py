class Student:
    
    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade
        # self.email = name + '@student.com'   # 此逻辑定义到第10行了 可自行解开注释实验一下有何区别

    @property
    def email(self):
        return f'{self.name}@student.com'

    # @property
    # def name(self):
    #     return self._name
    # @name.setter
    # def name(self, value):
    #     self._name = value

    def student_info(self):
        return f'{self.name}|{self.grade}|{self.email}'


std_1 = Student('Kuroye',11)
print(std_1.name)
print(std_1.email)
print(std_1.student_info())
print('---修改后---')

std_1.name = 'Erhan'

# 此变量变为 Erhan
print(std_1.name)

# 在为email添加getter(@property)前 此变量还是 Kuroye@student.com
print(std_1.email)

# 在为email添加getter(@property)前 此变量里name改变了 email没变
print(std_1.student_info())

# 若想email一同改变的话 可以在class里定义一个方法
# 如 第10行
# 这有一个问题 变量变为方法后 需要修改的地方会变多
# print(std_1.email())

# 所以应使用python里的属性装饰器使方法像变量
# 如 第9行
print(std_1.email)

# @property装饰器可视为getter
# python里setter的写法为
# @name.setter
# def name(self, value):
#     self._name = value