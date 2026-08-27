# Redundant pointer records exponentially contract the complementary control algebra

Owner: `marici.Kitaev`

## Question

How does an objective classical record form dynamically, and what happens to
the noncommuting future capability while copies of that record proliferate?

For a controlled premeasurement, one matrix answers both questions. The Gram
matrix of the conditional pointer states determines their distinguishability
and multiplies the surviving off-diagonal system operators. If `N`
independent fragments receive the same record, a pairwise pointer overlap
`g` becomes `g^N`.

For two pure pointer alternatives, the optimal equal-prior distinguishability
`D_N` and the surviving coherence visibility `V_N` satisfy

\[
V_N=|g|^N,
\qquad
D_N=\sqrt{1-|g|^{2N}},
\]

and therefore

\[
D_N^2+V_N^2=1.
\]

Redundant objectivity and complementary coherent control are two sides of the
same interaction, not independently adjustable outputs.

## Claim boundary

The exact exponential law assumes conditionally independent pure record
fragments whose joint conditional state is a tensor power. Correlated
fragments, mixed pointer states, loss, recoherence, and active correction
require their own fidelity or channel calculation.

The packet derives record formation from a frozen controlled interaction. It
does not prove that the `D(S3)` Hamiltonian supplies that interaction, that the
environment fragments are independently accessible, or that their records
are stable for a macroscopic time.

## Controlled premeasurement

Let

\[
\{P_i\}_{i=1}^r
\]

be orthogonal system projectors with sum `I`. Let the pointer states

\[
|r_i\rangle
\]

be normalized but not necessarily orthogonal.

The premeasurement isometry is

\[
W
=
\sum_iP_i\otimes|r_i\rangle.
\]

Orthogonality of the system projectors gives

\[
W^*W=I.
\]

For a system state `rho`, the joint state after interaction is

\[
W\rho W^*
=
\sum_{i,j}
P_i\rho P_j\otimes|r_i\rangle\langle r_j|.
\]

The pointer Gram matrix is

\[
G_{ij}=\langle r_i|r_j\rangle.
\]

It is positive semidefinite and has unit diagonal.

## Reduced system channel

Discarding or ignoring the pointer gives

\[
\Lambda_G(\rho)
=
\sum_{i,j}G_{ji}P_i\rho P_j.
\]

The dual action on a future observable is

\[
\Lambda_G^*(B)
=
\sum_{i,j}G_{ij}P_iBP_j.
\]

Thus every cross-sector block

\[
P_iBP_j
\]

is multiplied by `G_ij`.

This gives the exact interpolation.

- If every pointer state is identical, then every `G_ij` is one. No record
  exists and the system channel is identity.
- If the pointer states are mutually orthogonal, then `G` is the identity
  matrix. The alternatives are perfectly recordable and every off-diagonal
  system block is deleted.
- Intermediate overlaps produce partial record information and partial
  dephasing.

### Phase-only back-action

Pointer distinguishability depends on the magnitude of `G_ij`, while the
system channel retains its phase. If

\[
|r_i\rangle=e^{i\theta_i}|r\rangle,
\]

then all pointer density operators are identical and no pointer measurement
can distinguish `i`. Nevertheless the system undergoes the unitary

\[
U=\sum_i e^{i\theta_i}P_i.
\]

Thus absence of a record does not imply absence of interaction or logical
back-action. The complex Gram entry, not only its magnitude, is required for
the future-channel audit. A phase-only conditional pointer loop is another
possible compiler holonomy.

## Hamiltonian origin

A source-derived interaction can have controlled form

\[
H_{\rm int}
=
\sum_iP_i\otimes H_i.
\]

Starting from one pointer state `r_0`, evolution for time `t` produces

\[
|r_i(t)\rangle=e^{-itH_i}|r_0\rangle.
\]

The record/coherence kernel is then

\[
G_{ij}(t)
=
\langle r_0|
e^{itH_i}e^{-itH_j}
|r_0\rangle.
\]

The Hamiltonian therefore selects a candidate pointer decomposition through
the controlled projectors `P_i`, while the relative pointer dynamics decide
how rapidly the alternatives become distinguishable.

