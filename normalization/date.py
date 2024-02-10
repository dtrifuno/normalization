from normalization.base import Pipeline, RESub
from num2words import num2words

MONTHS = "јануари|февруари|март|април|мај|јуни|јули|август|септември|октомври|ноември|декември"

deordinalize_day_months = RESub(
    r"(?i)\b(\d{1,2})\s*-[мвт]и\s*" + f"({MONTHS})\\b",
    lambda m: f"{int(m.group(1))} {m.group(2).lower()}",
)

day_month_pattern = r"(?i)(\d{1,2})\s*" + f"({MONTHS})"


def day_month_repl(match):
    day = num2words(int(match.group(1)), lang="mk", to="ordinal", form="p")
    month = match.group(2).lower()
    return f"{day} {month}"


day_month2words = RESub(day_month_pattern, day_month_repl)


month_year_pattern = (
    f"(?i)((?:{MONTHS})\\s*)?" + r"(\d+)(\s*(?:година|год[.]?|г[.]?))?(?!\w)"
)


def month_year_repl(match):
    if match.group(1) is None and match.group(3) is None:
        return match.group(0)

    month = match.group(1).strip().lower() if match.group(1) is not None else None
    year = num2words(int(match.group(2)), lang="mk", to="year")
    suffix = "година" if match.group(3) is not None else None

    items = [month, year, suffix]
    return " ".join([item for item in items if item is not None])


month_year2words = RESub(month_year_pattern, month_year_repl)


dates2words = Pipeline(
    [
        deordinalize_day_months,
        day_month2words,
        month_year2words,
    ]
)
