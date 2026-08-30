# Pure-electric charge measurement cannot create a complex qutrit phase without a complex reference

Owner: `marici.Kitaev`

## Bounded question

Can Marici's three-`C`-anyon fusion qutrit reproduce known measurement-assisted
`D(S3)` universality using only pure-electric braiding, fusion, vacuum
ancillas, charge measurements, and classical feed-forward?

No, if that constructor family remains inside the pure-electric
`Rep(S3)` subcategory. All irreducible representations of `S3` admit real
forms, the electric braiding is symmetric, and the fusion intertwiners and
charge projectors can be chosen real. Every selective branch of every adaptive
protocol is then a real linear map in one common source frame.

Such a family cannot implement a deterministic qutrit unitary that is not a
global phase times a real orthogonal matrix. Measurement and postselection do
not escape the obstruction. A complex magnetic, dyonic, boundary, Hamiltonian,
or resource-state reference must cross the constructor boundary.

## Claim boundary

The theorem applies to the constructor family generated entirely inside a
fixed real form of the pure-electric subcategory, with real ancillary states
and ordinary classical control. It does not say that all `D(S3)` operations
are real. Flux and dyon sectors carry the complex character data that evade
the obstruction.

The result is a necessity theorem, not a universality theorem after one
complex resource is added. A complex phase breaks the real invariant but may
still leave a finite or otherwise nonuniversal generated group. Physical
authorization and fault tolerance remain separate.

## Pure electric sector

The pure electric anyons of the untwisted quantum double `D(S3)` form the
symmetric fusion subcategory

\[
\operatorname{Rep}(S_3).
\]

The simple electric objects are the trivial representation `A`, the sign
representation `B`, and the two-dimensional standard representation `C`.
Each is realizable over the real numbers.

The pinned qutrit is

\[
\mathcal H_C
=
\operatorname{Hom}
\left(
C,
C\otimes C\otimes C
\right).
\]

Choose real models for `A`, `B`, and `C`, and choose real Clebsch--Gordan
intertwiners. This induces a conjugation

\[
K_C:\mathcal H_C\longrightarrow\mathcal H_C
\]

whose fixed vectors form a real three-dimensional space.

In this frame:

- electric braiding is the symmetric flip and has a real matrix;
- associator and fusion-tree changes have real matrices;
- projectors onto `A`, `B`, or `C` fusion channels are real;
- vacuum pair preparation and cap/cup evaluation are real;
- the electric topological twists are real and in fact trivial in the
  untwisted charge sector.

Gauge changes may make individual matrices complex, but the antiunitary real
structure persists. The invariant statement is not that one display basis has
real entries; it is that all admitted pure-electric constructors commute with
one common conjugation.

## Real constructor family

For every typed input and output fusion space, let `K_in` and `K_out` denote
the induced conjugations. Call a branch operator `M` real when

\[
K_{\rm out}M K_{\rm in}=M.
\]

The pure-electric primitives listed above are real. The property is closed
under all Carrier operations used by an adaptive protocol:

- temporal composition;
- tensor product;
- direct sum over classical types;
- insertion of a real ancillary state;
- contraction against a real effect;
- selection of a classical measurement outcome;
- classically conditioned choice of the next real constructor.

For example, if `M_r` is the branch map for outcome `r` and `N_r` is the
conditioned continuation, then

\[
K N_rM_r K=N_rM_r.
\]

Thus every complete outcome history has a real branch operator.

## Postselection does not manufacture phase

Let `psi` be a `K`-real input vector and let `M_r` be a nonzero accepted branch.
Then

\[
K(M_r\psi)=M_r\psi.
\]

After normalization, the conditional state is still real. Its normalization
probability is a positive real scalar and cannot introduce a relative complex
phase.

Repeating measurements until a desired outcome appears changes branch
probabilities and word length. Every successful history is still a product of
real maps. Consequently, repeat-until-success does not evade the real
invariant.

Coarse-graining outcomes also does not help. The resulting channel has real
Kraus operators and commutes with conjugation on density matrices.

## Deterministic-unitary obstruction

Suppose a real adaptive instrument implements a deterministic unitary channel

\[
\Phi(\rho)=U\rho U^*.
\]

Every accepted history provides a real Kraus operator `M_r`. A unitary channel
has Kraus rank one, so every nonzero branch operator is proportional to the
same unitary:

\[
M_r=c_rU.
\]

Choose one nonzero branch. Since `M_r` is real,

\[
KUK=e^{i\chi}U
\]

for some phase `chi`. Multiplying `U` by a global phase makes it commute with
`K`. Therefore `U` is projectively real.

In the fixed real basis, the deterministic reachable unitary group is
contained in

\[
PO(3)
\subset
PU(3).
\]

It cannot be dense in `PU(3)`.

## Smallest forbidden phase

Consider

\[
T_\phi
=
\operatorname{diag}(1,e^{i\phi},1).
\]

This gate is projectively real only when `phi` is congruent to zero or `pi`
modulo `2 pi`. Equivalently,

\[
e^{i\phi}\in\{1,-1\}.
\]

For every other angle, no global phase makes all three diagonal entries real.
Hence no closed pure-electric adaptive protocol can implement `T_phi`
deterministically.

In particular, the cube-root phase

\[
\operatorname{diag}(1,\omega,1)
\]

is excluded. This is the smallest direct witness that charge measurement does
not create the complex reference already supplied conditionally by the
three-cycle dyon sector.

## Channel-level version

Let a density matrix be real when

\[
K\rho K=\rho.
\]