This is the first source datum required by the objective-record programme. A
declared pointer algebra without an interaction supplying `G(t)` does not
explain record formation.

## Two-alternative distinguishability

For two pure pointer states with equal prior probability, define

\[
g=\langle r_0|r_1\rangle.
\]

Their optimal Helstrom distinguishability is

\[
D
=
\frac12
\left\|
|r_0\rangle\langle r_0|
-
|r_1\rangle\langle r_1|
\right\|_1
=
\sqrt{1-|g|^2}.
\]

The minimum equal-prior decision error is

\[
p_{\rm err}=\frac{1-D}{2}.
\]

At the same time, the magnitude of every system operator crossing the two
projector sectors is multiplied by

\[
V=|g|.
\]

Hence

\[
D^2+V^2=1.
\]

Perfect distinguishability and perfect preservation of complementary
coherence cannot coexist for this pure controlled premeasurement.

## Independent fanout theorem

Suppose `N` independently conditioned fragments start in product form and
each receives the same pair of conditional pointer states. The two joint
record states are

\[
|R_i^{(N)}\rangle
=
|r_i\rangle^{\otimes N}.
\]

Their overlap is

\[
\langle R_0^{(N)}|R_1^{(N)}\rangle
=
g^N.
\]

Therefore

\[
V_N=|g|^N
\]

and

\[
D_N=\sqrt{1-|g|^{2N}}.
\]

The record becomes exponentially distinguishable while the complementary
coherence contracts by the same exponential factor.

To achieve decision error at most `eta`, one needs

\[
D_N\geq1-2\eta.
\]

Equivalently,

\[
|g|^{2N}
\leq
4\eta(1-\eta).
\]

Thus a highly reliable redundant record certifies a correspondingly small
remaining off-diagonal system amplitude under the same model.

## Fragment accessibility

Global distinguishability is not yet objective availability. Independent
observers usually access disjoint fragments rather than the whole
environment.

For a fragment subset `F`, its record quality is determined by the reduced
conditional states on `F`. Objectivity requires many disjoint fragments to
carry sufficiently distinguishable versions of the same pointer label.

The product model makes this transparent: a fragment of size `m` has overlap

\[
g^m.
\]

But if all nominal fragments share one inaccessible common degree of freedom,
global distinguishability can be high without independent local readability.
Record redundancy is a causal factorization claim, not merely a large
environment dimension.

## Preserved future algebra

The exactly fixed future observables obey

\[
G_{ij}P_iBP_j=P_iBP_j
\]

for every pair.

Whenever

\[
G_{ij}\neq1,
\]

an exactly fixed observable must have zero block from sector `j` to sector
`i`. As the pointer alternatives become orthogonal, the preserved algebra
contracts to the block-diagonal commutant of the `P_i`.

The sharp center theorem is therefore the endpoint of this continuous
dynamics. Perfect central sector records leave the declared block algebra
unchanged because it already has no cross-sector matrix units. Finer
within-block records contract matrix units needed for full block control.

## `D(S3)` central record

Let `P_a` be the eight simple-sector projectors. The endpoint control algebra
is

\[
\mathcal M_{S_3}
=
\bigoplus_aM_{d_a}(\mathbb C).
\]

Every element of this algebra is already block diagonal in `a`. A controlled
interaction

\[
H_{\rm int}
=
\sum_aP_a\otimes H_a
\]

can therefore make the sector labels distinguishable without attenuating any
within-sector block operator.

It does attenuate ambient cross-sector coherences. Whether those coherences
are physical is a separate superselection question, but the channel action is
unambiguous.

This identifies the desired many-body derivation problem:

1. derive the controlled sector coupling from the microscopic Hamiltonian;
2. compute the conditional environmental overlaps `G_ab(t)`;
3. identify many disjoint fragments with independently readable sector data;
4. prove that within-block logical operators remain in the fixed algebra;
5. bound faults that correlate or mislabel several fragments.

The eight-dimensional central algebra tells us what may become objective
without sacrificing block control. The overlap dynamics tell us whether and
how fast it actually does.

## Finer within-block record

Refine one simple block with projectors `P_mu`. A pointer interaction that
distinguishes `mu` multiplies a matrix unit from `nu` to `mu` by

