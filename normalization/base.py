import copy
import re

# jonatasgrosman/wav2vec2-large-xlsr-53-english


class Replacer:
    patterns: dict[str, str]

    def __init__(self, patterns):
        self.patterns = copy.deepcopy(patterns)

    def __call__(self, string: str):
        for old, new in self.patterns.items():
            string = string.replace(old, new)
        return string


class RESub:
    pattern: str
    repl: any  # re.Match[str] -> str

    def __init__(self, pattern: str | re.Pattern[str], repl: any):
        self.pattern = (
            pattern if isinstance(pattern, re.Pattern) else re.compile(pattern)
        )
        self.repl = repl

    def __call__(self, string):
        return re.sub(self.pattern, self.repl, string)


class Pipeline:
    def __init__(self, fns):
        self.fns = fns[:]

    def __call__(self, string):
        for fn in self.fns:
            string = fn(string)
        return string