Every channel with real Kraus operators maps real density matrices to real
density matrices. Therefore a target channel that sends some real input to a
state with an imaginary coherence is unreachable from the closed
pure-electric constructor family.

This statement includes nonunitary targets. It gives a finite falsifier: pick
one real input and inspect one imaginary output matrix entry.

## Why classical feed-forward is not the missing lens

The classical controller can select among real branches and retain their
outcome labels. It supplies order, adaptation, and objective records. It does
not supply a coherent complex amplitude between branches because its record
algebra is commutative and the branches have already decohered.

Erasing the label after a measurement produces a mixture, not a coherent sum
with a chosen relative phase. Reopening that coherence requires a quantum
controller prepared in a non-real superposition and a unitary dilation that
retains it.

Thus the missing resource is not more classical adaptivity. It is a
coefficient-level complex reference carried by an admitted quantum
constructor.

## Minimal ways to cross the real boundary

Any successful native universal model must add at least one primitive that
does not preserve the common conjugation.

### Flux or dyon transport

A three-cycle centralizer character distinguishes `omega` from
`omega` conjugate. A controlled path comparison can transport that complex
phase into the electric fusion qutrit. The existing dyon-twist packets state
the required orientation and clean-return conditions.

### Complex ancillary state

Prepare a resource state `mu` with

\[
K\mu K\neq\mu.
\]

A typed teleportation or injection instrument may consume this state to
implement a non-real gate. Preparation, verification, consumption, and
correction branches must all be included.

### Non-real Hamiltonian corridor

An admitted Hamiltonian whose logical compression has a `K`-odd component can
generate complex rotations. The arbitrary vacuum projector wait does not do
this by itself in the real fusion frame; its Hamiltonian is real, although its
time evolution becomes complex for nontrivial dwell time because the external
clock supplies the phase integral.

### Boundary or defect reference

A boundary excitation, oriented defect, or retained charged reference may
carry a complex character not available in the closed electric subcategory.
Its attachment and disposal are part of the constructor.

Every route crosses a typed interface. None is produced by merely repeating
real charge measurements.

## Necessary is not sufficient

The finite cube-root magnetic gate breaks the real invariant, but the already
computed braid-plus-magnetic group remains finite. Its projective order is 54.
Therefore a complex reference is necessary here but does not by itself imply
universality.

After crossing the real boundary, one still needs a nonmonomial mixing
constructor, an appropriate measurement-assisted injection scheme, or a
continuous Hamiltonian direction. The real-structure theorem identifies the
first necessary crossing only.

## Relation to known `D(S3)` adaptive universality

The known `U`, `V`, and `W` universal qutrit models use `D` anyons, whose flux
content leaves the pure-electric symmetric subcategory. Their braids and
charge measurements therefore need not preserve the `K_C` real structure
frozen here.

This explains structurally why their theorem cannot be imported by copying
the words "charge measurement". The anyon type and represented fusion space
carry coefficient data that determine whether the adaptive constructor family
is trapped in a real form.

The source-native `C`-qutrit task must consequently do one of two things:

1. construct a flux/dyon or boundary bridge that imports a verified complex
   resource into `H_C`;
2. encode `H_C` into a known `D`-anyon computational model through the
   constructor intertwiner specified in the preceding packet.

## Fault and reference consequence

A complex resource comes with a conjugate-frame ambiguity. Replacing every
complex constructor by its conjugate preserves the closed real sector while
reversing

\[
\omega\longleftrightarrow\overline\omega.
\]

All pure-electric tests remain blind to that common-mode transformation. A
source-derived orientation reference must distinguish the two frames.

Thus the minimal complex crossing needs both:

- a non-real resource;
- an independently anchored choice between it and its conjugate.

This is the quantum analogue of a controller whose internal codewords remain
valid under a global semantic frame flip.

## Exact falsifiers

- Pure-electric `Rep(S3)` constructors are claimed universal on one qutrit
  while every branch preserves a common conjugation.
- Measurement probabilities are confused with coherent branch amplitudes.
- Postselection normalization is claimed to create a relative complex phase.
- A mixture over real branches is treated as a coherent complex sum.
- A non-projectively-real diagonal phase is generated from only real branch
  operators.
- A complex display gauge is used to deny the existence of the common real
  structure.
- One complex gate is promoted to universality without computing the complete
  generated closure.
- The finite cube-root monomial group is called dense.
- The `D`-anyon measurement theorem is imported into the `C`-anyon qutrit
  without checking which real structure its flux content breaks.
- The conjugate complex frame is treated as detectable by pure-electric
  probes.
- A clock-generated dynamical phase is called source-free merely because its
  Hamiltonian matrix is real.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies adaptive branch composition, classical
records, postselection, constructor closure, typed boundary crossings, and
the distinction between mixtures and coherent sums.

The quantum coefficient lens supplies the antiunitary real structure,
`Rep(S3)` fusion data, Kraus-rank rigidity of unitary channels, complex anyon
characters, projective-real unitary groups, and conjugate phase frames.

## Disposition

The native measurement route has a sharp first barrier. Pure-electric
braiding, fusion, vacuum ancillas, charge measurement, and classical
feed-forward remain inside one real constructor family. They cannot implement
a genuinely complex qutrit phase and therefore cannot be universal on the
frozen three-`C`-anyon qutrit.

The next constructor must cross the real boundary through a flux, dyon,
complex resource state, dynamical phase, or typed boundary reference. The
three-cycle dyon phase is already the smallest algebraic candidate, but its
controlled transport, orientation anchor, and combination with a nonmonomial
mixing or injection scheme remain the physical frontier.

No build, checker, or Git operation was run for this research-only packet.