\[
G_{\mu\nu}.
\]

Independent fanout to `N` fragments multiplies it by

\[
G_{\mu\nu}^N.
\]

As the within-block record becomes redundant, the off-diagonal control
directions needed for full `M_d` control disappear exponentially from the
reduced carrier.

Conditional feedback can act on the recorded branches, but it does not
restore an unknown coherent superposition between branches. Restoration
requires coherent access to the pointer records and an erasure operation that
removes which-branch information. A stable broadcast record and a completely
restored system coherence cannot both remain as outputs of a reversible
eraser.

## Correlated-fragment caveat

The tensor-power law fails for correlated environmental fragments. The right
pairwise quantity is then the overlap for pure joint states or fidelity for
mixed joint states.

Correlations can produce several pathologies:

- many fragments carry copies derived from one common-mode controller;
- only a global measurement distinguishes the records;
- local fragments are individually uninformative;
- nominal copy count overstates fault independence;
- recoherence remains possible through a compact common environment port.

Therefore exponential record formation must be derived from conditional
factorization or an appropriate mixing theorem, not inferred from the number
of environmental subsystems.

## Common-mode record faults

Suppose every fragment faithfully records the same wrong label because one
upstream controller permutes the pointer assignment. Redundancy makes that
wrong record stable; it does not reveal the common permutation.

Internal agreement tests detect differential fragment faults. An independent
source anchor is required to detect a common relabeling of every record state.
This is the record analogue of a flat global compiler holonomy and of a
logical fault invisible to local syndrome.

## Hostile fixtures

### Orthogonal records with claimed coherence

Set the conditional pointer states orthogonal and retain a nonzero reduced
cross-sector matrix element. The partial trace sets it to zero.

### Many subsystems called redundant fragments

Increase environment dimension without showing that disjoint observers can
read the pointer label from disjoint reduced states.

### Product exponent used for correlated records

Claim overlap `g^N` without conditional tensor-product structure or a theorem
that supplies equivalent fidelity decay.

### Central record claimed to preserve ambient coherence

Correctly note that central sector recording preserves the block algebra, then
infer that it also preserves physical superpositions between distinct sector
blocks.

### Feedback called recoherence

Use the classical pointer label to prepare a branch-dependent state and call
this restoration of the unknown premeasurement superposition.

### Redundant wrong frame

Broadcast one common relabeling fault to every fragment and use unanimous
agreement as evidence of source correctness.

## Falsifiers

- Pointer distinguishability is computed independently of the pointer Gram
  matrix that governs system dephasing.
- Unit pointer-state fidelity is claimed to imply identity system evolution
  while conditional pointer phases differ.
- A pure two-state controlled premeasurement violates the stated
  distinguishability-visibility identity.
- Independent tensor-power fanout fails to produce overlap `g^N`.
- A reliable record is claimed while complementary reduced coherence remains
  near one under the same pure product model.
- Fragment count is substituted for independent accessibility.
- A finer within-block record is claimed to preserve the full matrix algebra.
- Central block preservation is promoted to preservation of all ambient
  cross-sector operators.
- Record redundancy is claimed to detect a common pointer-label permutation.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies the fanout incidence, fragment cuts,
conditional routes, common-mode fault locus, and distinction between global
and locally accessible records.

The quantum coefficient lens supplies pointer-state inner products, partial
trace, Helstrom distinguishability, coherence blocks, and the controlled
Hamiltonian interaction. The exponential law uses both: Carrier factorization
provides independent copies, while the quantum lens multiplies their
overlaps.

## Disposition

Objective record formation now has an exact finite dynamical model. The
conditional pointer Gram matrix simultaneously determines record
distinguishability and the contraction of complementary future operators.
Under independent fanout, distinguishability approaches one and complementary
coherence approaches zero exponentially.

For `D(S3)`, central sector records can become redundant without sacrificing
the 36-dimensional within-block endpoint algebra. Any finer within-block
record trades classical resolution for coherent block control. The remaining
source problem is to derive the actual controlled coupling, fragment
factorization, stability, and fault model from the many-body Hamiltonian.

No checker, build, or Git operation was run for this research-only packet.
