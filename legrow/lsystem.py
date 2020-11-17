from __future__ import annotations

import sys

from . import resources
from .render.turtle import TRender


class LSystem:
    """Simple, single letter symbol system."""

    def __init__(self, axiom: str, rules: dict):
        self.axiom = axiom
        self.rules = rules
        self.state = None

    @classmethod
    def from_config(cls, cfg: dict) -> LSystem:
        return cls(cfg["axiom"], cfg["rules"])

    def rewrite(self, axiom) -> str:
        """For each symbol in axiom, apply rule or keep it if no corresponding rule exists."""
        return "".join(self.rules.get(c, c) for c in axiom)

    def __iter__(self):
        return self

    def __next__(self):
        if self.state is None:
            self.state = self.axiom
        else:
            self.state = self.rewrite(self.state)
        return self.state


if __name__ == "__main__":
    cfg = resources.lsystems()[sys.argv[1]]
    ls = LSystem.from_config(cfg)

    for _ in range(int(sys.argv[2])):
        next(ls)

    print(len(ls.state))
    TRender(ls).render(size=cfg.get("size", 10), angle=cfg.get("angle", 90))
