# Continuous vacuum wait gives universality by leaving topological gate equivalence

Owner: `marici.Kitaev`

## Bounded question

The protected `D(S3)` fusion qutrit has a finite electric-braid and magnetic
gate group. Adding arbitrary waiting time under the native vacuum projector,
together with discrete electric braids, generates `U(3)`. Is that continuous
control itself topologically protected?

No. A logical operation that is invariant under all sufficiently small
admissible deformations is locally constant on each connected component of
protocol space. Evolution under a non-scalar projector varies continuously
and nontrivially in projective unitary space. Its waiting time is therefore an
analog control coordinate, not a topological label.

The result does not defeat the qutrit controllability theorem. It identifies
its physical price. The finite braids may be topological transports, while
the continuously selected vacuum-relative phase requires calibration,
active fault handling, or replacement by a separately protected discrete
gate.

## Claim boundary

The local-constancy theorem is exact for the stated definition of topological
gate equivalence, and its application to a rank-one vacuum projector is exact.
It does not prove that the frozen electric braids have a microscopic
fault-tolerant realization, that a particular vacuum corridor remains gapped,
or that any fixed vacuum angle enlarges the finite gate group densely. Those
are independent source and synthesis theorems. Approximate geometric
robustness, composite-pulse cancellation, and active quantum error correction
may suppress analog phase error without making the waiting coordinate an
exact topological invariant.

## Topological gate equivalence

Let `P_adm` be a space of admitted physical protocols. A point records the
complete typed path: anyon trajectories, Hamiltonians, code projectors,
ancillas, records, and recovery instructions. Let

\[
\mathcal U:\mathcal P_{\rm adm}\longrightarrow PU(d)
\]

be the accepted logical operation, modulo global phase.

Call the realization exactly topological on an admitted region when
`mathcal U` is invariant under every continuous deformation in that region
that preserves the declared topological data and avoids forbidden events such
as charge collision, gap closure, boundary crossing, or record leakage.

Equivalently, `mathcal U` factors through the connected-component set

\[
\pi_0(\mathcal P_{\rm adm}).
\]

This definition is deliberately stronger than small numerical sensitivity.
It expresses exact dependence on a discrete path class rather than on metric
details of the path.

## Local-constancy theorem

Let

\[
s\longmapsto c_s
\]

be a continuous family of admitted protocols contained in one connected
topological class. If the logical realization is exactly topological, then

\[
\mathcal U(c_s)
\]

is constant in `PU(d)`.

The proof is immediate from factorization through `pi_0`: every `c_s` has the
same component label, and the logical operation depends only on that label.

Consequently, a differentiable one-parameter logical family

\[
U(s)=e^{-isH}
\]

can be topological throughout an open interval only when its projective
generator vanishes:

\[
H-\frac{\operatorname{Tr}H}{d}I=0.
\]

Thus `H` must be scalar. A non-scalar Hamiltonian supplies a genuine metric
control direction and cannot be selected by continuously varying an otherwise
unchanged topological path class.

## Application to the vacuum corridor

For the protected fusion qutrit, the native waiting pulse is, up to an
irrelevant scalar energy and scale,

\[
U_A(t)=e^{-itP_A},
\]

where

\[
P_A=|A_L\rangle\langle A_L|
\]

has rank one. Its projective infinitesimal generator is

\[
P_A-\frac13I,
\]

which is nonzero. Hence the family `U_A(t)` is not locally constant in
`PU(3)`.

Two waiting times give the same projective gate exactly when their difference
is an integer multiple of `2 pi`. In every smaller open interval, changing
the waiting time changes the logical gate.

The continuous vacuum wait therefore obtains its control power precisely from
data that topology does not erase: elapsed time and the integrated
vacuum--nonvacuum energy splitting.

## Quantitative timing sensitivity

Let the intended phase be `theta` and let the implemented phase be
`theta+delta`. The relative logical error is

\[
e^{-i\delta P_A}.
\]

On a superposition of one vacuum vector and one orthogonal vector, the ideal
and faulty outputs have trace distance

\[
2\left|\sin\frac{\delta}{2}\right|.
\]

For `|delta|` no larger than `pi`, this is also the diamond distance between
the two unitary channels. In particular, the logical error is first order in
small phase error.

If the energy splitting is `Delta`, then the intended phase is

\[
\theta=\Delta t.
\]

Small timing and calibration errors give

\[
\delta\theta
=
\Delta\,\delta t+t\,\delta\Delta
+\delta t\,\delta\Delta.
\]

Topological separation of the anyons does not quantize or syndrome this
overrotation. It may suppress other faults while leaving this commanded
logical direction exposed.

## Why dense topological computation is not excluded

The theorem does not say that a topological gate image must be finite. A
discrete set of braid words can have a dense image in a projective unitary
group. Each word is still attached to a discrete topological class; density
arises from longer discrete compositions, not from continuously deforming one
word to tune its gate.

