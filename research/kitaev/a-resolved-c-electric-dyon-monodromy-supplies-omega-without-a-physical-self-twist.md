# A resolved C-electric--dyon monodromy supplies omega without a physical self-twist

Owner: `marici.Kitaev`

## Bounded question

Can the intrinsic cube-root phase needed by the sixth-root qutrit constructor
be implemented using the standard anyonic command set of creation, braiding,
fusion-channel preparation, and measurement, without assuming that a framed
self-twist is directly executable on the lattice?

Yes at the ribbon-category level. Let `D_k` denote the three-cycle dyon whose
centralizer character is `chi_k`, and let `C` denote the standard
two-dimensional pure-electric charge. Their fusion has two multiplicity-free
channels:

\[
D_k\otimes C
\cong
D_{k+1}\oplus D_{k-1}.
\]

A full monodromy of `D_k` and `C` acts by `omega` on the first channel and by
`omega` inverse on the second. Preparing one resolved channel therefore turns
an ordinary full braid into a clean scalar cube-root phase. Reverse braid
orientation or select the other channel to obtain the conjugate phase.

This replaces the questionable physical self-twist primitive with ordinary
anyon motion and fusion-channel control. The remaining gap is coherent
incidence: the full braid must occur on exactly the charged-bridge route that
carries `S`, without leaving a route or fusion record.

## Claim boundary and primary-source boundary

The fusion restriction and balancing-equation calculation below are exact in
the ribbon category of untwisted `D(S3)`.

Kitaev's original operational proposal admits unitary transformations by
moving anyons around one another and measurements by joining and fusing them.
Cowtan and Majid give explicit quantum-double ribbon operators and a lattice
braiding example, and identify the three `C3` centralizer-character sectors.
They also state that deterministic non-Abelian transport operations used in
their `D(S3)` computation discussion are assumed rather than constructed.

Primary sources:

