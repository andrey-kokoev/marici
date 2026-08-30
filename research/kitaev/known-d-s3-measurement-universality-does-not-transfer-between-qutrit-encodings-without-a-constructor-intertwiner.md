# Known `D(S3)` measurement universality does not transfer between qutrit encodings without a constructor intertwiner

Owner: `marici.Kitaev`

## Bounded question

Does the known measurement-assisted universality of `D(S3)` anyons close the
physical-controllability gap for Marici's protected three-`C`-anyon fusion
qutrit?

Not directly. The literature proves universality for qutrit encodings built
from `D` anyons and particular intermediate charge measurements. Marici's
pinned qutrit is the multiplicity space of three electric `C` anyons with
total charge `C`. Equality of Hilbert-space dimension gives an abstract
unitary isomorphism, but it does not transport the braid representation,
charge effects, ancillary states, leakage sectors, or physical constructor
words.

The correct transfer object is a fault-filtered constructor intertwiner. Until
such an intertwiner is built, the literature supplies a highly relevant
existence template and a concrete primitive inventory, not a theorem about
the frozen Marici encoding.

## Claim boundary

This packet is a source audit and an abstract transfer theorem. It does not
rederive the matrices or universality proofs in the cited papers, certify the
recent circuit proposals experimentally, or construct a conversion between
the `C`-anyon and `D`-anyon qutrits.

The 2015 source explicitly separates its algebraic adaptive model from the
physical justification of the extra measurements and from leakage analysis.
Later sources provide more concrete lattice and circuit realizations, but
their exact fault model and encoding must still be matched to Marici's frozen
objects before their conclusions are imported.

## Source-native result already available

Cui, Hong, and Wang prove that all `D(S3)` braid images are finite and hence
braiding alone is not universal. They define three qutrit models, called `U`,
`V`, and `W`. Their main adaptive results are:

- the `U` and `V` models become universal using braiding plus two specified
  charge measurements;
- the `W` model additionally uses a specified ancillary state;
- successful adaptive conversions are repeat-until-success, with failure
  probability decreasing exponentially in the number of trials;
- a two-qutrit controlled phase is obtained by an explicit braid word;
- universality then uses classical qutrit gates, generalized Hadamard, `SUM`,
  and a noncomputational-basis measurement.

The source also states that the physical justification of the added
measurements and the leakage problem are not addressed in that algebraic
model.

The paper is:

- Shawn X. Cui, Seung-Moon Hong, and Zhenghan Wang, *Universal quantum
  computation with weakly integral anyons*, 2015,
  https://arxiv.org/abs/1401.7096.

Chen, Ren, Fan, and Jaffe subsequently give explicit circuits for creating,
moving, and locally measuring all nontrivial `D(S3)` anyons, together with a
remote total-charge interferometer and an active-error-correction proposal:

- Liyuan Chen, Yuanjie Ren, Ruihua Fan, and Arthur Jaffe, *A Universal Circuit
  Set Using the S3 Quantum Double*, 2024,
  https://arxiv.org/abs/2411.09697.

A later pedagogical exposition makes braiding and measurement concrete in the
`S3` quantum-double lattice using generalized ribbon operators:

- Chiu Fan Bowen Lo, Anasuya Lyons, Ruben Verresen, Ashvin Vishwanath, and
  Nathanan Tantivasadakarn, *Universal Quantum Computation with the S3 Quantum
  Double: A Pedagogical Exposition*, 2025,
  https://arxiv.org/abs/2502.14974.

These sources materially change the Marici frontier. Measurement-assisted
`D(S3)` universality is not conjectural. The remaining issue is exact
constructor transport into the encoding and fault contract frozen here.

## The two qutrit objects are differently typed

Marici's current protected qutrit is

\[
\mathcal H_C
=
\operatorname{Hom}
\left(
C,
C\otimes C\otimes C
\right),
\]

which has dimension three. Its current logical data include:

- two electric braid generators acting as `1` plus the standard
  two-dimensional representation;
- a native first-pair vacuum projector `P_A`;
- a three-cycle-flux cube-root gate candidate;
- a finite monomial group and its nine-effect SIC orbit;
- a conditional continuous vacuum-wait corridor.

