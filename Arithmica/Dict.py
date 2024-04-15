# Class that defines the interpreter's dictionary that manages assigned variables
class Dict:
    def __init__(self):
        self.dict = {}

    def get(self, name):
        value = self.dict.get(name, None)
        return value

    def set(self, var_name, value):
        self.dict[var_name] = value

    def remove(self, name):
        del self.dict[name]