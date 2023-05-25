import pytest
from ..max_path_sum import Triangle


@pytest.fixture
def sample_triangle():
    triangle_height = 4
    triangle_data = [(3,), (7, 4), (2, 4, 6), (8, 5, 9, 3),]
    return Triangle(triangle_height, triangle_data)


triangles_test_data = [
        (Triangle(0, []), 0),
        (Triangle(1, [(10,)]), 10),
        (Triangle(2, [(1,), (2, 3)]), 4),
        (Triangle(3, [(5,), (5, 10), (5, 10, 10)]), 25),
        (Triangle(4, [(3,), (10, 15), (20, 1, 15), (14, 15, 20, 10)]), 53)
    ]


class TestTriangle:
    def test_creation_of_triangle_sample_triangle_data(self, sample_triangle):
        triangle_data = sample_triangle.row_data
        triangle_height = sample_triangle.height
        triangle = Triangle(triangle_height, triangle_data)
        assert isinstance(triangle, Triangle)

    def test_creation_of_triangle_empty_row_data_list(self):
        zero_triangle = Triangle(height=0, row_data=[])
        assert isinstance(zero_triangle, Triangle)

    def test_max_total_sum_sample_triangle(self, sample_triangle):
        assert sample_triangle.max_total_sum() == 23

    @pytest.mark.parametrize(
        "triangle_in_test, max_total_sum", triangles_test_data
    )
    def test_max_total_sum_valid_triangles_data(self, triangle_in_test, max_total_sum):
        triangle = triangle_in_test
        expected_max_total_sum = max_total_sum
        actual_max_total_sum = triangle.max_total_sum()
        assert actual_max_total_sum == expected_max_total_sum
