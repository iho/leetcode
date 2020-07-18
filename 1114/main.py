import threading
class Foo(object):
    def __init__(self):
        self.second_lock = threading.Lock()
        self.third_lock = threading.Lock()
        self.third_lock.acquire()
        self.second_lock.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.second_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_lock.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        self.third_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()