import pytest

from normalization.cardinals import cardinals2words
from normalization.fleurs import process


@pytest.mark.parametrize(
    "input,expected",
    [("од околу 3,7 милиони", "од околу 3,7 милиони")],
)
def test_cardinals2words(input, expected):
    # assert cardinals2words(input) == expected
    assert process(input) == expected