The `U`, `V`, and `W` models in Cui--Hong--Wang are selected qutrit subspaces
inside fusion spaces of four `D` anyons. Their basis labels, braid group,
intermediate total-charge sectors, and leakage complement are different. In
particular, their adaptive measurements act on charge decompositions native
to those four-anyon spaces.

Thus the comparison is not

\[
\mathbb C^3\cong\mathbb C^3.
\]

It is a comparison of two represented and instrumented fusion objects.

## Abstract state-space isomorphism is vacuous here

Choose any unitary

\[
J:\mathcal H_C\longrightarrow\mathcal H_U.
\]

For every logical unitary `W` on `H_U`, the conjugate

\[
J^*WJ
\]

is a unitary on `H_C`. This proves no physical transfer. It silently treats
`J` and `J*` as executable operations and forgets that `W` may be an adaptive
instrument whose branches leave and re-enter the computational subspace.

The same mistake would make every universal qutrit platform a physical
compiler for every other qutrit platform merely because both have dimension
three.

## Constructor-intertwiner theorem

Let `C_C` and `C_U` be the admitted physical constructor categories for the
two encodings, and let

\[
\Lambda_C,
\qquad
\Lambda_U
\]

be their accepted logical evaluations.

A universality theorem transfers from `H_U` to `H_C` only after supplying the
following data.

### Executable encoding and decoding

There must be physical constructors

\[
E:\mathcal H_C\longrightarrow\mathcal H_U,
\qquad
D:\mathcal H_U\longrightarrow\mathcal H_C
\]

whose accepted logical maps satisfy

\[
DE=I_{\mathcal H_C}
\]

up to the declared tolerance and correctable record. Their microscopic
domains include the required anyon creation, charge conversion, ancillary
inventory, and total-charge constraints.

### Primitive intertwining

For every imported primitive constructor `g` used by the universal compiler,
there must be an admitted `C`-side implementation `g_C` such that

\[
D\,\Lambda_U(g)\,E
=
\Lambda_C(g_C)
\]

as channels or instruments, not only as selected scalar probabilities.

If `g` has measurement outcomes `r`, the equality is branchwise:

\[
D\,\Lambda_{U,r}(g)\,E
=
\Lambda_{C,r}(g_C),
\]

with the same outcome typing, probabilities, retained records, and authorized
feed-forward.

### Leakage compatibility

The image of `E` must enter the declared `U`-model computational subspace.
Every intermediate leakage sector reached by the adaptive protocol must be
typed, and `D` must be defined on every accepted terminal sector. Projecting
away an untyped branch is not a deterministic transfer.

### Composition coherence

For constructor words, repeated encode--operate--decode steps must compose
without accumulating an untracked frame, ancilla, or charge-sector cocycle.
Equivalently, the transfer is a functor up to declared correctable coherence
cells, not a collection of unrelated matrix conjugacies.

### Uniform fault filtration

The encoding, imported primitives, measurements, recovery, and decoding must
obey one common causal fault model. A single fault may not spread through the
conversion corridor into an uncorrectable logical operation. Success
probability, leakage, support, duration, and logical error must satisfy the
declared scaling contract.

Given these five items, any finite adaptive `U`-side compiler word transports
to a `C`-side word by composition. Density or universality then transfers with
the accumulated error and success bounds supplied by the intertwiner packet.

Without any one item, the transport theorem is undefined or false.

## The first typing obstruction

The two encodings do not even carry actions of the same raw braid group:

- the Marici qutrit begins with three `C` strands;
- the literature models use four `D` strands and selected total-charge
  sectors.

Therefore a simple relation

\[
J\rho_C(\sigma_i)=\rho_U(\sigma_i)J
\]

is not yet typed. One first needs a map from `C`-side spacetime constructors
to `D`-side braid and measurement words, including creation or removal of the
additional strand and the anyon-type conversion.

This is stronger than a representation-equivalence problem. It is a fusion
module and constructor-functor problem.

## Minimal algebraic falsifiers for a proposed bridge

Even before microscopic compilation, a candidate `J` can fail through finite
invariants.

### Braid-spectrum mismatch

If a declared `C` braid is mapped to a `U` braid word with a different
projective spectrum, no unitary intertwiner exists for that assignment.

