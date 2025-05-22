from threading import Semaphore

class RendezvousDEchange:
    def __init__(self):
        self.semaphore_first = Semaphore(0) 
        self.semaphore_second = Semaphore(0) 
        self.first_value = None
        self.second_value = None
        self.has_first = False
        self.has_second = False

    def echanger(self, value):
        if not self.has_first:
            self.first_value = value
            self.has_first = True

            self.semaphore_second.acquire()
            result = self.second_value

            self.has_first = False
            self.has_second = False

            self.semaphore_first.release()
            return result
        else:
            self.second_value = value
            self.has_second = True

            self.semaphore_second.release()

            self.semaphore_first.acquire()
            return self.first_value
