import pytest
from tipgenerator.main import calculate_tip, split_bill


@pytest.mark.parametrize(
    "total_bill, tip_percent, expected", [(100, 10, 10), (100, 12, 12), (100, 15, 15)]
)
def test_calculate_tip(total_bill, tip_percent, expected):
    result = calculate_tip(total_bill, tip_percent)
    assert result == expected


@pytest.mark.parametrize(
    "total_bill, num_people, expected",
    [(100, 5, 20), (68, 8, 8.5), (100, 3, 33.33)],
)
def test_split_bill(total_bill, num_people, expected):
    result = split_bill(total_bill, num_people)
    assert result == expected
