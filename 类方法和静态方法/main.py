class Student:
    
    num_of_std = 0
    raise_amount = 1.04

    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade
        self.email = name + '@student.com'

        Student.num_of_std += 1

    def student_info(self):
        return f'{self.name}|{self.grade}|{self.email}'

    def apply_raise(self):
        self.grade = int(self.grade * self.raise_amount)

    # 此方法为类方法 类方法的传参是类 而不是实例
    @classmethod    
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # 此方法为静态方法
    @staticmethod
    def is_schoolday(day):
        # python的自带判断星期的方法 0-6 0是周一 6是周日 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    def __str__(self) -> str:
        return self.student_info()

std_1 = Student('Kuroye',70)
std_2 = Student('Yernar',80)

# 调用类方法时 它会自动传输cls参数 只需手动传输自定义元素
Student.set_raise_amount(1.05)
# 上行相当于 Student.raise_amount = 1.05
# 类方法也可以通过实例进行调用 不过没人那么做 不合理

print(Student.raise_amount)
print(std_1.raise_amount)
print(std_2.raise_amount)

# 在使用类型时 
# 一般方法的第一个参数为实例 我们叫它self
# 类方法的第一个参数为类型 我们叫它cls
# 静态方法不会自动传任何参数 它会像一般函数一样工作 尽管静态方法不会使用到实例和类 我们也会把它写在类里面 因为它和类有某种逻辑连接

# 举个例子说 我们想要在Student类里添加一个接收日期并返回布尔值的方法来判断此日期是上学日还是休息日

import datetime
my_date = datetime.date(2024, 1, 9)

print(Student.is_schoolday(my_date))