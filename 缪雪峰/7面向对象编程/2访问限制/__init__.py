class Student(object):

    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s : %s ' %(self.__name,self.__score))

bart = Student('Bart Simpson', 98)
# print(bart.__name)

print(bart._Student__name)