### Fusion-projector mismatch

If

\[
JP_AJ^*
\]

does not equal the declared literature charge effect, the native vacuum test
has not been transported.

### Instrument mismatch

Two measurements can have conjugate effects while their postmeasurement
states, leakage branches, or classical records differ. Effect equality is
insufficient for adaptive computation.

### Tensor mismatch

A one-qutrit unitary bridge may fail to map the two-qutrit fusion embedding.
Then the imported controlled phase or `SUM` gate has no compatible action on
two encoded Marici qutrits.

### Frame mismatch

A common conjugation can preserve unlabeled transition probabilities while
reversing the cube-root orientation or relabeling charge outcomes. A source
anchor must fix the based frame.

## Two legitimate research routes

### Route A: physical encoding conversion

Construct `E` and `D` between the three-`C` fusion qutrit and one literature
four-`D` qutrit. Then import the established adaptive universal gate set with
branchwise records and fault filtration.

This route must explain how electric charges are converted into, or coupled
to, transposition-flux anyons without erasing the protected state.

### Route B: native measurement universality

Retain `H_C` and seek analogues of the literature's charge measurements and
ancillary states directly in its fusion category. Prove universality for the
finite electric/magnetic gate group plus those native instruments.

The existing vacuum effect and SIC tester are not automatically sufficient.
A rank-one measurement directly on the unknown data qutrit is destructive.
Measurement-assisted unitary computation generally needs entangled ancillas,
teleportation structure, repeat-until-success branches, or a reversible
fusion-space conversion.

Route B is likely the smaller Marici-native theorem. Route A has stronger
external physical precedent.

## Revised physical frontier

The prior arbitrary vacuum-wait programme remains a valid hybrid-control
route. It is no longer the only known route to universality in `D(S3)`.

The source-informed hierarchy is now:

1. braiding alone has finite image;
2. arbitrary vacuum waiting gives conditional continuous `U(3)` control on
   the Marici qutrit;
3. one irrational fixed vacuum phase gives conditional dense control;
4. measurement and ancilla augmentation is known to give universal `D(S3)`
   qutrit models;
5. transfer of item 4 to the frozen Marici qutrit requires a constructor
   intertwiner or a native rederivation.

Item 4 prevents us from treating analog waiting as conceptually necessary.
Item 5 prevents us from declaring the current physical gap closed.

## Exact falsifiers

- The literature result is described as braiding-only universality.
- Three-dimensional Hilbert-space isomorphism is treated as constructor
  equivalence.
- A four-`D`-anyon charge measurement is applied to the three-`C`-anyon space
  without an encoding map.
- Selected outcome probabilities are used in place of branchwise instrument
  equality.
- A repeat-until-success protocol is called deterministic without retaining
  its outcome record and failure branches.
- A one-qutrit intertwiner is used to import a two-qutrit gate without tensor
  compatibility.
- Leakage omitted by the 2015 algebraic model is silently treated as solved.
- A recent lattice circuit is imported without matching its code, locality,
  and fault model to the frozen Marici source.
- The native rank-one vacuum effect is claimed to implement a nondestructive
  universal measurement gate on an unknown qutrit by itself.
- The existence of one universal `D(S3)` encoding is treated as universality
  of every `D(S3)` fusion encoding.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies typed state spaces, executable encoding and
decoding, branchwise records, constructor functors, tensor compatibility,
leakage ports, and fault-filtered composition.

The quantum coefficient lens supplies anyon labels, fusion spaces, braid
representations, charge-measurement instruments, ancillary topological
states, qutrit universality, and projective frame data.

## Disposition

The external source changes the programme substantially: universal adaptive
computation with `D(S3)` anyons is already an established algebraic result,
and explicit lattice constructor proposals now exist. The right Marici task
is therefore no longer to ask whether `D(S3)` can be universal in principle.

The first unresolved arrow for the pinned three-`C`-anyon qutrit is an exact
constructor intertwiner to one of the known four-`D`-anyon universal models,
or a native proof that the required charge measurements and ancillas act on
`H_C`. Until that arrow is supplied, known universality is a source-native
template rather than a transported theorem.

No build, checker, or Git operation was run for this research-only packet.
