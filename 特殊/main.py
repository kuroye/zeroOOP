class Student:
    
    raise_amount = 1.04

    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade
        self.email = name + '@student.com'


    def student_info(self):
        return f'{self.name}|{self.grade}|{self.email}'

    def apply_raise(self):
        self.grade = int(self.grade * self.raise_amount)

    # repr 方法用于调试
    def __repr__(self):
        return f"Student({self.name}, {self.grade}, {self.email})"

    # str 方法用于提高可读性
    def __str__(self):
        return self.student_info()


std_1 = Student('Kuroye',70)
std_2 = Student('Erhan',80)

# 定义特殊方法前只会返回此实例的内存地址
print(std_1)

# print(1+2)
# print('a' + 'b')