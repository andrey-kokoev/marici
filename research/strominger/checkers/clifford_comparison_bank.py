"""Conditional single-reader bank interpretation of the supplied matrix fixture.

Uses actual Cl(2,0) multiplication, sewing, normalized readout and isometric
lift. Composition is a declared read/multiply/lift recipe, NOT the conservative
memory exchange and NOT an energy-conserving preparation claim.
"""
from dataclasses import dataclass
from retained_reference_protocol import algebra,memory


def coefficients(matrix):
    a,b=matrix[0];c,d=matrix[1]
    return ((a+d)/2,(a-d)/2,(b+c)/2,(b-c)/2)


@dataclass(frozen=True)
class ComparisonBank:
    label: tuple
    source: tuple
    target: tuple
    bank: tuple
    provenance: tuple
    parents: tuple = ()

    def raw(self):
        return algebra.matrix(algebra.sew(self.bank))

    def normalized(self):
        return algebra.matrix(memory.readout(self.bank))


def from_legs(row,left,right):
    # Chronological left then right, while tensor factors are right,left.
    bank=algebra.tensor(coefficients(right),coefficients(left))
    return ComparisonBank(row.label,row.source,row.target,bank,
                          ('supplied-shared-leg-bank','right-tensor-left'))


def compose(left,right):
    if left.target!=right.target:
        raise ValueError('Comparison bank composition requires original common target')
    value=algebra.multiply(memory.readout(right.bank),memory.readout(left.bank))
    return ComparisonBank(('composite',left.label,right.label),left.source,right.target,
                          memory.lift(value),('declared-normalized-read-multiply-lift',),
                          (left,right))
