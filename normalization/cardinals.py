from normalization.base import RESub
from num2words import num2words

patterns = r"\d{1,3}(?:[.]\d{3})*(?:,\d+)?|\d+(,\d+)?"


def cardinals_repl(match):
    n = match.group(0).replace(".", "").replace(",", ".")
    return num2words(n, lang="mk")


cardinals2words = RESub(patterns, cardinals_repl)
