class number():
    def __init__(self, value, type_):
        self.value = value
        self.type = type_

    def __repr__(self):
        return f'{self.type}: {self.value}'


class string():
    def __init__(self, value, type_):
        self.value = value
        self.type = type_

    def __repr__(self):
        return f'{self.type}: {self.value}'


class run():
    def __init__(self):
        method = getattr(self, 'number')


run()
