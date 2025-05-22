from threading import Semaphore, Lock

class GenProdCons:
    def __init__(self, size=10):
        assert size > 0, "Buffer size must be > 0"
        self.buffer = []
        self.size = size
        self.empty = Semaphore(size)  
        self.full = Semaphore(0)      
        self.mutex = Lock()           

    def put(self, e):
        self.empty.acquire()      
        with self.mutex:            
            self.buffer.append(e)
        self.full.release()      

    def get(self):
        self.full.acquire()      
        with self.mutex:          
            value = self.buffer.pop(0)
        self.empty.release()  
        return value

    def __len__(self):
        with self.mutex:
            return len(self.buffer)
