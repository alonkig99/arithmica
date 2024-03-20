class Token:
    def __init__(self, type_, value=None, sign=None):
        self.type = type_
        self.value = value  # int val
        self.sign = sign

    def __repr__(self):
        if self.value: return f'{self.type}:{self.sign}:{self.value}'
        return f'{self.type}'

    def matches(self, type_, value):
        return self.type == type_ and self.value == value
