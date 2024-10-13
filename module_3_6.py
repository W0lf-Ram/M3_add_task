def calculate_structure_sum(*args):
    total_sum = 0

    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            sub_sum = sum(calculate_structure_sum(item) for item in i)
            total_sum += sub_sum
        elif isinstance(i, dict):
            sub_sum = sum(calculate_structure_sum(k, v) for k, v in i.items())
            total_sum += sub_sum
        elif isinstance(i, type(None)):
            continue

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)