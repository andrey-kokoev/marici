# Scalar weights from a declared action; coupling selection fails

## Question and disposition

The operator requested derivation of the physical weights, not another arithmetic
implementation. The prior action-selection countermodels already rule out
inferring an action from the dependent core alone. This packet tests the stronger,
actual scalar interface: fixed kinetic normalization, quartic interaction grammar,
field parity and tree pole factorization.

The local weights are now derived **conditionally from a declared action and
quantum pairing convention**. The coupling is not selected: two positive values
survive the tested conditions and give distinct native amplitudes. Thus the request
to derive unique physical weights from the bare Carrier remains unfulfilled, with
a concrete obstruction rather than an unexplored arithmetic dependency.

SCC obligations: forward realization from action to local weights and coefficient
readout compatibility. Physical action selection is a separate, failed promotion.

## Action to weights

Start with the declared four-dimensional real scalar family

\[
\mathcal L=\frac Z2\partial_\mu\phi\partial^\mu\phi
-\frac{m^2}{2}\phi^2-\frac{\lambda}{4!}\phi^4,
\qquad \eta=\operatorname{diag}(1,-1,-1,-1).
\]

The kinetic Hessian, paired between opposite Fourier momenta, gives

\[
K(q)=Zq^2-m^2.
\]

The fourth field variation at zero gives `-lambda`; the `4!` is canceled by
four differentiations. `agda/ScalarActionDerivatives.agda` implements formal
polynomial differentiation and proves the quadratic and quartic normalization
identities over any supplied commutative ring with the requisite inverses.
`agda/ScalarActionWeights.agda` instantiates them in the constructed component
rational ring, using the previously proved inverse fractions for 2 and 24.

For the chosen phase `exp(iS)` and normalized Gaussian pairing, formal integration
by parts gives

\[
\partial_x(xe^{iKx^2/2})=(1+iKx^2)e^{iKx^2/2},
\qquad 0=1+iK\langle x^2\rangle,
\qquad \langle x^2\rangle=i/K.
\]

The expectation identity uses formal Gaussian integration by parts. Vanishing
boundary terms, the phase convention, normalization and a Green-function prescription are assumed;
no oscillatory integral or continuum measure is constructed here. The checker
differentiates the integrand and solves the resulting linear identity rather than
inserting a propagator lookup table. Away from poles the local factors are

\[
V_4=-i\lambda,\qquad G(q)=\frac{i}{Zq^2-m^2}.
\]

Different pole prescriptions are not distinguished by these non-pole rational
values. Fixing `Z=1` and `m=0` recovers the benchmark kernel. This fixes the kinetic
normalization, not the quartic coupling.

For a quartic tree with V vertices and V-1 internal edges,

\[
(-i)^V i^{V-1}=-i\bigl((-i)i\bigr)^{V-1}=-i.
\]

Consequently the delta-stripped `i M` convention yields

\[
\mathcal M_h=-\lambda^V\prod_e K(q_e)^{-1}.
\]

In particular, one six-point channel contributes `-lambda^2/q^2`.
This phase argument is a written all-V identity; the checker also tests V=1 through
12. The Fourier, quantum and amputation conventions remain declared physical
inputs, not consequences of package composition.

## Constructed inversion and actual channel comparison

`ScalarActionWeights.reciprocal` handles **every nonzero signed integer**, using
sign and positive magnitude to construct a component fraction. Its inverse law is
proved for all such integers. Zero requires a contradiction witness, so there is
no fallback branch assigning a spurious zero inverse.

The new channel kernel is computed using the constructed signed operations from
the actual `ScalarSixFixture` external momenta and the declared `+---` metric.
Every channel has a checked nonzero-kernel witness. No call to the old reciprocal
units or old weight function computes the new weights; those appear only on the
reference side of the comparison.

