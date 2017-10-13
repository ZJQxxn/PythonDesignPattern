'''

PrintFactory.py
__author__=zjq_1112@qq.com
================
    2017.10.13  
    Main methods:    
        Using abstract factory pattern to implement two different
        simple print class. class:'SinglePrint' print a sentence 
        in a single line while class:'SeperatePrint' seperates t
        he sentence and print words each a line.
    Advantages:
        It is easy to change the 'factory' so that you can get
        different result.
    Disadvantages:
        It takes a lot of work to change something inside the 
        factory classes.You need to change every one of them.
'''


class SinglePrint:
    '''
    Print a sentence in a single line.
    
    Attributions:
        text: An instance of class:'Text' to store the sentence.
                
    '''

    def __init__(self, sentence=''):
        self.text = self.Text(sentence)

    class Text:
        '''
        Store the string sentence.
        
        Attributions:
            sentence: The string you want to store.
            
        Methods:
            print() : Print the sentence.      
        '''
        def __init__(self,sentence):
            '''
            Init a instance with a string.
            :param sentence: A string you want to print.
            '''
            self.sentence=sentence

        def print(self):
            '''
            Print self.sentence in asingle line.
            :return: void
            '''
            print("Print in asingle line:")
            print(self.sentence)


class SeperatePrint:
    '''
    Print a sentence each word a line.
        
    Attributions:
        sentence : The sentence you want to print.
                
    Methods:
        print() : Print the sentence.      
    '''

    def __init__(self,sentence):
        '''
        Init a instance with a string.
        :param sentence: A string you want to print.
        '''
        self.text=self.Text(sentence)

    class Text:
        '''
        Store the string sentence.

        Attributions:
            sentence: The string you want to store.

        Methods:
            print() : Print the sentence.      
        '''
        def __init__(self, sentence):
            '''
            Init a instance with a string.
            :param sentence: A string you want to print.
            '''
            self.sentence = sentence

        def print(self):
            '''
            Print the sentence seperately.
            :return: void
            '''
            print("Print in asingle line:")
            words=self.sentence.split()
            for each in words:
                print(each)


def print_sentence(factory,sentence):
    '''
    Print a sentence in the way 'factory' implements.
    :param factory: The print factory you want to use.
    :param sentence: The sentence you want to print.
    :return: void
    '''
    pr=factory(sentence)
    pr.text.print()


if __name__ == '__main__':
    print_sentence(SinglePrint,'Hello world')
    print_sentence(SeperatePrint,'Hello world')


