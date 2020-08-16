from math import ceil, floor, log10


class Number():
    def __init__(self, value, type):
        self.value = value
        self.type = type


class float(Number):
    def __init__(self, value):
        super().__init__(value, 'float')

    def added_to(self, other):
        if isinstance(other, Number):
            error = other.error if other.type == 'sfloat' else None
            value = self.value + other.value

            sig_figs = ceil(log10(value)) - ceil(log10(error)) if error else None

            return sfloat(value, sig_figs) if sig_figs else float(value)

    def __repr__(self):
        return f'{self.value}'


class sfloat(Number):
    def __init__(self, value, sig_figs=None):
        super().__init__(value, 'sfloat')
        self.value = round(value, sig_figs - int(floor(log10(abs(value)))) - 1) if sig_figs is not None else value
        self.sig_figs = sig_figs if sig_figs else len(str(self.value).replace('.', ''))
        self.error = 5 * (10 ** (floor(log10(self.value)) - self.sig_figs))

    def added_to(self, other):
        if isinstance(other, Number):
            if other.type == 'sfloat':
                error = (self.error + other.error) / 5
                error = 5 * (10 ** (floor(log10(error))))
            else:
                error = self.error
            value = self.value + other.value

            sig_figs = ceil(log10(value)) - ceil(log10(error))

            return sfloat(value, sig_figs)

    def __repr__(self):
        return f'{self.value} ({self.sig_figs} s.f.) : {self.error}'


val_1 = sfloat(1.23, 2)
val_2 = sfloat(1.0011276, 4)
val_2 = float(0.5223)

print(val_2.added_to(val_2))
