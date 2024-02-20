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

    def __str__(self) -> str:
        return self.student_info()

#国际学生
class InternationalStudent(Student):
    # 只会改变此子类的类变量值 如果不定义会从父类获取
    raise_amount = 1.10

    #定义一个init方法 不需要重复父类的init方法
    def __init__(self, name, grade, moth_lang):
        #调用父类的init方法handle
        super().__init__(name, grade)
        # 给新增的属于子类的字段新的定义逻辑 比如母语这个新变量
        self.moth_lang = moth_lang

# 班长
class ClassPresident(Student):
    
    def __init__(self, name, grade, students=None):
        super().__init__(name, grade)
        if students is None:
            self.students = []
        else:
            self.students = students

    # 添加几个班长类使用的方法
    def add_std(self, std):
        if std not in self.students:
            self.students.append(std)
    
    def remove_std(self, std):
        if std in self.students:
            self.students.remove(std)

    def print_stds(self):
        for emp in self.students:
            print('-->', emp.student_info())

int_std_1 = InternationalStudent('Kuroye',70, 'Kazakh')
int_std_2 = InternationalStudent('Yernar',80, 'Chinese')

cls_pst_1 = ClassPresident('Erhan', 90, [int_std_1])


print(int_std_1)
print(int_std_2)

print(int_std_1.moth_lang)

print(cls_pst_1.email)

cls_pst_1.print_stds()


# 此方法判断实列是不是这个类
print(isinstance(cls_pst_1, InternationalStudent))
# 此方法可以判断是否是父子类关系
print(issubclass(InternationalStudent, Student))