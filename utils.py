
def provide_inputs(func):
    def wrapper():
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        return func(inputs=lines)
    return wrapper
