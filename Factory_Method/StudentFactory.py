'''

StudentFactory.py
__author__=zjq_1112@qq.com
==========================

Main Method:
    If we want to change class type easily in customer's
    side and do not break the encapsulation priciple, 
    we can use factory method.
'''

class Student:
    '''
    Abstract class for different type of students
     
     Methods:
         learn
         play
    '''

    def learn(self):
        pass

    def play(self):
        pass


class PrimaryStudent(Student):
    '''
    Class for primary students
    
    Attributions:
        type:Type of student
    
    Methods:
        learn
        play
    '''

    type='primary student'

    @classmethod
    def learn(cls):
        print('%s is learning' % cls.type)

    @classmethod
    def play(cls):
        print('%s is playing' % cls.type)


class CollegeStudent(Student):
    '''
    Class for college students.
    
    Attributions:
        type:Type of student
    
    Methods:
        learn
        play
    '''

    type='college student'

    @classmethod
    def learn(cls):
        print('%s is learning' % cls.type)

    @classmethod
    def play(cls):
        print('%s is playing'%cls.type)


class Home:
    '''
    Abstract class for home
    
    Methods:
        at_home
    '''

    @classmethod
    def at_home(cls):
        pass


class PrimaryHome(Home):
    '''
    Class for a home of primary student
    
    Methods:
        at_home
    '''
    @classmethod
    def at_home(cls):
       PrimaryStudent.learn()
       PrimaryStudent.play()


class CollegeHome(Home):
    '''
    Class for a home of college student

    Methods:
        at_home
    '''

    @classmethod
    def at_home(cls):
        CollegeStudent.learn()
        CollegeStudent.play()


if __name__ == '__main__':
    '''
    It is easy to change factory.The concrete
    operations is decides by factory in the 
    side of customers.The coder don't care 
    about what exactly factory the customer 
    want to use.But you need to add many
    codes if you want to add a new 'Student'.
    The good news is that you won't break the 
    capsulations principle in this way.
    '''
    CollegeHome.at_home()
    PrimaryHome.at_home()
