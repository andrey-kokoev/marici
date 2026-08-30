#!/usr/bin/env python3
"""Finite separation of source selection from readout rigidification."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Model:
    name: str
    selected_lenses: frozenset[int]
    presentation_readouts: tuple[int, ...]

    @property
    def selects(self) -> bool:
        return len(self.selected_lenses) == 1

    @property
    def rigidifies(self) -> bool:
        return len(set(self.presentation_readouts)) == 1


models = (
    Model("neither", frozenset({0, 1}), (0, 1)),
    Model("selector_only", frozenset({0}), (0, 1)),
    Model("rigidifier_only", frozenset({0, 1}), (0, 0)),
    Model("both", frozenset({0}), (0, 0)),
)

observed = {(m.selects, m.rigidifies) for m in models}
expected = {(False, False), (True, False), (False, True), (True, True)}
assert observed == expected

print("selector/rigidifier four-case census: 4/4")
for model in models:
    print(f"{model.name}: selector={model.selects}, rigidifier={model.rigidifies}")
