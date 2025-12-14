def get_median(numbers):
    return (
            (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) + 1]) / 2) \
        if len(numbers) % 2 == 0 else numbers[len(numbers) // 2]


def standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    res = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return res ** 0.5


def generate_statistics(numbers):
    stats = {
        'mean': sum(numbers) / len(numbers),
        'median': get_median(numbers),
        'standard_deviation': standard_deviation(numbers),
    }

    return stats


stats = generate_statistics([1, 2, 3, 4, 5])
print(stats)
