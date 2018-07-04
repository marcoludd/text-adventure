'''
    Store
'''

class Store:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Store, cls).__new__(cls)
            return cls._instance
    
    def __init__(self):
        self.store_inventory = list()
