from threading import Condition

class GenProdCons:
    def __init__(self, size=10):
        assert size > 0, "Buffer size must be > 0"
        self.buffer = []
        self.size = size
        self.condition = Condition()

    def put(self, e):
        with self.condition:
            while len(self.buffer) >= self.size:
                self.condition.wait()
            self.buffer.append(e)
            self.condition.notify_all()

    def get(self):
        with self.condition:
            while len(self.buffer) == 0:
                self.condition.wait()
            value = self.buffer.pop(0)
            self.condition.notify_all()
            return value
        
    def __len__(self):
        return len(self.buffer)