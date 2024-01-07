from sys import getsizeof


class Serialization:

    def __init__(self):
        pass

    @staticmethod
    def deserialize(serialize):
        deserialized = []
        pairs = serialize.split(',')

        for pair in pairs:
            num, count = map(int, pair.split(':'))
            deserialized.extend([num] * count)

        return deserialized

    @staticmethod
    def serialize(numbers):
        serialized = []
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1]:
                count += 1
            else:
                serialized.append(str(numbers[i - 1]) + ':' + str(count))
                count = 1
        serialized.append(str(numbers[-1]) + ':' + str(count))  # Для последнего числа
        return ','.join(serialized)

    @staticmethod
    def compress_ratio(serialized, original):
        return getsizeof(serialized) / getsizeof(original)