For the fixture's declared coupling `3/5`, all ten channel weights are individually
Agda-equal to the previous common-denominator coefficients. The independent
symbolic-action checker compares each derived term with the Python native table
and sums to `6/25`. It parses and hashes the actual Agda source inputs. This does
not replace the prior native execution with a constant-amplitude seed or claim
that the Python evaluator is formally verified.

## Strongest selection test

Conjecture: once the component arithmetic, canonical massless kinetic term,
quartic grammar and tree sewing conditions are fixed, those conditions select the
remaining physical weights.

Rivals: the old reciprocal table hides arithmetic incompleteness; the discrepancy
is merely field normalization; a genuine contact coupling remains free.

Risky consequence: two admissible normalized source models over the same unweighted
kinematic incidence cannot give different amplitudes if that incidence uniquely
selects the weights.

Both positive couplings below have the same canonical quadratic kernel, even field
parity, local quartic grammar and ten-channel kinematic incidence:

| Coupling | Four-point amplitude | Six-point amplitude |
| --- | --- | --- |
| 3/5 | -3/5 | 6/25 |
| 6/5 | -6/5 | 24/25 |

The source actions are different. Their difference is `-phi^4/40`. The complete
marked packages retain their different coupling inputs; they are **not** asserted
to be equal. What agrees is the explicitly unweighted kinematic incidence. With
the same unit kinetic residue, this is not an unrecorded field rescaling.

The six-point pole residue is `-lambda^2 = -M4 M4` for either value. More generally,
rescaling lambda by a scales a quartic n-point tree by `a^(n/2-1)`. On a cut,
`n_left+n_right=n+2`, so the two lower-tree exponents add to the original exponent.
Tree factorization therefore does not fix this scale. A separate constant contact
addition has zero pole residue; this last control is outside the frozen pure-quartic
grammar and tests residue-only selection, not the declared quartic theory.

Agda constructs actual native four-point factor executions for both couplings and
proves their rational readouts unequal. Its generic action-derivative theorem
applies to both. This extends the prior DSC action counterexample to the actual
amplitude coefficient interface; it is not a claim that no stronger source law
could select a theory or parameter.

Disposition: arithmetic incompleteness is removed, normalization is held fixed,
and a free contact coupling survives. The present conditions do not determine the
physical weights. The missing source datum is an independently justified action/
parameter selector, plus the quantum pairing/pole prescription. This selection
branch stops here until such source material exists; no new waiting issue or
observer-fitted condition is manufactured.

## Verification

Fresh safe/cubical compilation passes, including generic formal derivatives,
nonzero integer inversion, all ten channel equalities and the native unequal-readout
proof. The existing `FiniteFiberAmplitude.agda:19` naming warning remains nonfatal.

The exact symbolic audit also detects:

- omitted vertex factorial: residual `-23 lambda`;
- using K instead of its inverse: residual `i(K^2-1)`;
- reversed tree sign: residual `2 lambda^2/K`;
- a contact addition invisible to pole residues.

Commands through structured-command:

```text
pwsh -NoProfile -File research/nima/checkers/check_scalar_action_weights.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_scalar_action_weights.py
uv run --with sympy python research/aspect/scc/scc.py check nima-scalar-action-weights
```

Receipts: `results/agda-ScalarActionWeights.json` and
`results/scalar-action-weights.json`. The latter verifies the current 23-module
local formal import closure and binds the source fixture and reference evaluator.
The symbolic Gaussian calculation is not an Agda theorem or a constructive measure
result. No coupling prediction, physical realization of bare fibration, arbitrary-n
compiler certification, loop measure or independent review is claimed.

New sources, checkers, manifest, packet and generated evidence are uncommitted;
no existing researcher source was changed and no computation remains active.
Graph stimulus and report were admitted at sequence 15605,
`ev-000000015605-ee4f6b76-cbd6-4875-bd13-d978464700cb`, and remain uncommitted.
Earlier arithmetic reports at 15601 and 15604 remain uncommitted as recorded in
`completed-component-arithmetic.md`; graph admission is not truth certification.
