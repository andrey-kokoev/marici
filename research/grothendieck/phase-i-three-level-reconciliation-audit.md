# Phase-I three-level reconciliation audit

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: typed audit accepting Nima's correction at `pi_0` while preserving the
full-Carrier closure

## Audit question

Nima proposes that three statements coexist:

1. the admitted full Carrier has no total, neutral, equivariant, unital,
   distributive multiplication;
2. after the explicit monoidal-disjoint-union relaxation, the free additive
   object `M = pi_0(Surf_U^sqcup)` nevertheless has a canonical initial
   semiring multiplication; and
3. quotienting the noncommuting unit symmetry to
   `D4_ab = C2 x C2` gives an exact labelled rig candidate, but not yet an
   authorized physical realization.

The three claims are compatible. The second corrects one overbroad sentence
in the earlier closure packet; it does not reopen the first conclusion.

## Level 1: admitted full Carrier

The operation-inventory closure remains unchanged. No admitted candidate is
simultaneously Carrier-level, coefficient-neutral, total on unmarked
objects, source-equivariant, unital, and distributive. The exact obstruction
vector remains

\[
\boxed{(130,2,1,2)}.
\]

In particular, connected sewing still has no `D4 x D4`-fixed interface and
has arity-two unit residual. Nima's endomorphism construction is not another
row of this Carrier-level inventory: its multiplication is defined only
after passing to the derived commutative monoid `pi_0`.

## Level 2: conditional `pi_0`

Under the already-declared relaxation from categorical coproduct to
symmetric-monoidal geometric disjoint union, connected decomposition proves
that the pointed monoid `M` is free on `U`. For every `a` in `M`, freeness
gives a unique additive endomorphism `f_a` with `f_a(U)=a`. The law

\[
a\cdot b=f_a(b)
\]

is canonical at this type. Evaluation at `U` identifies `M` with its
additive endomorphisms; composition gives associativity and unit, while
additivity and pointwise addition give the two distributive laws. The
pointed universal property then makes `M` the initial commutative semiring.

The distinguished generator is legitimate here because `U` is part of the
conditional pointed construction, and endomorphism composition is available
in the derived category of commutative monoids. Neither fact supplies a
bifunctor on the surface groupoid.

Consequently the earlier sentence

> initial semiring and intrinsic primes: not derived

must be read as a **full-Carrier** statement. The corrected typed statement
is:

\[
\boxed{
\begin{aligned}
&\text{full Carrier initial semiring: not derived},\\
&\text{conditional initial semiring on }\pi_0:\text{ derived},\\
&\text{conditional intrinsic primes and UFD: derived}.
\end{aligned}}
\]

The intrinsic-prime checker is a finite readout audit using ordinary integer
encodings of component words. It does not itself prove the unbounded theorem;
that strength comes from the free-monoid normal form, well-founded component
length, repeated subtraction, and the group completion. This is correctly
typed in Nima's packet. It still derives no `Spec(Z)`, residue fields,
Frobenius, or Euler product.

## Level 3: the `D4_ab` rig shadow

The Eckmann--Hilton obstruction is decisive. Endomorphisms of a monoidal unit
must commute, whereas the quadrilateral generator has rotation and reflection
with `rs != sr`. Hence the conditional multiplication on `pi_0` cannot lift
to a monoidal product with unit `U` on the full `D4`-resolved groupoid.

Abelianization is the maximal algebraic quotient compatible with that
necessary unit law. The resulting `D4_ab`-labelled finite-component groupoid
has an exact formal rig structure, but two qualifications are essential:

- its cartesian-product multiplication is an algebraic completion, not a
  source-derived Carrier sewing;
- the quotient kills the commutator subgroup and has not been authorized as
  a physical realization.

The `m=2` Ward line factors through `D4_ab`, but this is not a hostile test:
it is one-dimensional, so its group action necessarily kills every
commutator. It verifies the exact source character but supplies no global
authorization.

The flavor comparison further shows that universal coefficient-level
factorization is the wrong gate. A commutator moves the exact sparse
coefficient presentation, while physical weak-basis invariants remain fixed.
Thus the labelled rig is already falsified as a universal coefficient object;
only a candidate physical-readout shadow remains.

## Verdict and next falsifier

Nima's three-level reconciliation is accepted with the typing above:

| Level | Exact status |
|---|---|
| admitted full Carrier | closed; no Phase-I multiplication |
| conditional pointed `pi_0` | initial semiring and intrinsic primes derived |
| `D4_ab` labelled rig | exact algebraic candidate, physically unauthorized |

Phase II remains gated. No Burnside--Witt structure, `Spec(Z)`, Frobenius, or
Euler product follows.

The next sharp test must use a source-established **physical invariant** with
a genuinely higher-dimensional nonabelian source action. A rank-one character
cannot detect a commutator, while requiring every raw coefficient lens to
factor has already been falsified. The candidate arithmetic shadow fails if
such a physical invariant detects information killed by abelianization.

## Verification

The companion checker imports all eight exact result packets, verifies every
level and the deliberate nonzero obstructions, and records input digests:

- `research/grothendieck/checkers/phase_i_three_level_reconciliation_audit.py`;
- `research/grothendieck/results/phase-i-three-level-reconciliation-audit.json`.

No ledger entry is claimed by this packet.
