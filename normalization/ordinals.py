# аdd -тен

from num2words import num2words

from normalization.base import RESub

masculine_pattern = r"(рв|ор|ет|ти|ми)|[вртм]и(о[твн])"
feminine_pattern = r"([вртм]а)|[вртм]а([твн]а)"
neuter_pattern = r"([вртм]о)|[вртм]о([твн]о)"
plural_pattern = r"([вртм]и)|[вртм]и([твн]е)"
pattern = (
    r"(\d+)\s*-?\s*(?:"
    + f"{masculine_pattern}|{feminine_pattern}|{neuter_pattern}|{plural_pattern}"
    + r")\b"
)


def ordinal_repl(match):
    number = int(match.group(1))
    match_idx = next(i for i, v in enumerate(match.groups()[1:]) if v is not None)
    form = ["m", "f", "n", "p"][match_idx // 2]

    is_definite = match_idx % 2 == 1
    suffix = match.groups()[1:][match_idx] if is_definite else ""
    return num2words(number, lang="mk", to="ordinal", form=form) + suffix


ordinal2words = RESub(pattern, ordinal_repl)
