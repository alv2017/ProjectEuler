import pytest

from ..lattice_path import lattice_routes


@pytest.fixture(scope="module")
def known_lattice_routes():
    return [
        {"m": 1, "n": 1, "routes": 2},
        {"m": 2, "n": 2, "routes": 6},
        {"m": 3, "n": 2, "routes": 10},
        {"m": 2, "n": 3, "routes": 10},
        {"m": 3, "n": 3, "routes": 20},
    ]


@pytest.fixture(scope="module")
def invalid_lattices():
    return [{"m": 0, "n": 1}, {"m": 1, "n": 0}, {"m": 501, "n": 1}, {"m": 1, "n": 501}]


class TestLatticeRoutes:
    def test_valid_lattices(self, known_lattice_routes):
        for item in known_lattice_routes:
            m = item["m"]
            n = item["n"]
            expected_routes = item["routes"]
            calculated_routes = lattice_routes(m, n)
            assert calculated_routes == expected_routes

    def test_invalid_lattices(self, invalid_lattices):
        for item in invalid_lattices:
            m = item["m"]
            n = item["n"]
            with pytest.raises(ValueError, match="Invalid Lattice Size"):
                lattice_routes(m, n)
