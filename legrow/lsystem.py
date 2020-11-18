from __future__ import annotations

import sys
import tkinter as tk

from . import resources
from .render.turtle import TRender


class RewriteSystem:
    """Simple, single letter rewrite system tracking history."""

    def __init__(self, axiom: str, rules: dict):
        self.axiom = axiom
        self.rules = rules
        self.states = [axiom]

    @classmethod
    def from_config(cls, cfg: dict) -> RewriteSystem:
        return cls(cfg["axiom"], cfg["rules"])

    def rewrite(self, axiom) -> str:
        raise NotImplementedError

    @property
    def state(self):
        return self.states[-1]

    def __iter__(self):
        return self

    def __next__(self):
        self.states.append(self.rewrite(self.state))
        return self.state


class D0LSystem(RewriteSystem):
    """Deterministic context-free L-system."""

    def rewrite(self, axiom) -> str:
        """For each symbol in axiom, apply rule or keep it if no corresponding rule exists."""
        return "".join(self.rules.get(c, c) for c in axiom)


if __name__ == "__main__":

    cfg = resources.lsystems()[sys.argv[1]]
    ls = D0LSystem.from_config(cfg)
    for _ in range(int(sys.argv[2])):
        next(ls)

    TRender.render(lsystem=ls, size=cfg.get("size", 10), angle=cfg.get("angle", 90))
