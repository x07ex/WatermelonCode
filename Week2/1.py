def _main(num: int, matrix: tuple or list) -> str:
    matrix = matrix.split('\n')
    if num % 2 != 0 and len(matrix[0]) % 2 != 0:
        return f"{matrix}\nYes"
    else:
        return f"{matrix}\nNo"

print(_main(3, '\n'.join(['1 0 0', '0 0 1', '0 1 0'])))