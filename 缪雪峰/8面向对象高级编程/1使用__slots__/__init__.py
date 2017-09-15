class Student(object):
    pass

s=Student()
s.name='Michael'
print(s.name)

def set_score(self,score):
    self.score=score

Student.set_score=set_score

s.set_score(100)
print(s.score)


class Student(object):
    __slots__ = ('name','age')

s=Student()
s.name='Michael'
s.age=25
s.score=99
