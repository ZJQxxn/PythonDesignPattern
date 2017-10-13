'''

ProductBuilder.py
__author__=zjq_1112@qq.com
=================
    2017.10.13

    Main Method:
        If we create two products.They have some same part 
        and other parts are different.If we seperately call
        the operation to build each part of it,it is complex
        and we cmay miss some part by accident.So we use bu-
        ilders to encapsulate the produce operations.

'''

class AbstractDesk:
    '''
    Abstract class of different desk
    
    Methods:
        produceLeg: Create leg of desk
        produceTop: Create top of desk
    '''
    def produceLeg(self):
        pass

    def produceTop(self):
        pass


class GlassDesk(AbstractDesk):
    '''
    Class of glass desks.
    
    Attributions:
        type: The type of this desk
        
    Methods:
        produceLeg: Create leg of desk
        produceTop: Create glass top of desk
    '''

    type='glass'

    def produceLeg(self):
        print("Produce legs of %s desk"%self.type)

    def produceTop(self):
        print("Produce top of %s desk"%self.type)


class WoodenDesk(AbstractDesk):
    '''
    Class of wooden desks.

    Attributions:
        type: The type of this desk

    Methods:
        produceLeg: Create leg of desk
        produceTop: Create wood top of desk
    '''

    type = 'wood'

    def produceLeg(self):
        print("Produce legs of %s desk" % self.type)

    def produceTop(self):
        print("Produce top of %s desk" % self.type)


class Builder:
    '''
    Encapsulate several produce operations.
    
    Attributions:
        desk:Class of the desk you want
        
    Methods:
        produce:Produce each part of this desk
    '''
    def __init__(self,deskType):
        self.desk=deskType()

    def produce(self):
        '''
        Produce each part of a desk
        :return:void 
        '''
        self.desk.produceLeg()
        self.desk.produceTop()


def produceDesk(deskType):
    '''
    Poduce different desk depending on 'deskType'
    :param deskType:Classname of the desk you want 
    :return: void
    '''
    builder=Builder(deskType)
    builder.produce()


if __name__ == '__main__':
    produceDesk(GlassDesk)
    produceDesk(WoodenDesk)