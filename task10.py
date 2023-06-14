class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def join(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'A'
            return 5
        raise MealyError('join')

    def edit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 8
        raise MealyError('edit')

    def move(self):
        if self.state == 'D':
            self.state = 'A'
            return 7
        if self.state == 'C':
            self.state = 'C'
            return 4
        raise MealyError('move')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    o.join()  # 1
    o.edit()  # 0
    o.join()  # 2
    o.edit()  # 3
    o.move()  # 7
    o.join()  # 1
    o.edit()  # 0
    o.join()  # 2
    o.move()  # 4
    o.move()  # 4
    o.edit()  # 3
    o.edit()  # 6
    o.edit()  # 8
    o = main()
    o.edit()  # 0
    o.join()  # 2
    o.move()  # 4
    o.edit()  # 3
    o.move()  # 7
    o.join()  # 1
    raises(lambda: o.move(), MealyError)
    o.edit()  # 0
    o.join()  # 2
    o.edit()  # 3
    raises(lambda: o.join(), MealyError)
    o.edit()  # 6
    o.edit()  # 8
    raises(lambda: o.edit(), MealyError)
    o = main()
    o.edit()  # 0
    o.join()  # 2
    o.join()  # 5
