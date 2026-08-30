# Spin-grade bridge spec: what the bottom arrow of the descent square must satisfy

A specification, not a construction. This packet states, from the
gravitational side, the exact contract that any mixed boundary trace —
the bottom arrow of Nima's descent square, from the scaffold conductor
line to the gravitational soft coefficient line — must satisfy. Each
gate is falsifiable; the gravitational side of every gate is certified
by `checkers/cocycle_bridge_gates_checks.py` (groups C2–C3). The
Carrier-side inputs are Nima's to supply.

## Setup

The descent square:

```
scalar momentum/spinor normalization  --helicity evaluation-->  helicity coefficient line
            | alternating fusion conductor                          | soft residue
            v                                                       v
   scaffold conductor line  --mixed boundary trace-->   gravitational soft coefficient line
```

The right column and the bottom-right corner now exist (descent-gate
arc, ledger 1899). The missing bottom arrow is a comparison map `B`
from Carrier-side conductor data to gravitational readouts. The
gravitational readouts carry a 2x2 character census under the two
involutions `(alpha, sigma)` (antipodal transport; helicity
conjugation), with physical parity the diagonal `P = alpha . sigma`:

| rung | readout | (chi_alpha, chi_sigma) | diagonal product |
|---|---|---|---|
| 0 | displacement / electric | (-1, +1) | -1 |
| 1 | spin / magnetic | (-1, -1) | +1 |
| 2 | ballistic / electric | (-1, +1) | -1 |

## Gate G1 — the character-forbidding gate (C3.1)

The Carrier/fusion side's conductor line carries the uniformly
diagonal-invariant product character (+1 on every rung; Nima's ev-2100
finding, declared input). The gravitational coefficient line's diagonal
product character is `[-1, +1, -1]`, not `[+1, +1, +1]`.

**Consequence:** no character-preserving identification between the two
sectors' coefficient lines exists — the vectors differ in exactly the
two electric entries (Hamming distance 2, so not even a rung permutation
can match them) and agree ONLY at rung 1, the magnetic one (C3.1). Any
candidate `B` that acts as the identity on characters — any "the two
lines are the same object" map — is excluded before construction begins.
This is the exact content of the alternating-vs-uniform difference
between the sectors.

## Gate G2 — the anchor gate (C2, C3.2)

Exactly one gravitational readout line is diagonal-even: the spin-grade
(magnetic, rung-1) line. Certified at the character census level (C2.4):
the product character is +1 only at rung 1.

The anchor also survives direct examination of the magnetic readout `M`
on an exact P-symmetric spin-2 datum, but **not** as naive pointwise
invariance. The certified statements (C3.2) are:

- the datum is invariant as a spin-2 tensor (`P(C_zz) = z^4 C_zz`,
  `P(C_zbzb) = zb^4 C_zbzb`);
- the two readout terms obey the exact diagonal covariance law
  `P(A) = z^10 zb^2 A`, `P(B) = z^2 zb^10 B` (sigma-conjugate tensor
  weights), so `P` maps the magnetic sigma-line to itself:
  `sigma(P(M)) + P(M) = 0`;
- in the dilation frame the P-even dressing vanishes identically on the
  P-invariant datum: `z^4 A = zb^4 B` exactly — the dilation-dressed
  magnetic readout is exactly P-even;
- `M` is nonzero at the fresh witness (`M|W2 = -558186307585/111045168`),
  while the electric combination is NOT P-invariant there (C3.2b,
  residual `-3048757028445173/1004950228464`).

The naive statement `P(M) = M` for the RAW readout is false on every
datum tested (the two terms carry different diagonal tensor weights) and
is retained as the typed obstruction **C3.2!** with exact residual
`91712801267753425/13064352970032` at the fresh witness. "Diagonal-even
magnetic rung" is therefore a character/density-line statement (plus
exact dilation-frame evenness), not pointwise invariance of the raw PSZ
component.

**Consequence:** the image of any comparison map from a Carrier
diagonal-invariant object must land in the spin-grade sector. Rung 1 is
the unique anchor of the bottom arrow on the gravitational side.

## Gate G3 — the cocycle-intertwining gate (C1, C3.3)

The gravitational coefficient line is not P-invariant; it is
P-covariant with the exact cocycle `F` (see
`diagonal-parity-cocycle.md`):

```
P(K^+) = sigma(F) . K^+ ,   P(K^-) = F . K^- ,   F . sigma(F) = (z zbar)^-2 .
```

**Consequence:** at the level of the coefficient lines (before
projection to a rung readout), `B` cannot be an equivariant map of
trivial Z_2-objects. It must satisfy the intertwining condition

```
B ∘ (Carrier diagonal action) = (gravitational twisted action by F) ∘ B ,
```

i.e. `B` is a map of *covariant* objects, and the comparison is
specified up to the cocycle `F`. Equivalently (C3.3): the space of
diagonal-even gravitational readout lines in rungs {0,1,2} is exactly
1-dimensional, spanned by rung 1 — so after projection the untwisted
comparison exists precisely on the spin grade, and nowhere else.

## What this spec does not claim

- It does not construct `B`. The cross-sector source object (the actual
  mixed boundary trace) is Carrier-side work.
- It does not lift the sign-gauge no-go: the character census and the
  cocycle are gravitational-side exact data; a canonical bridge still
  requires the source-derived comparison, not character matching.
- It does not derive antipodal matching at `i^0`; that remains a
  declared external physical input.

## Falsifiability

Each gate fails loudly if the underlying exact checks fail:

- G1 is false if the gravitational diagonal character vector ever
  computes to [+1,+1,+1] (C3.1);
- G2 is false if any electric rung is found diagonal-even (C2.4), or if
  the magnetic line fails P-stability (`sigma(P(M)) + P(M) = 0`) or the
  dilation-frame evenness `z^4 A = zb^4 B` on P-symmetric data (C3.2),
  or if the raw pointwise obstruction C3.2! unexpectedly vanishes;
- G3 is false if the twisted action fails to be a Z_2 action (C1.3) or
  if the diagonal-even readout space is not 1-dimensional (C3.3).

## Verification

`uv run --with sympy python research/strominger/checkers/cocycle_bridge_gates_checks.py`
— see `research/strominger/results/cocycle_bridge_gates.json`,
groups C2–C3.
