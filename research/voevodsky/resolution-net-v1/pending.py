"""Separate open-context boundary. Holes are obligations, never seed witnesses."""
from dataclasses import dataclass
from reference import Admission, Package, Rule, Seed, Step, unit
from admission import package as validate_package

@dataclass(frozen=True)
class Hole:
    slot: str
    package: Package

@dataclass(frozen=True)
class Branch:
    rule: Rule
    children: tuple

@dataclass(frozen=True)
class Receipt:
    slot: str
    ticket: str
    evidence: Admission

@dataclass(frozen=True)
class Pending:
    context: Hole | Branch
    receipts: tuple[Receipt, ...] = ()

    def __post_init__(self):
        holes = self.holes()
        if type(self.receipts) is not tuple:raise ValueError('immutable receipts required')
        slots=set();tickets=set()
        for r in self.receipts:
            if type(r) is not Receipt or type(r.ticket) is not str or not r.ticket:
                raise ValueError('invalid receipt')
            if r.slot not in holes or r.slot in slots or r.ticket in tickets:
                raise ValueError('unknown, duplicate slot or reused ticket')
            if type(r.evidence) is not Admission or type(r.evidence.witness) is not str:
                raise ValueError('admission evidence required')
            validate_package(r.evidence.package)
            if r.evidence.package!=holes[r.slot]:raise ValueError('wrong evidence package')
            slots.add(r.slot);tickets.add(r.ticket)

    def holes(self):
        holes={}
        def visit(c):
            if type(c) is Hole:
                if type(c.slot) is not str or not c.slot or c.slot in holes:
                    raise ValueError('hole occurrences must have unique slot IDs')
                validate_package(c.package);holes[c.slot]=c.package;return c.package
            if type(c) is not Branch or type(c.children) is not tuple or type(c.rule) is not Rule:
                raise ValueError('invalid open context')
            r=c.rule
            if type(r.inputs) is not tuple or len(r.inputs) not in (1,2) or type(r.witness) is not str:
                raise ValueError('explicit witnessed unary/binary rule required')
            validate_package(r.output)
            if tuple(visit(child) for child in c.children)!=r.inputs:raise ValueError('context rule interface mismatch')
            return r.output
        visit(self.context);return holes

    def accept(self, slot, ticket, evidence):
        # Persistent state: rejection does not mutate the prior context.
        return Pending(self.context,self.receipts+(Receipt(slot,ticket,evidence),))

    def missing(self):
        return tuple(sorted(set(self.holes())-{r.slot for r in self.receipts}))

    def materialize(self):
        if self.missing():raise ValueError('unfilled obligations are not admission evidence')
        evidence={r.slot:r.evidence for r in self.receipts}
        def build(c):
            if isinstance(c,Hole):return unit(evidence[c.slot])
            return Step(c.rule,tuple(build(child) for child in c.children))
        return build(self.context)
