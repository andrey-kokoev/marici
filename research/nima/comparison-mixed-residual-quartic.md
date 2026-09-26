# A quartic comparison residual from two independent source actions

## Source and question

Continue the [retained-comparison action](retained-comparison-generating-series.md),
not the already established fiber roundtrip. The source is the existing pointed
swap in `BoundaryGeneratedQuestions`, lifted to two factors by the actual
`ObserverCoherenceCube.Geometry.expandLeft`, `expandRight` and `run` operations.

The earlier [observer source-power comparison](observer-source-cubic-quartic-comparison.md)
counts source factors, not polynomial degree. This test explicitly distinguishes
those notions. SCC obligations: product realization, action-composition comparison,
then readout compatibility. No new physical field or quartic coefficient is claimed
merely because the product has four coordinates.

## Commuting routes can have a nonzero action-composition defect

Let P be the existing swap operator. On the two-factor function space put

\[
A=P\otimes1,\qquad B=1\otimes P.
\]

Both are orthogonal involutions and AB=BA. The old quadratic recipe, now on an
independent joint field Psi, is

\[
S_T(\Psi)=\tfrac12\langle\Psi,(1-T)\Psi\rangle.
\]

The separate and composite actions differ:

\[
S_A(\Psi)+S_B(\Psi)-S_{AB}(\Psi)
=\tfrac12\langle\Psi,(1-A)(1-B)\Psi\rangle.
\]

Indeed, `(1-A)+(1-B)-(1-AB)=(1-A)(1-B)`. Since

\[
(1-A)(1-B)=(1-P)\otimes(1-P),
\]

the difference is the residual in both independent factors. This is a mixed
composition/additivity defect, NOT a nonzero commutator and not a failure of the
existing route homotopy. The source's commuting-square proof remains intact.

The mixed operator has rank one. It is four times the projector onto the tensor
product of the two anti-invariant sectors. Its square is four times itself,
whereas repeating the single-factor residual gives `(1-P)^2=2(1-P)`.

## Product readout gives a quartic

Declare the multiplicative probe on independent source values:

\[
\Psi(x,y)=\phi(x)\psi(y).
\]

This readout uses coefficient multiplication. The formal module proves, over an
arbitrary small commutative ring, that the mixed residual factors as

\[
((1-A)(1-B)\Psi)(x,y)
=((1-P)\phi)(x)\,((1-P)\psi)(y).
\]

In the counting pairing, its action is consequently

\[
E_{\rm mixed}(\phi\otimes\psi)=2S_P(\phi)S_P(\psi).
\]

For two copies of the same probe, and the actual source contrast
`delta=phi01-phi10`, this becomes

\[
E_4(\phi)=2S_P(\phi)^2=\tfrac12\delta^4.
\]

The quartic polynomial was not entered as a desired interaction: it is computed
from the stored source swap, its existing independent product lifts, the preceding
action recipe and the declared product probe. `ComparisonMixedResidual.agda`
proves the unhalved quadratic numerator is delta squared and the mixed numerator
is delta to the fourth, as well as their square relation. Division by two and
formal differentiation are checked over exact rational symbolic coefficients.

The fourth derivative with respect to delta is 12. This is the coefficient in
this declared comparison readout, not a prediction of the scalar fixture's 3/5.
The fourth-order polynomial has zero Hessian at the zero probe, so adding it would
not change the earlier quadratic kernel there. Differentiating on the four source
coordinates requires the Jacobian of `phi -> phi tensor phi`; the checker verifies
that chain rule and rejects dropping its factor.

On a purely anti-invariant phi, the simultaneous action S_AB vanishes: two swaps
act evenly. The separate actions and their mixed difference do not vanish. Thus
replacing the mixed defect by S_AB would miss the entire quartic in this control.

## This is not automatic from copying a source point

The linearization of the source map `x -> (x,x)` sends

\[
\sum_x\phi_x e_x\longmapsto\sum_x\phi_x(e_x\otimes e_x).
\]

It is NOT the multiplicative probe
`phi tensor phi`, which contains coefficients `phi_x phi_y`. The linearized copy
is an isometry and intertwines P with P tensor P. The simultaneous action then
recovers S_P, while its mixed defect is

\[
\tfrac12(\phi_{01}+\phi_{10})^2,
\]

still quadratic. On an arbitrary independent joint probe the mixed action is
also quadratic, now in its sixteen independent coordinates. Quarticity arises
only after the explicitly nonlinear product-probe restriction. No physical
product-state preparation or quantum cloning operation is asserted.

## Higher independent residuals generate all even degrees

For n independent slots, inclusion-exclusion over nonempty subsets of the
comparison actions gives

\[
E_n(\Psi)=\tfrac12\left\langle\Psi,
  \bigotimes_{i=1}^{n}(1-P)\,\Psi\right\rangle.
\]

The proof is the expansion of the tensor product: each subset contributes its
product of slot operators with the corresponding alternating sign. Contracting
against the product probe `phi tensor ... tensor phi` gives

\[
E_n(\phi^{\otimes n})
=\tfrac12\langle\phi,(1-P)\phi\rangle^n
=2^{n-1}S_P(\phi)^n
=\tfrac12\delta^{2n}.
\]

This all-n identity is a written finite-tensor algebra argument, not an arbitrary-n
Agda theorem. The checker constructs every comparison corner and all source states
for n=1,2,3,4 and obtains degrees 2,4,6,8. The quartic is therefore not uniquely
selected by the recipe. The ordinary formal series of these residual levels is

\[
\sum_{n\geq1}t^{n-1}E_n
=\frac{\delta^2}{2(1-t\delta^2)}.
\]

t counts independent residual levels; it is not a derived physical coupling.
The factorial vertices in this normalization are `(2n)!/2`.

## Physical interpretation gate and sign

The checked equation is `separate action = composite action + mixed residual`.
It does not decide which side becomes the physical action, or whether this
comparison defect is an interaction term, a correction to action assembly, or an
observable retained separately. Its positive sign follows this stated orientation.

For example, declaring `S_physical=S_P+kappa E4` gives fourth derivative
`12 kappa`; no source law here selects kappa, product-probe preparation, quartic
truncation or physical spacetime normalization. The full retained source and higher
comparison interfaces already exist; the unresolved step is their physical
readout/assembly selection, not a missing type of comparison.

This advances the conditional construction: a quartic residual now follows from
an actual pair of source operations, instead of being inserted as a potential.
It does not derive the earlier physical scalar action or its parameters.

## Verification

Fresh safe/cubical compilation passes for `agda/ComparisonMixedResidual.agda`,
including 25 local source modules. Generic ring proofs cover the binary residual
identity, commuting residual order, product factorization and the quadratic/quartic
numerators. Exact symbolic checks cover the action identities, chain rule, copied
versus product probes, source corner enumeration and the formal generating series.

```text
pwsh -NoProfile -File research/nima/checkers/check_comparison_mixed_residual.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_comparison_mixed_residual.py
uv run --with sympy python research/aspect/scc/scc.py check nima-comparison-mixed-residual
```

Receipts: `results/agda-ComparisonMixedResidual.json` and
`results/comparison-mixed-residual.json`. The checker parses the already proved
actual source swap images and verifies current formal import hashes.
New files/evidence remain uncommitted; no existing researcher source was edited.
No new quantum prescription, physical coupling prediction or independent review.
Report event `ev-000000015612-cb1cf4e2-9319-4b62-9850-f2fe5fbcce0c` at sequence
15612 is admitted but uncommitted. No computation remains active; graph admission
is not truth certification.
