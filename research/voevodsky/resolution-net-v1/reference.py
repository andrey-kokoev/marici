"""Finite immutable resolution syntax; a reference semantics, not a net evaluator."""
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Package:
    name: str
    data: tuple[str, ...] = ()

@dataclass(frozen=True)
class Admission:
    package: Package
    witness: str

@dataclass(frozen=True)
class Rule:
    name: str
    inputs: tuple[Package, ...]
    output: Package
    witness: str

    def __post_init__(self):
        if len(self.inputs) not in (1, 2):
            raise ValueError('only unary/binary witnessed rules are admitted')

@dataclass(frozen=True)
class Seed:
    package: Package
    evidence: 'Admission | Seed | Step'

    def __post_init__(self):
        if not isinstance(self.evidence, (Admission, Seed, Step)):
            raise TypeError('seed requires admission evidence or a prior resolution')
        if self.package != self.evidence.package:
            raise ValueError('seed package does not match its evidence')

    @property
    def level(self):
        return 0 if isinstance(self.evidence, Admission) else self.evidence.level + 1

@dataclass(frozen=True)
class Step:
    rule: Rule
    premises: tuple['Seed | Step', ...]

    def __post_init__(self):
        if not isinstance(self.premises, tuple) or not all(isinstance(p, (Seed, Step)) for p in self.premises):
            raise TypeError('premises must be an ordered immutable tuple of resolutions')
        if tuple(p.package for p in self.premises) != self.rule.inputs:
            raise ValueError('premise packages/arity do not match rule')
        if len({p.level for p in self.premises}) != 1:
            raise ValueError('premises belong to different closure layers')

    @property
    def package(self):
        return self.rule.output

    @property
    def level(self):
        return self.premises[0].level

History = Seed | Step

def unit(evidence: Admission | History) -> Seed:
    return Seed(evidence.package, evidence)

def map_seeds(f: Callable, history: History) -> History:
    if isinstance(history, Seed):
        return Seed(history.package, f(history.evidence))
    return Step(history.rule, tuple(map_seeds(f, p) for p in history.premises))

def flatten(history: History) -> History:
    if history.level < 1:
        raise ValueError('flatten requires resolution-valued seeds')
    if isinstance(history, Seed):
        return history.evidence
    return Step(history.rule, tuple(flatten(p) for p in history.premises))

def rule_trace(history: History) -> tuple:
    """Ordered occurrence tree, including rule witnesses; not just an endpoint."""
    if isinstance(history, Seed):
        return ('seed', history.package, history.evidence)
    return ('rule', history.rule, tuple(rule_trace(p) for p in history.premises))
