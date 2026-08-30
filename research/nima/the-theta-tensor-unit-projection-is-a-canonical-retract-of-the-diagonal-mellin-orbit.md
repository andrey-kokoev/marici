# The theta tensor-unit projection is a canonical retract of the diagonal Mellin orbit

## The remaining ambiguity

The labelwise Green square gives, for every source vector (f),

[
Delta f=(mathcal M_n f)_{nge 1}.
]

Scalar theta synthesis is not a left inverse of (Delta). Nevertheless the
multiplicative label system already contains a distinguished object: the unit
label (1).

## Unit evaluation

Let (operatorname{ev}_1) be projection to the (n=1) component and define

[
epsilon_1
=
mathcal M_1^{-1}operatorname{ev}_1.
]

Because

[
mathcal M_1 f(u)=e^{u/2}f(e^u),
]

we have the exact identity

[
epsilon_1Delta f
=
mathcal M_1^{-1}mathcal M_1f
=
f.
]

Thus the diagonal Mellin orbit has a canonical retract once the multiplicative
unit label is retained. No fitted coefficients, invariant mean, or inversion of
the scalar theta sum enters this construction.

For the completed first Adams square this gives

[
epsilon_1
left(
  igoplus_nmathcal C^{-1}mathcal M_ns_p
ight)
=
b_p,
]

and hence

[
d_p
=
-rac12S_{mathrm{ord}}epsilon_1
left(
  igoplus_nmathcal C^{-1}mathcal M_ns_p
ight).
]

## Topological scope

The claim is made on the retained labelled carrier, whose topology has
continuous coordinate projections. On a product, projective sequence, or
weighted direct-sum realization, (operatorname{ev}_1) is continuous with
the norm or seminorm of the first coordinate.

This does not assert that the unweighted diagonal map into
(igoplus_nL^2) is bounded: every (mathcal M_n) is isometric, so such a
diagonal has infinite unweighted Hilbert norm. The Euler--Maclaurin
renormalized theta completion and the label carrier must remain typed
separately.

## Structural compatibility

The unit retract preserves every structure acting identically on the analytic
factor and diagonally in the label:

[
epsilon_1(mathbf 1otimes A)Delta
=
A
]

whenever (A) commutes with (mathcal M_1) in the declared comparison
square. In particular it preserves the wall--jump coordinates and the ordered
primitive after those are constructed labelwise.

Prime idempotents are untouched because the theta label and valuation prime
label are different tensor factors.

## What this does not prove

The map (epsilon_1) is a unit evaluation, not scalar theta augmentation. It
is not permutation-symmetric in the positive-integer labels, and it does not
recover a source vector from an arbitrary scalar sum

[
sum_nmathcal M_nf.
]

Nor is it faithful on the full label carrier: it annihilates every packet with
zero first coordinate. Its faithfulness is exactly restricted to the diagonal
orbit (operatorname{ran}Delta), where the first coordinate already contains
one complete copy of the source.

Therefore two downstream uses must remain distinct:

- constructor counit: (epsilon_1), exact on the diagonal orbit;
- theta observer: labelled Gaussian synthesis followed by Poisson sewing and
  Mellin readout.

The second may observe arithmetic completion, but it is not needed to define
the first Adams edge.

## Authority audit

The construction is source-authorized precisely if the positive-integer label
monoid and its unit (1) are part of the frozen theta carrier and all admitted
completion maps retain that coordinate. If the completed theory quotients out
or symmetrizes away the unit coordinate, then (epsilon_1) does not descend.

The required descent test is

[
ker qsubseteqker(mathcal M_1^{-1}operatorname{ev}_1),
]

for the declared completion quotient (q). Before such a quotient, the retract
is canonical and bounded; after a quotient, descent must be proved rather than
assumed.

## Verdict

The missing theta-label counit exists canonically on the faithful labelled
Mellin orbit: evaluate at the multiplicative tensor unit and undo its
half-density chart. This closes recovery of the single Stieltjes boundary copy
without treating scalar theta synthesis as invertible.

The remaining gate is narrower: verify that the actual renormalized completion
retains the (n=1) coordinate and that every downstream sewing quotient
satisfies the unit-evaluation descent condition.
