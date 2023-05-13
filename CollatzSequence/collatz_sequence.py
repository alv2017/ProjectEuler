
class CollatzSequence:
    sequence_length_memory = [0, 1]
    sequence_max_length_memory = [0, 1]

    def __init__(self, max_size):
        self.max_size = max_size
        dt = max_size + 1 - len(self.sequence_length_memory)
        if dt > 0:
            self.sequence_length_memory += [0] * dt
            self.sequence_max_length_memory += [0] * dt

        self._generate_sequence_max_length_data()

    def _generate_sequence_max_length_data(self):
        previous_item = 1
        previous_length = 1
        for i in range(2, self.max_size + 1):
            slen = self.sequence_length(i)
            if slen >= previous_length:
                self.sequence_max_length_memory[i] = i
                previous_item = i
                previous_length = slen
            else:
                self.sequence_max_length_memory[i] = previous_item

    @staticmethod
    def collatz_sequence(start: int) -> list:
        """ Returns Collatz sequence for a given start value
        :param start: Collatz sequence start value
        :return: Collatz sequence
        """
        n = start
        sequence = [n]
        while n != 1:
            n = 3 * n + 1 if n % 2 else n // 2
            sequence.append(n)
        return sequence

    def sequence_length(self, start: int) -> int:
        slen = 0
        n = start

        if n == 1:
            return 1

        while n != 1:
            if n < self.max_size + 1 and self.sequence_length_memory[n] > 0:
                self.sequence_length_memory[start] = slen + self.sequence_length_memory[n]
                return self.sequence_length_memory[start]

            slen += 1
            n = (3 * n + 1) if n % 2 else (n // 2)
        # we need to include start value and 1 to the sequence
        self.sequence_length_memory[start] += 2
        return self.sequence_length_memory[start]

    def get_max_length_item(self, n):
        if n <= self.max_size:
            return self.sequence_max_length_memory[n]
        else:
            raise ValueError(f"Item value can not exceed the max_size parameter.")


