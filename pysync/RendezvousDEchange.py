from threading import Condition

class RendezvousDEchange:
    def __init__(self):
        self.condition = Condition()
        self.first_value = None
        self.has_first = False

    def echanger(self, value):
        with self.condition:
            if not self.has_first:
                self.first_value = value
                self.has_first = True
                self.condition.wait()
                other_value = self.second_value
                self.has_first = False
                self.condition.notify()
                return other_value
            else:
                self.second_value = value
                self.condition.notify()
                self.condition.wait()
                return self.first_value