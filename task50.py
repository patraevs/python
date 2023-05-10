# todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в
# верхний регистр и возвращает их в виде списка текстовых аргументов.

def dec_arg_str(func):
    def _wrapper(*args, **kwargs):
        func(*args)
        return [x.upper() for x in args if isinstance(x, str)]
    return _wrapper


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)


@dec_arg_str
def msum(matrix, str1, str2):
    result = sum([matrix[i][j] for i in range(len(matrix))
                  for j in range(len(matrix[i]))])
    return result


print(msum(matrix, 'GHufd', 'sdgfsdf'))
