import pytest
from pi_domain.product_id import is_valid_strict, is_valid, are_equal, normalise, generate

@pytest.mark.parametrize("product_id", [
    "AAA-AAA-AAA",
    "A8C-DEF-GH1",
    "346-79A-AAA"
])
def test__is_valid_strict__success(product_id):
    actual = is_valid_strict(product_id)
    assert actual, f"'{product_id}' is invalid"

@pytest.mark.parametrize("product_id", [
    "aaa-aaa-aaa",
    "OOO-OOO-OOO",
    "III-III-III",
    "ZZZ-ZZZ-ZZZ",
    "SSS-SSS-SSS",
    "BBB-BBB-BBB",
    "QQQ-QQQ-QQQ",
])
def test__is_valid_strict__fail(product_id):
    actual = not is_valid_strict(product_id)
    assert actual, f"'{product_id}' is invalid"

@pytest.mark.parametrize("product_id", [
    "aaa-aaa-aaa",
    "0AA-AAA-AAA",
    "1AA-AAA-AAA",
    "2AA-AAA-AAA",
    "5AA-AAA-AAA",
    "8AA-AAA-AAA",
])
def test__is_valid__success(product_id):
    actual = is_valid(product_id)
    assert actual, f"{product_id} is invalid"

@pytest.mark.parametrize("product_id,expected", [
    ["ABC-DEF-GHI", "A8C-DEF-GH1"],
    ["abc-def-ghi", "A8C-DEF-GH1"],
    ["OIZ-SBQ-AAA", "012-580-AAA"]
])
def test__normalise(product_id: str, expected: str):
    actual = normalise(product_id)
    assert actual == expected, f"{product_id} != {expected}"

@pytest.mark.parametrize("a,b", [
    ["ABC-DEF-GHI", "ABC-DEF-GHI"],
    ["ABC-DEF-GHI", "abc-def-ghi"],
])
def test__product_ids_are_equal(a: str, b: str):
    actual = are_equal(a, b)
    assert actual, f"'{a}' != '{b}'"




def p(x):
    print (x)
    return x


def test_foo():
    actual = generate()
    assert is_valid(actual), actual
