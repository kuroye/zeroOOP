
# 类的定义方式
class Student:
    
    # 初始化 constructor
    def __init__(self, name, grade):
        
        # 属性
        self.name = name
        self.grade = grade
        self.email = name + '@student.com'

    # 注意 每一个函数必须传输实例(自己) 此函数以字符串的形式返回用户信息
    def student_info(self):
        return f'{self.name}|{self.grade}|{self.email}'

    # 这是toString 类型转换为字符串的函数 调用了student_info 函数
    def __str__(self) -> str:
        return self.student_info()

# std_1 和 std_2 是实例
std_1 = Student('Kuroye',11)
std_2 = Student('Yernar',9)


# 输出时会调用__str__函数
print(std_1)

# 可单独调用类里定义过的函数
print(std_2.student_info())