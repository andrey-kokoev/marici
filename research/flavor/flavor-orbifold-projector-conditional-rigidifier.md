# Orbifold projector conditional rigidifier: WP742

## Question

Can a geometric projection remove WP739's second singlet without a tunable
vacuum potential and thereby turn the WP736 Clebsch ray into a source-derived
portal selector?

## Declared relational experiment

Consider an (SO(5)) vector on (S^1/Z_2) with equal endpoint parity

\[
P=\operatorname{diag}(1,1,1,1,-1).
\]

This is not an operation inside the original four-dimensional (SO(5))
experiment. It changes the physical groupoid to the stabilizer of (P). Its
connected zero-mode symmetry is (SO(4)), followed by the declared diagonal
(SO(3)).

For positive intrinsic field parity, the zero-mode projector is

\[
\Pi_+=\frac{I_5+P}{2}
=\operatorname{diag}(1,1,1,1,0).
\]

The surviving four-dimensional carrier restricts as

\[
4\downarrow SO(3)_{\mathrm{diag}}=3\oplus1.
\]

Thus the unwanted second singlet is removed and the surviving singlet
projector is unique. Conditional on this boundary packet, the construction is
a genuine labelled-projector selector and rigidifier. It inherits WP736's
normalized Clebsch relation

\[
\frac{\kappa_B^2}{\kappa_A^2}=4.
\]

## Boundary authority obstruction

The same bulk field admits negative intrinsic parity. Its zero-mode projector
is then

\[
\Pi_-=\frac{I_5-P}{2}
=\operatorname{diag}(0,0,0,0,1),
\]

which retains only the other singlet. The two zero-mode domains differ before
any low-energy dynamics is applied. Their projector difference has exact
Frobenius norm (sqrt5).

Consequently, the projection does not derive its own parity choice. It moves
the selector question from a scalar-potential coefficient to a boundary
equivalence class and an intrinsic parity. This is a discrete fiber rather
than a continuous mixing angle, but it is still a source fiber.

This typing agrees with the primary gauge–Higgs literature. Yamamoto identifies
the arbitrariness of imposed orbifold boundary conditions and states that a
more fundamental dynamics is needed to determine them. The proposed dynamical
formulation restricts contributing equivalence classes but does not establish
this flavor boundary packet as a unique outcome. See
[arXiv:1401.0466](https://arxiv.org/abs/1401.0466). A concrete
(SO(5)\times U(1)\times SU(3)) construction uses orbifold conditions to break
(SO(5)) to (SO(4)), but also reports that an essential brane scalar has an
unresolved origin. See [arXiv:1902.01603](https://arxiv.org/abs/1902.01603).

## Magnitude and clock fiber

Even after choosing the projector, dimensional reduction gives

\[
g_4=\frac{g_5}{\sqrt\ell},
\]

where (ell) is the compactification length. Its logarithmic sensitivities
are

\[
\frac{\partial\log g_4}{\partial\log g_5}=1,
\qquad
\frac{\partial\log g_4}{\partial\log\ell}=-\frac12.
\]

Geometry therefore fixes neither the parent coupling nor the compactification
clock. The portal magnitude at a physical energy remains on a two-input
fiber, before ordinary RG relevant directions are considered.

## Threshold and instrument gates

At an orbifold boundary, only the residual symmetry must be respected. The
singlet and triplet are inequivalent residual representations, so independent
localized portal terms are allowed. Writing their finite contributions as
(delta_A) and (delta_B), the ordered contrast becomes

\[
\Delta_{\mathrm{low}}
=\Delta_{\mathrm{parent}}+\delta_B-\delta_A.
\]

Hence the bulk Clebsch sign survives thresholds only if a source principle
forbids the difference or fixes it inside a strict uncertainty margin.
Orbifolding alone supplies neither condition.

Nor does a representation label constitute an instrument. No calibrated pair
of detector channels on physical16 is supplied by the compactification.

## Disposition

The geometric projection is stronger than the failed one-(14) vacuum: once
chosen, it removes the singlet mixing fiber exactly and preserves the WP736
Clebsch ray. It is nevertheless conditional, not Deutschian. The boundary
class, intrinsic parity, bulk coupling, compactification clock, localized
threshold terms, and detector map remain independently variable.

A progressive successor must derive all those objects from one admitted
source dynamics. Merely choosing the favorable parity or setting localized
operators to zero would relocate the tuning.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp742_orbifold_projector_conditional_rigidifier.py`.

Generated result:
`results/wp742_orbifold_projector_conditional_rigidifier.json`.
