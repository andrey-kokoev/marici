# The center is the maximal sharp record compatible with full endpoint control

Owner: `marici.Kitaev`

## Question

Which sharp classical records can be created without disturbing any future
operation in a frozen executable operator algebra?

For a sharp Lüders record whose projectors lie inside the executable algebra,
the answer is exact: every record projector must lie in the center. Therefore
the center is the maximal internal sharp record algebra compatible with
preserving the full future capability.

For the multiplicity-free `D(S3)` endpoint algebra, this identifies the
eight-dimensional central sector readout as maximal. Any sharper internal
record resolves information inside a simple block and necessarily destroys
some future block coherence.

## Claim boundary

The theorem is for finite-dimensional sharp projective records with the
declared Lüders update. Other instruments with the same effects can have
different disturbance properties, but a repeatable sharp nondemolition
implementation remains subject to related commutation constraints.

Algebraic compatibility does not construct the measuring apparatus, pointer
fanout, locality schedule, or fault-tolerant extraction. “Maximal record” here
means maximal internal sharp algebra under the stated nondisturbance contract.

## Executable algebra

Let

\[
\mathcal M\subseteq\operatorname{End}(\mathcal H)
\]

be the finite-dimensional algebra of future executable observables on the
accepted carrier.

Let

\[
\{P_i\}_{i=1}^r\subseteq\mathcal M
\]

be a projective record:

\[
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
\]

The unrecorded Lüders channel acts on future observables by

\[
\Lambda^*(B)=\sum_iP_iBP_i.
\]

The record preserves full endpoint capability when

\[
\Lambda^*(B)=B
\]

for every `B` in `M`.

## Maximal-center theorem

The following are equivalent.

1. The Lüders record preserves every future observable in `M`.
2. Every `P_i` commutes with every element of `M`.
3. Every `P_i` belongs to the center `Z(M)`.

### Proof

For a sharp Lüders channel, an operator `B` is fixed exactly when it commutes
with every projector `P_i`. Therefore fixing all of `M` is equivalent to

\[
P_i\in\mathcal M'
\]

for every `i`. By hypothesis the record is internal, so

\[
P_i\in\mathcal M.
\]

Hence

\[
P_i\in\mathcal M\cap\mathcal M'
=
Z(\mathcal M).
\]

Conversely, central projectors commute with all of `M`, so their Lüders
channel fixes all future executable observables.

Thus no noncentral internal sharp refinement can preserve the complete
algebra.

## Finite-algebra decomposition

Write the represented algebra in standard form as

\[
\mathcal H
=
\bigoplus_a
\left(\mathbb C^{m_a}\otimes\mathbb C^{d_a}\right),
\]

\[
\mathcal M
=
\bigoplus_a
\left(I_{m_a}\otimes M_{d_a}(\mathbb C)\right).
\]

Its commutant is

\[
\mathcal M'
=
\bigoplus_a
\left(M_{m_a}(\mathbb C)\otimes I_{d_a}\right),
\]

and its center is

\[
Z(\mathcal M)
=
\bigoplus_a\mathbb C I_{m_ad_a}.
\]

An internal record can preserve all of `M` only by resolving the central block
label `a`. It cannot resolve a basis coordinate inside a simple matrix block
without pinching some matrix units.

## External commutant records

The internality assumption matters. A projector in `M'` but not in `M` can
record a multiplicity, gauge, or ancillary coordinate while leaving `M`
undisturbed.

Such a record is not an internal logical observable. It belongs to a separate
commutant port. Its physical meaning and availability must be derived from the
source decomposition; equal tensor dimensions do not manufacture it.

For a multiplicity-free representation, every `m_a` equals one and

\[
\mathcal M'=Z(\mathcal M).
\]

Then even the external algebraic commutant supplies no sharper nondisturbing
projector than the sector center.

## `D(S3)` endpoint consequence

The represented endpoint block algebra is

\[
\mathcal M_{S_3}
=
\bigoplus_{a=1}^{8}M_{d_a}(\mathbb C),
\]

with

\[
(d_a)=(1,1,2,3,3,2,2,2).
\]

It has complex dimension

\[
\sum_ad_a^2=36
\]

and center dimension eight.

Each simple sector occurs once, so the representation is multiplicity-free.
Therefore

\[
\mathcal M_{S_3}'=Z(\mathcal M_{S_3}).
\]

The eight sector projectors generate the maximal sharp record algebra whose
Lüders channel preserves every future block observable. The previously frozen
twist and monodromy probes span this center exactly.

This gives the hierarchy a dynamical meaning:

- the eight-dimensional center is the maximal nondisturbing sharp internal
  record;
- the 36-dimensional block algebra is the retained coherent control algebra;
- resolving any of the 28 traceless within-block directions as a sharp record
  necessarily removes some complementary block coherence.

The 248-dimensional ambient kernel of the central probes is not an accidental
tomographic deficiency. Much of it is information that cannot be made into
the same nondisturbing classical record while preserving the declared future
algebra.

## Within-block hostile witness

Consider one two-dimensional simple block. Let the proposed sharper record be
the `Z` projectors

\[
P_\pm=\frac12(I\pm Z).
\]

Its Lüders channel fixes `I` and `Z` but sends

\[
X\longmapsto0,
\qquad
Y\longmapsto0.
\]

