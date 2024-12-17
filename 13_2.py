class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError("Початкове значення виходить за межі допустимого діапазону.")

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max
            if self.current > self.max_value:
                self.current = self.max_value
        else:
            raise ValueError("Максимальне значення не може бути менше мінімального.")

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min
            if self.current < self.min_value:
                self.current = self.min_value
        else:
            raise ValueError("Мінімальне значення не може бути більше максимального.")

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Достигнуто максимуму.")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Достигнуто мінімуму.")

    def get_current(self):
        return self.current


# Тестування класу
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто максимуму
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто мінімуму
assert counter.get_current() == 7, 'Test4'
