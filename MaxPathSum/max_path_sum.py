
class InvalidTriangleData(Exception):
    pass


class Triangle:
    def __init__(self, height: int, row_data: list[list]):
        self.height = height
        self.row_data = self.validate_row_data(height, row_data)

    def validate_row_data(self, height, row_data):
        if len(row_data) != height:
            raise InvalidTriangleData("Invalid triangle row data.")

        for row in enumerate(row_data, start=1):
            if len(row[1]) != row[0]:
                raise InvalidTriangleData("Invalid triangle row data.")

        return row_data

    def max_total_sum(self):
        if self.height == 0:
            return 0
        current_row_index = self.height - 1
        current_row = list(self.row_data[current_row_index])
        while current_row_index > 0:
            next_row = list(self.row_data[current_row_index - 1])
            for i in range(len(current_row) - 1):
                next_row[i] += max(current_row[i], current_row[i+1])
            current_row = next_row
            current_row_index -= 1
        return current_row[0]


if __name__ == "__main__":
    t = Triangle(4, [(3,), (7, 4), (2, 4, 6), (8, 5, 9, 3),])
    print(t.height)
    print(t.row_data)
    print(t.max_total_sum())





