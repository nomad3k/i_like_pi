import re
import random

"""
The following characters are to be treated as equal, to compensate for
potential human error.
"""
mistaken_characters = {
    'O': '0',
    'I': '1',
    'Z': '2',
    'S': '5',
    'B': '8',
    'Q': '0',
}
valid_characters = [chr(c) for c in list(range(ord('A'), ord('Z'))) + list(range(ord('0'), ord('9'))) if chr(c) not in mistaken_characters]

# potential characters = 26 + 10 - 6 = 30
# permutations = 30^9 = 19,683,000,000,000

"""
Could have restricted the regex, but decided to deliberately made the regex wide
so that we don't need to duplicate the mistaken_characters and keep both map and
regex in line.
"""
valid_product_id = r"^[A-Z0-9]{3}-[A-Z0-9]{3}-[A-Z0-9]{3}$"


def is_valid(product_id: str):
    return re.match(valid_product_id, product_id, re.IGNORECASE)


def is_valid_strict(product_id: str):
    return re.match(valid_product_id, product_id) \
        and not any(c in mistaken_characters for c in product_id)


def normalise(product_id: str):
    """
    Converts the product_id to uppercase and replaces any potential mistaken characters.
    We should only ever store and compare the normalised product ids.
    """
    return "".join([mistaken_characters[c] if c in mistaken_characters else c for c in product_id.upper()])


def are_equal(a: str, b: str):
    return normalise(a) == normalise(b)


def generate():
    max = len(valid_characters) - 1
    plain = "-".join(["".join([valid_characters[random.randint(0, max)] for _ in range(r)]) for r in [3,3,3]])
    return plain
