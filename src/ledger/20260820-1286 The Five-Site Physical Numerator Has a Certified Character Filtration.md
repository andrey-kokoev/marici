---
title: "The Five-Site Physical Numerator Has a Certified Character Filtration"
date: 2026-08-20
entry: 1286
status: active-narrow-result
author: marici.Benincasa
---

# 1286 — The Five-Site Physical Numerator Has a Certified Character Filtration

Sequence claim: `seqclaim-57bf1173ce4c390119678e72`.

## Frozen object

Use Entry 1270's degree-sixteen numerator (N_{16}), Entry 1257's physical
five-sheet Kummer cover, and Entry 1280's corrected decomposition

[
N_{16}
equiv
sum_{Ssubseteq{1,ldots,5}}
C_S(t,u_1,u_2,u_3)y_S,
qquad y_i^2=F_i(u).
]

No symmetry between the five occurrence labels is assumed on this asymmetric
physical slice.

## Exact character grading

Let (w=|S|). Every one of the 43296 monomials in the 32 coefficient
polynomials satisfies

[
oxed{
deg_tequiv wpmod 2,
qquad
deg_t+deg_ule 16-w.
}
]

All 32 characters are nonzero. Their exact aggregate profile is

[
egin{array}{c|c|c|c|c}
w & #	ext{ characters} & #	ext{ terms} &
deg_t^{min} & deg_t^{max}\
hline
0&1&2549&0&16\
1&5&8363&1&15\
2&10&16778&0&14\
3&10&10068&1&13\
4&5&5012&0&12\
5&1&526&1&11
end{array}
]

The largest loop-coordinate degrees are respectively

[
16, 14, 14, 12, 12, 10.
]

The binomial character counts are the deck-character census, not evidence for
a residual permutation symmetry.

## Provenance and verification

The canonical producer now writes the deterministic fingerprint

[
mathtt{296f5cb5d53a2cbc}
]

for the serialized 13304-term numerator. The Kummer reducer refuses any input
whose stored fingerprint differs from its live recomputation. The completed
packet records the same fingerprint.

The decomposition passes:

1. exact quotient-ring reduction;
2. the monomial-by-monomial grading audit above;
3. four independent finite-field cover evaluations, two modulo (1009) and
   two modulo (1013).

All four reconstructed 32-character values equal the original numerator.

## Meaning

The physical numerator is neither scalar nor an unstructured rank-32 object.
It carries the filtration forced by ambient degree and labelled deck
character:

[
oxed{
	ext{character weight }w
Longrightarrow
	ext{coefficient budget }16-w
	ext{ with fixed }t	ext{-parity}.
}
]

This is coefficient structure over the frozen carrier. It does not by itself
identify a finite de Rham master basis, a Gauss--Manin invariant block, or a
physical integration-cycle projection.

## Next falsifier

Construct the Kummer connection in the same 32 labelled characters and test
whether this degree/parity filtration is preserved by source-derived
Gauss--Manin transport. A failure would show that the grading is only a
numerator presentation; preservation would provide the first canonical
finite filtration for choosing the five-site coefficient reduction.
