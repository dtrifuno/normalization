import pytest

from normalization.cardinals import cardinals2words


@pytest.mark.parametrize(
    "input,expected",
    [("од околу 3,7 милиони", "од околу три запирка седум милиони")],
)
def test_cardinals2words(input, expected):
    assert cardinals2words(input) == expected