The record gains one within-block classical coordinate by deleting two
coherent future directions. It therefore reduces the executable algebra from
`M_2` to its diagonal commutative subalgebra.

No redundancy of the `Z` pointer restores the lost `X,Y` capability. More
copies make the selected record more objective while making its dephasing
harder to reverse.

## Toric-code consequence

On a fixed toric-code logical sector with two encoded qubits, the full logical
operator algebra is a matrix algebra and has only scalar center. Therefore no
nontrivial sharp logical-loop record can preserve every logical observable on
the same code copy.

An intersecting primal and dual logical loop anticommute. Recording one sharply
disturbs the other. They may be estimated in separate settings or on repeated
preparations, but they are not one simultaneous nondemolition classical
record.

Local stabilizer syndrome is different. Stabilizer projectors commute with the
logical algebra on the accepted decomposition and can record local error
syndrome without selecting a logical basis. This is why local syndrome can be
nondemolition yet remain blind to the logical sector.

Thus the earlier statement that two loop probes are jointly faithful on an
abelian homology defect class must not be transported untyped into the quantum
logical algebra. Classical defect diagnosis and simultaneous sharp quantum
recording have different coefficient requirements.

## Record-capability frontier

For a subalgebra

\[
\mathcal N\subseteq\mathcal M,
\]

a sharp record preserves `N` exactly when every record projector lies in the
commutant `N'`. Sharpening the record generally shrinks the preserved future
algebra to

\[
\mathcal M\cap\{P_i\}'.
\]

This defines a frontier:

- coarse central records preserve maximal coherent capability;
- finer records distinguish more present coordinates;
- each noncentral refinement removes future operators not commuting with the
  new pointer algebra.

The frontier is ordered by commutants, not by record-bit count alone.

## Objective record formation

A central PVM supplies a commutative candidate pointer algebra. Its values can
in principle be copied to many records without invoking the no-broadcasting
obstruction for unknown noncommuting states.

But centrality is only the algebraic compatibility gate. Objective record
formation additionally requires a source-derived interaction that:

1. correlates the sector projectors with pointer states;
2. makes those pointer states distinguishable and stable;
3. redundantly fans them out through sufficiently independent environments;
4. bounds back-action outside the central pinching already declared;
5. preserves the physical endpoint capability claimed after recording.

The center identifies what may be recorded nondestructively relative to `M`.
It does not explain how the environment selects or stabilizes that record.

## Controlled-context caveat

A phase or kernel action invisible inside the declared endpoint algebra can
become visible after adjoining a coherent control system. Enlarging the future
algebra can shrink its center and commutant.

Therefore maximality is relative to the frozen executable algebra. If a later
programme admits controlled-sector superpositions, external phase references,
or coherent higher-order maps, the nondisturbance audit must be repeated on
the enlarged algebra.

This is the same reason projective channel equivalence can fail under
controlled-unitary use.

## Hostile fixtures

### Full block control claimed after a basis record

Sharply record a basis coordinate inside a nontrivial simple block and retain
the claim that all block matrix units remain executable. The off-diagonal
units are removed by pinching.

### Central dimension called full tomography

Use the eight sector projectors to infer all 36 block coordinates or all 256
ambient Hermitian coordinates.

### Commutant multiplicity inferred from dimensions

Postulate an external gauge register because the Hilbert-space dimension
factorizes, without a source-derived representation decomposition.

### Separate settings called one objective record

Measure anticommuting toric loops on separately prepared copies and describe
the resulting tomography data as simultaneous nondemolition values on one
carrier.

### Algebraic center called a physical apparatus

Identify central projections but provide no interaction, pointer states,
fanout, stability, or fault model.

### Frozen-algebra maximality exported after enlargement

Prove a record central relative to one block algebra, then adjoin coherent
cross-sector controls without recomputing the commutant.

## Falsifiers

- A noncentral internal projector is claimed to preserve every element of
  `M` under its Lüders channel.
- A sharp record's preserved future algebra is larger than its commutant
  without a non-Lüders instrument theorem.
- The eight-dimensional `D(S3)` center is called the full 36-dimensional
  endpoint algebra.
- A within-block sharp record is claimed to preserve complementary matrix
  units.
- Joint faithfulness of classical loop coordinates is promoted to simultaneous
  sharp measurability of anticommuting logical loops.
- An external commutant port is inferred without source typing.
- Centrality is promoted to physical broadcast implementation.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies subalgebra inclusion, commutant restriction,
record refinement, and the change of future capability after a cut. The
quantum coefficient lens supplies completely positive Lüders dynamics,
matrix-block coherence, anticommutation, and the difference between a sharp
effect and its recording instrument.

The center-commutant theorem is an operator-algebraic bridge between them. Its
application to anyons, logical loops, or pointer states requires the quantum
source typing.

## Disposition

The central `D(S3)` readout is now characterized by a maximality theorem. It is
the largest sharp internal record algebra that can be created by Lüders
pinching while preserving the full 36-dimensional endpoint block algebra.
Any sharper internal record sacrifices some noncommuting future capability.

This also fixes the loop-probe typing boundary. Two additive holonomy probes
can be jointly faithful on a classical cohomology class, while intersecting
quantum logical loops require incompatible sharp settings. The Carrier cycles
are shared; joint recordability is decided by the coefficient algebra and the
instrument.

No checker, build, or Git operation was run for this research-only packet.
