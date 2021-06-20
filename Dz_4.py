from functools import wraps


def val_check(decorator_chek_func):
    def _val_check(funk_calc_cube):
        @wraps(funk_calc_cube)
        def wrapped(x):
            if decorator_chek_func(x):
                return funk_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped

    return _val_check


@val_check(lambda x: x > 0)
def calc_cube(x):
    return x ** 4


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
