class Question(object):
    """A class for answering my OO questions about python.

       attributes: a_number"""

    def __init__(self):
        print "You've initialized a Question!"

    def __str__(self):
        return "You've got an instance of the Question class there, bub."

    def myself_add(self, new_number):
        self.a_number += new_number

    def outer_add(self, new1, new2):
        # the first param of a class method is always self, even if you don't call it that
        return new1 + new2

    
if __name__ == '__main__':
    my_q = Question()
    print my_q
    my_q.a_number = 12
    print 'A number:',my_q.a_number
    my_q.myself_add(3)
    print 'A number:',my_q.a_number
    print 'Result:',my_q.outer_add(7, 6)


