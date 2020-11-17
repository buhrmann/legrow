from __future__ import annotations

import sys

from . import resources


class LSystem:
    def __init__(self, axiom: str, rules: dict):
        self.axiom = axiom
        self.rules = rules
        self.state = None

    @classmethod
    def from_config(cls, cfg: dict) -> LSystem:
        return cls(cfg["axiom"], cfg["rules"])

    def rewrite(self, axiom) -> str:

        res = ""
        for c in axiom:
            s = self.rules[c]
            res += s

        return res

    def __iter__(self):
        return self

    def __next__(self):
        if self.state is None:
            self.state = self.axiom
        else:
            self.state = self.rewrite(self.state)
        return self.state


if __name__ == "__main__":
    cfgs = resources.lsystems()
    ls = LSystem.from_config(cfgs[sys.argv[1]])
    for _ in range(10):
        print(next(ls))