For the frozen `D(S3)` qutrit, however, the already derived discrete
braid-plus-cube-root image is finite. Its projective order is 54. The present
`U(3)` theorem reaches beyond that finite image by introducing the metric
waiting coordinate.

This yields a precise trichotomy.

1. Discrete topological words may already have dense image. Then no analog
   wait is required for universality.
2. A separately protected fixed non-topological gate may enlarge the discrete
   image to a dense group. Its protection requires an independent theorem.
3. Arbitrary-time waiting supplies Lie controllability, but its phase accuracy
   is an analog control obligation.

The present `D(S3)` result establishes the third case. It does not yet
establish the second.

## Physical compiler consequence

The qutrit compiler should no longer be described by the single adjective
`topological`. It is a hybrid realization:

- electric braid words provide discrete routing of the three qutrit axes;
- the coherent fusion corridor exposes the vacuum projector;
- elapsed time supplies a continuous phase;
- inverse transport closes the corridor;
- calibration and fault handling price the analog phase.

The logical `U(3)` Lie closure remains exact. What changes is the fault claim.
Topology can protect the storage and discrete routing without automatically
protecting the continuously chosen rotation angle.

## Smallest fault-tolerant replacement question

The next source question is not whether arbitrary waiting times generate
`U(3)`; that is settled. It is whether the source provides one fixed,
independently certifiable vacuum phase

\[
V_\vartheta=e^{-i\vartheta P_A}
\]

such that the finite monomial group together with `V_vartheta` generates a
dense projective subgroup, and whether `V_vartheta` has a fault-tolerant
implementation.

There are three separate gates:

1. an algebraic density theorem for the chosen exact angle;
2. a microscopic constructor for that angle;
3. an error-correction or distillation theorem that suppresses its physical
   implementation error.

Passing the first does not imply either of the others. Conversely, a
continuously calibrated pulse may be useful physical control without being a
topological gate.

## Fault models exposed by the theorem

### Timing overrotation

The corridor is coherent and closes perfectly, but the dwell time is wrong.
The error is a syndrome-invisible logical rotation about `P_A`.

### Gap miscalibration

The commanded time is exact while the vacuum-relative energy splitting
drifts. Only the phase integral matters, so the logical fault is identical to
a timing error at the endpoint.

### Common-mode calibration

Every vacuum pulse and every internal calibration tester shares the same
mis-scaled clock or energy model. Internal relations can remain consistent
while all synthesized angles are wrong relative to an external reference.

### Corridor dephasing

Branch-dependent environment return destroys coherence. This is distinct
from analog overrotation: it changes a unitary pulse into a channel and is
detected by the existing rank-one environment Gram condition.

### Topological path fault

The braid word changes its discrete class. This is distinct from dwell-time
error and belongs to the topological routing fault model.

These fault classes require different witnesses. One storage syndrome cannot
be presumed jointly faithful on all of them.

## Exact falsifiers

- A non-scalar continuously tunable Hamiltonian is called exactly
  topological on one connected protocol class.
- Robustness under a finite list of perturbations is promoted to invariance
  under every admitted small deformation.
- The finite `D(S3)` braid image is called continuously universal without the
  vacuum wait or another nonfinite resource.
- Density of discrete braid words is confused with continuous tuning of one
  braid class.
- A waiting-time overrotation is claimed detectable by the passive topological
  syndrome without an added phase reference or encoded gadget.
- Exact Lie rank is promoted to a threshold theorem.
- A chosen fixed vacuum phase is called universal without proving density of
  the enlarged discrete group.
- Algebraic density is promoted to a protected microscopic implementation.
- A gap closing or charge collision is treated as a harmless deformation
  inside one admitted topological class.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies connected protocol classes, deformation
invariance, discrete route labels, metric dwell coordinates, and the
distinction between path-class robustness and calibrated continuous control.

The quantum coefficient lens supplies projective unitary action, the rank-one
vacuum projector, diamond-distance phase sensitivity, braid representations,
and the distinction between coherent overrotation and dephasing.

## Disposition

The protected `D(S3)` fusion qutrit has a hybrid control architecture.
Discrete electric braids can be topological, and their conjugation orbit turns
one vacuum projector into a Lie-complete Hamiltonian family. But continuously
choosing the vacuum dwell time is not topological: it varies within one
connected protocol class and produces first-order logical phase sensitivity.

Thus the existing `U(3)` theorem is an exact controllability result, not yet a
fault-tolerant topological-computation theorem. The next decisive move is to
replace arbitrary analog waiting by a fixed source-derived gate with separate
density and fault-tolerance certificates, or else to accept and explicitly
price calibrated analog control.

No build, checker, or Git operation was run for this research-only packet.
