
class Student:
    
    # 这是类变量 写在类里 类变量可从类调用 (Student.num_of_std) 也可从实例调用(instance.num_of_std)
    num_of_std = 0
    raise_amount = 1.04

    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade
        self.email = name + '@student.com'

        # 每当多一个学生实例 学生总数就得+1 所以num of std这个类变量要写在 init函数里
        # 这里选择了以类调用类变量的方式 因为此值应总体改变 而不只是为单一实例服务
        Student.num_of_std += 1

    def student_info(self):
        return f'{self.name}|{self.grade}|{self.email}'

    # 注意这里的raise_amount是根据实例调用的类变量 修改实例调用的类变量只改变该实例对应的类变量 而不是类的类变量 
    def apply_raise(self):
        self.grade = int(self.grade * self.raise_amount)

    def __str__(self) -> str:
        return self.student_info()

std_1 = Student('Kuroye',70)
std_2 = Student('Yernar',80)

# 仅改变std_1实例的raise_amount 其他不变
print('仅改变std_1实例的raise_amount 其他不变')
std_1.raise_amount = 1.05
print('类调用的类变量: ' + str(Student.raise_amount))
print('std_1实例调用的类变量: ' + str(std_1.raise_amount))
print('std_2实例调用的类变量: ' + str(std_2.raise_amount))
# 这里做个笔记 为什么实例(__init__函数)根本没有定义raise amount 依然能调用? 因为实例里没有raise amount就会从类里面面获取

# 调用函数修改了grade的值
print('调用函数修改了std_1实例grade的值')
print(std_1.grade)
std_1.apply_raise()
print(std_1.grade)

# 学生总数
print(Student.num_of_std)