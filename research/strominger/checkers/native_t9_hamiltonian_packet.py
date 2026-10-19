"""Explicit coefficient-field extension around, not inside, pinned software T9.

The original137 labels/domains remain unchanged.23 additional joint-arrow
slots are caller-supplied retained data, never implicit native contexts.
"""
from dataclasses import dataclass, replace
from fractions import Fraction
import sympy as S


def rational(value):
    value = S.sympify(value)
    if not value.is_Rational:
        raise ValueError('exact rational snapshot required')
    return Fraction(int(value.p), int(value.q))


@dataclass(frozen=True)
class NativeHamiltonianPacket:
    native: object
    native_indices: tuple
    hidden: tuple
    provenance: str

    def reconstruct(self):
        full = S.zeros(160,4)
        for index,row in zip(self.native_indices,self.native.original):
            full[index,:] = S.Matrix(1,4,[v for r in row.value for v in r])
        for index,values in self.hidden:
            full[index,:] = S.Matrix(1,4,values)
        return full


def build_packet(full, native_indices, fixture, transport, provenance):
    if not provenance:
        raise ValueError('completion provenance required')
    native_indices = tuple(native_indices)
    if (full.shape != (160,4) or len(native_indices) != 137
            or len(set(native_indices)) != 137
            or any(not 0 <= i < 160 for i in native_indices)):
        raise ValueError('declared160-to137 coefficient layout required')
    if len(fixture['source']) != 137:
        raise ValueError('original137-row interface required')
    rows = []
    for index,row in zip(native_indices,fixture['source']):
        values = tuple(rational(v) for v in full.row(index))
        rows.append(replace(row,value=(values[:2],values[2:])))
    native = transport(tuple(rows),fixture)
    hidden = tuple((i,tuple(rational(v) for v in full.row(i)))
                   for i in range(160) if i not in set(native_indices))
    return NativeHamiltonianPacket(native,native_indices,hidden,provenance)


@dataclass(frozen=True)
class HamiltonianPacketStep:
    parent: NativeHamiltonianPacket
    result: NativeHamiltonianPacket
    propagator: S.ImmutableMatrix
    generator: S.ImmutableMatrix
    provenance: str


def advance_packet(packet, propagator, generator, fixture, transport, provenance):
    """Retain an exact rational conservative step and its complete parent.

    Same-generator commutation and norm preservation do not alone certify an
    elapsed time. The caller must separately identify this supplied propagator
    with the intended exponential/clock; the checker does so for its quarter.
    """
    if not provenance:
        raise ValueError('step provenance required')
    U,A = S.ImmutableMatrix(propagator),S.ImmutableMatrix(generator)
    if U.shape != (160,160) or A.shape != (160,160):
        raise ValueError('declared coefficient-field operator dimensions')
    if any(value.is_real is not True for matrix in (U,A) for value in matrix):
        raise ValueError('real coefficient-field operators required')
    if A.T+A != S.zeros(160) or U.T*U != S.eye(160) or U*A != A*U:
        raise ValueError('conservative same-generator step required')
    result = build_packet(U*packet.reconstruct(),packet.native_indices,fixture,transport,
                          packet.provenance+'; '+provenance)
    return HamiltonianPacketStep(packet,result,U,A,provenance)