- A. Kitaev, [Fault-tolerant quantum computation by anyons](https://arxiv.org/abs/quant-ph/9707021).
- A. Cowtan and S. Majid, [Quantum double aspects of surface code models](https://arxiv.org/abs/2107.04411).

Accordingly, this packet supplies an exact braid-level compiler target. It
does not claim that the required deterministic or coherently controlled
non-Abelian lattice transport has already been constructed.

## Three-cycle dyon labels

Write

\[
S_3=\langle r,t\mid r^3=t^2=e,\;trt=r^{-1}\rangle.
\]

The three-cycle conjugacy class and its centralizer are

\[
\mathcal C_3=\{r,r^{-1}\},
\qquad
Z_r=\langle r\rangle\cong C_3.
\]

For `k` modulo three, let

\[
\chi_k(r)=\omega^k.
\]

The corresponding simple quantum-double objects are denoted `D_k`. Each has
quantum dimension two and twist

\[
\theta_{D_k}=\omega^k.
\]

The standard pure-electric object `C` has twist

\[
\theta_C=1.
\]

## Restriction of the standard charge

Restrict the standard representation of `S3` to the three-cycle centralizer.
Its two eigencharacters are `chi_1` and `chi_-1`, so

\[
\operatorname{Res}^{S_3}_{C_3}C
\cong
\chi_1\oplus\chi_{-1}.
\]

Tensoring a `C3`-flux dyon by a pure-electric charge preserves the flux class
and tensors its centralizer representation by this restriction. Therefore

\[
D_k\otimes C
\cong
D_{k+1}\oplus D_{k-1}.
\]

The dimension check is exact:

\[
2\cdot2=2+2.
\]

Both fusion multiplicities are one. A fixed output charge therefore resolves
the channel without an additional multiplicity coordinate.

## Balancing-equation phase

Let

\[
M_{D_k,C}=c_{C,D_k}c_{D_k,C}
\]

be the chosen oriented full monodromy. In a ribbon category, its action on a
simple fusion channel `X` is

\[
M_{D_k,C}|_X
=
\frac{\theta_X}{\theta_{D_k}\theta_C}I_X.
\]

On the `D_{k+1}` channel this gives

\[
M_{D_k,C}|_{D_{k+1}}
=
\frac{\omega^{k+1}}{\omega^k}
I
=
\omega I.
\]

On the `D_{k-1}` channel it gives

\[
M_{D_k,C}|_{D_{k-1}}
=
\frac{\omega^{k-1}}{\omega^k}
I
=
\omega^{-1}I.
\]

The phase is independent of `k`. What matters is which of the two relative
fusion channels was selected.

Reversing the full braid replaces the monodromy by its inverse and exchanges
the two phase values.

## Minimal orientation resource

The simplest specialization takes the twist-trivial three-cycle fluxion
`D_0`. Then

\[
D_0\otimes C
\cong
D_1\oplus D_2.
\]

Full monodromy acts by `omega` on total charge `D_1` and by its conjugate on
total charge `D_2`.

Thus a nontrivial-spin ancilla need not be assumed at preparation. The
orientation resource can be localized entirely in one resolved fusion
channel of a `D_0` fluxion with the ordinary electric `C` charge.

The choice between `D_1` and `D_2` is one relational `C2` orientation bit.
It is a typed topological charge distinction, not an analog phase setting.

## Minimal globally neutral phase ancilla

The pair `D_0,C` in total channel `D_1` is not by itself creatable from the
vacuum: its total charge is nontrivial. Global charge conservation requires a
compensating reference.

Since

\[
D_1^*=D_2,
\]

the smallest vacuum-neutral preparation is the three-anyon packet

\[
\left(D_0\otimes C\longrightarrow D_1\right)
\otimes D_2
\longrightarrow A.
\]

It has a direct create--split--braid--re-fuse--annihilate realization in the
fusion category:

1. create a `D_1,D_2` pair in the vacuum channel;
2. split `D_1` through the unique channel into `D_0` and `C`;
3. perform one oriented full monodromy of `D_0` with `C`;
4. re-fuse `D_0,C` through the same channel to `D_1`;
5. annihilate `D_1,D_2` back into the vacuum.

Because the intermediate fusion multiplicity is one and the monodromy scalar
on it is `omega`, the closed ancillary history evaluates to `omega` times the
vacuum line. All topological charges and fusion ports return to their initial
state.

Applied unconditionally this is only a global phase. Applied coherently on
one of the two charged-bridge routes, it is exactly the required phase
kickback. This formulation makes the remaining constructor especially
precise: coherently control whether the entire vacuum-neutral loop is inserted
into the route history.

The conjugate loop is obtained by starting with the opposite orientation
channel or reversing the monodromy. It evaluates to `omega` inverse.

## Clean phase kickback

Prepare the `D_k,C` pair in the known total channel `D_{k+1}`. Let `Braid`
denote their full monodromy. Then for every state `phi` in that channel,

\[
Braid|\phi\rangle=\omega|\phi\rangle.
\]

If one coherent bridge route applies no braid and the other applies this full
braid, the joint state transforms as

\[
R|\psi\rangle\otimes|0\rangle\otimes|\phi\rangle
+
S|\psi\rangle\otimes|1\rangle\otimes|\phi\rangle
\]

to

\[
R|\psi\rangle\otimes|0\rangle\otimes|\phi\rangle
+
\omega S|\psi\rangle\otimes|1\rangle\otimes|\phi\rangle.
\]

The braid returns the phase ancilla exactly because monodromy is scalar on the
resolved multiplicity-one channel. Real `X` recombination then gives the
already derived branches

\[
K_{X+}=\frac{R+\omega S}{2},
\qquad
K_{X-}=\frac{R-\omega S}{2}.
\]

For the vacuum-projector cube-root holonomy, `X-` is the `3/4` sixth-root
success branch and `X+` is the `1/4` correctable failure.

## Why fusion-channel resolution is indispensable

If the total channel is unresolved, the braid is not scalar on the ancilla.
For a coherent superposition

\[
|\phi\rangle
=
a|\phi_+\rangle+b|\phi_-\rangle
\]

across the two fusion channels, the braided route carries

\[
a\omega|\phi_+\rangle
+
b\omega^{-1}|\phi_-\rangle.
\]

The route has become entangled with the channel label. Discarding that label
dephases the route unless one amplitude vanishes.

For the equal incoherent mixture, the off-diagonal route coherence is
multiplied by

\[
\frac{\omega+\omega^{-1}}2=-\frac12.
\]

The same real scalar that appears in the central Wilson shadow is therefore
the signature of a missing channel-resolution constructor.

## Braid orientation, channel label, and bridge orientation

There are three distinct binary choices:

1. clockwise versus counterclockwise full monodromy;
2. total fusion channel `D_{k+1}` versus `D_{k-1}`;
3. bridge holonomy `H` versus `H*`.

Changing either of the first two conjugates the route coefficient. If the
bridge holonomy is not also conjugated, the sixth-root branch becomes the
rank-deficient filter derived in the relative-framing packet. If all three
are conjugated coherently, the constructor remains ideal and implements
`Q_A*`.

This cleanly separates a detectable phase-channel mismatch from a common-mode
orientation-frame reversal.

## Physical command decomposition

The braid-based implementation requires the following constructors:

1. create a globally neutral dyon pair and split one member into the typed
   `D_k,C` channel;
2. verify or preserve the multiplicity-one `D_{k+1}` fusion channel;
3. transport one anyon around the other and return both to their original
   sites;
4. re-fuse and annihilate the ancillary packet back to vacuum;
5. make that closed loop conditional on the same coherent route coordinate that
   selects `S` rather than `R`;
6. erase no history by tracing; instead return every position, fusion, and
   apparatus port before real route recombination.

Items one through four belong to the standard create--braid--fuse language.
Item five remains the new coupled constructor. A classically commanded braid
does not automatically provide a coherent superposition of braided and
unbraided histories.

## Source-level correction to the prior framing proposal

The topological twist remains a correct coefficient calculation, and
relative ribbon framing remains a valid abstract incidence model. But neither
must be assumed as a primitive physical actuator.

The resolved-monodromy construction realizes the same cube-root coefficient
using the operation class explicitly foregrounded in topological quantum
computation: moving anyons around one another. This is therefore the preferred
microscopic target.

The source boundary remains real. Cowtan and Majid explicitly note, in their
`D(S3)` computational appendix, that the deterministic non-Abelian transport
operators they use are claimed in earlier work and are beyond their scope to
construct. Marici must still supply or type that transport rather than citing
the existence of ribbon operators as proof of an executable motion primitive.

## Minimal hostiles

### Unresolved total charge

Prepare both fusion channels and discard the label. The full braid attenuates
route coherence instead of supplying a unit phase.

### Wrong resolved channel

Prepare `D_{k-1}` while the compiler declares `D_{k+1}`. The phase is
conjugated and the fixed bridge gadget becomes a rank-deficient filter.

### Spectator braid

Braid the resolved pair in an apparatus whose history is not correlated with
the `R/S` bridge route. The phase is exact but the qutrit channel is unchanged.

### Classical braid control

Record whether the braid occurred in a classical controller or environment.
The bridge receives a mixture rather than a coherent route coefficient.

### Transport residue

Return the anyon positions but leave different local ribbon, clock, or bath
states after the braided and unbraided histories. The coefficient is reduced
by their overlap and the branch has Choi rank greater than one.

## Exact falsifiers

- `C` restricted to `C3` is treated as a single character.
- The fusion `D_k` times `C` omits either neighboring dyon channel.
- The monodromy phase is assigned without conditioning on the fusion channel.
- The same phase is assigned to both multiplicity-one channels.
- Full braid orientation is reversed without conjugating the phase.
- A known total charge is inferred from an unresolved central readout.
- A scalar braid on a spectator ancilla is promoted to a qutrit gate.
- Deterministic braid control is inferred from an abstract braid-group
  representation.
- Returning anyon positions is treated as proof of full environment return.
- The categorical balancing equation is promoted to a lattice transport
  theorem.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies resolved route alternatives, incidence,
closed transport histories, endpoint return, channel labels, classical versus
coherent control, and the distinction between a mathematical braid and an
executable transport constructor.

The quantum coefficient lens supplies centralizer restriction, dyon fusion,
the balancing equation, topological twists, monodromy eigenvalues,
multiplicity-one channel rigidity, and Kraus decoherence after channel erasure.

## Disposition

The cube-root phase no longer requires a physical self-twist primitive. A
resolved full monodromy between a three-cycle dyon and the standard electric
charge supplies `omega` exactly. The minimal choice is `D_0` times `C` in the
total `D_1` channel; selecting `D_2` or reversing the braid supplies the
conjugate.

This moves the physical frontier into the standard anyon command set while
leaving one precise gap: construct a coherent conditional monodromy on the
same route bit that carries the charged qutrit bridge, with deterministic
non-Abelian transport and complete environment return.

No build, checker, or Git operation was run for this research-only packet.
