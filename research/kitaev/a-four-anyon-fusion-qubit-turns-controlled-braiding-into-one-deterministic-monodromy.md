# A four-anyon fusion qubit turns controlled braiding into one deterministic monodromy

Owner: `marici.Kitaev`

## Bounded question

Can the remaining coherent choice between “braid” and “do not braid” be
removed from the cube-root phase constructor?

Yes algebraically. Encode the route coordinate in two fusion channels on
which one unconditional full braid has different eigenvalues. The minimal
vacuum-neutral workspace with fixed external anyon types is

\[
D_0,\ C,\ C,\ D_0.
\]

Its total-vacuum fusion space is two-dimensional. A full monodromy of the
first `D_0,C` pair acts as `diag(omega,omega squared)`. Projectively this is
`diag(1,omega)`, exactly the relative route phase required before real
recombination.

Thus no laboratory controller need coherently decide whether a braid occurs:
perform the same deterministic braid in every run. The quantum state itself,
through its fusion channel, controls the phase.

The required unbiased fusion-qubit measurement is also intrinsic: fuse the two
middle electric `C` charges and distinguish total charge `A` from `B`. In the
two vacuum-compatible channels this recoupling is exactly the real Hadamard
matrix. The remaining physical gate is the bridge-to-fusion-channel encoding
isometry.

## Claim boundary

The fusion-space dimension, monodromy matrix, route-isometry calculation, and
minimality statement below are exact in the untwisted `D(S3)` ribbon category.

The packet does not derive the required encoding isometry from lattice ribbon
operators or construct the nondestructive middle-pair charge measurement on a
specific lattice. It derives the relevant recoupling row in the frozen group
representation convention and identifies the encoding isometry as the first
remaining exact typing gate.

## Four fixed anyons and two vacuum channels

Use the fusion rule

\[
D_0\otimes C\cong D_1\oplus D_2.
\]

The second pair obeys the same rule. Since

\[
D_1^*=D_2,
\qquad
D_2^*=D_1,
\]

there are exactly two pairwise fusion paths to the vacuum:

\[
(D_0C\to D_1)(CD_0\to D_2)\to A,
\]

and

\[
(D_0C\to D_2)(CD_0\to D_1)\to A.
\]

All displayed fusion multiplicities are one. Define the orthonormal fusion
basis

\[
|0_F\rangle
=
|(D_1,D_2)\to A\rangle,
\]

\[
|1_F\rangle
=
|(D_2,D_1)\to A\rangle.
\]

Therefore

\[
\dim\operatorname{Hom}
\left(
A,D_0\otimes C\otimes C\otimes D_0
\right)
=2.
\]

Both logical fusion states have the same fixed external anyon types and the
same total vacuum charge. Their coherent superposition violates no total-
charge superselection rule.

## Minimality inside this phase-port family

Two fixed anyons with total vacuum have one dual-pair fusion channel. They do
not carry both `D_1` and `D_2` intermediate alternatives.

With three fixed simple anyons, a chosen third object can compensate either
intermediate channel `D_1` or `D_2`, because vacuum fusion requires its charge
to be the dual of that channel. No one simple third object is dual to both.

Four fixed anyons are therefore minimal for retaining both monodromy
eigenchannels coherently while keeping total charge vacuum in this
`D_0,C` construction.

The second `C,D_0` pair supplies the conjugate channel required by each branch.

## Deterministic monodromy gate

Apply one oriented full monodromy to the first `D_0,C` pair in every run. By
the balancing equation, its action in the fusion basis is

\[
B_F
=
\begin{pmatrix}
\omega&0\\
0&\omega^2
\end{pmatrix}.
\]

Removing the common scalar `omega` gives

\[
B_F\sim
\begin{pmatrix}
1&0\\
0&\omega
\end{pmatrix}.
\]

The required relative cube-root phase is therefore a deterministic logical
gate on the fusion qubit.

No superposition of braid commands appears. The braid word is fixed; its
action depends coherently on the pre-existing fusion channel.

## Bridge-incidence isometry

Let `R,S` be the two full-rank charged qutrit routes with common typed
endpoints. The target route-encoding isometry is

\[
J|\psi\rangle
=
\frac1{\sqrt2}
\left(
R|\psi\rangle\otimes|0_F\rangle
+
S|\psi\rangle\otimes|1_F\rangle
\right).
\]

Because `R,S` are unitary and the two fusion channels are orthogonal,

\[
J^*J
=
\frac12(R^*R+S^*S)
=I.
\]

Thus `J` is a valid isometry on the unknown qutrit. It is the precise
incidence constructor connecting the charged bridge to the orientation fusion
qubit.

After deterministic monodromy,

\[
(I\otimes B_F)J|\psi\rangle
\sim
\frac1{\sqrt2}
\left(
R|\psi\rangle\otimes|0_F\rangle
+
\omega S|\psi\rangle\otimes|1_F\rangle
\right).
\]

## Required fusion-qubit recombination

Define the unbiased fusion states

\[
|X+\rangle
=
\frac{|0_F\rangle+|1_F\rangle}{\sqrt2},
\]

\[
|X-\rangle
=
\frac{|0_F\rangle-|1_F\rangle}{\sqrt2}.
\]

Measuring in this basis gives qutrit branch operators

\[
K_{X+}=\frac{R+\omega S}{2},
\qquad
K_{X-}=\frac{R-\omega S}{2}.
\]

Hence the four-anyon fusion qubit plus one deterministic braid reproduces the
complete ideal phase-halving instrument.

For the vacuum-projector cube-root holonomy, `X-` is the `3/4` sixth-root
success branch and `X+` is the `1/4` correctable failure.

## The relevant recoupling row is exactly Hadamard

Use an eigenbasis for the standard electric representation in which

\[
\rho_C(r)|+\rangle=\omega|+\rangle,
\qquad
\rho_C(r)|-\rangle=\omega^2|-\rangle,
\]

and the transposition exchanges `+` and `-`.

Let `|r>` and `|r inverse>` denote the two flux basis vectors of `D_0`.
Degree zero and invariance under the group action give the following explicit
normalized vacuum vectors:

\[
|0_F\rangle
=
\frac1{\sqrt2}
\left(
|r\rangle|+\!-\rangle|r^{-1}\rangle
+
|r^{-1}\rangle|-\!+\rangle|r\rangle
\right),
\]

\[
|1_F\rangle
=
\frac1{\sqrt2}
\left(
|r\rangle|-\!+\rangle|r^{-1}\rangle
+
|r^{-1}\rangle|+\!-\rangle|r\rangle
\right).
\]

The first vector has first-pair charge `D_1`; the second has first-pair
charge `D_2`. The outer flux pair is an essential relational reference and
must not be silently contracted away.

Now fuse the two middle electric charges. The standard representation obeys

\[
C\otimes C\cong A\oplus B\oplus C.
\]

Within the middle cross-character subspace, the normalized `A` and `B` charge
states are

\[
|A\rangle
=
\frac{|+\!-\rangle+|-\!+\rangle}{\sqrt2},
\]

and

\[
|B\rangle
=
\frac{|+\!-\rangle-|-\!+\rangle}{\sqrt2}.
\]

The first is invariant under the transposition; the second acquires its sign.
Both are invariant under the three-cycle because the two eigencharacters
multiply to one. They are therefore exactly the trivial and sign electric
charges.

The outer `D_0,D_0` pair likewise has normalized `A` and `B` channels

\[
|A_{out}\rangle
=
\frac{|r,r^{-1}\rangle+|r^{-1},r\rangle}{\sqrt2},
\]

\[
|B_{out}\rangle
=
\frac{|r,r^{-1}\rangle-|r^{-1},r\rangle}{\sqrt2}.
\]

Define the two vacuum-compatible recoupled states

\[
|A_F\rangle=|A_{out}\rangle|A\rangle,
\qquad
|B_F\rangle=|B_{out}\rangle|B\rangle.
\]

Direct expansion gives

\[
|0_F\rangle
=
\frac{|A_F\rangle+|B_F\rangle}{\sqrt2},
\]

\[
|1_F\rangle
=
\frac{|A_F\rangle-|B_F\rangle}{\sqrt2}.
\]

The `C` summand is carried by the same-character states and is absent from the
total-vacuum four-anyon sector because the outer `D_0,D_0` pair contains only
`A`, `B`, and `D_0`, not the electric `C` channel. Hence the recoupling matrix
from the `0_F,1_F` basis to the matched `A_F,B_F` channels is, up to
fusion-vertex phase conventions,

\[
F_{rec}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The row magnitudes are gauge-invariant and equal. Vertex gauge phases merely
rename the calibrated route phases; in the displayed real convention, `A`
is `X+` and `B` is `X-`.

Thus ordinary middle-pair charge measurement supplies the exact unbiased
fusion-qubit recombination required by the LCU instrument. No uncomputed
`F`-symbol remains in this two-dimensional sector.

## General biased-measurement falsifier

Suppose one available measurement row is

\[
\langle m|
=
\overline a\langle0_F|
+
\overline b\langle1_F|,
\qquad
|a|^2+|b|^2=1.
\]

After monodromy, its qutrit branch is

\[
K_m
=
\frac1{\sqrt2}
\left(
\overline a R
+
\overline b\omega S
\right).
\]

If `|a|` differs from `|b|`, no phase calibration converts this into the
required equal-weight LCU branch. It generally becomes an input-dependent
filter. A correct scalar braid phase cannot repair a biased recombination
row.

## What happened to coherent braid control

The prior implementation required the map

\[
|0\rangle\longmapsto I,
\qquad
|1\rangle\longmapsto Braid.
\]

The fusion-qubit implementation instead performs `Braid` unconditionally and
uses its spectral decomposition

\[
Braid
=
\omega|0_F\rangle\langle0_F|
+
\omega^2|1_F\rangle\langle1_F|.
\]

Control has moved from the classical command history into a protected quantum
number. This is precisely the desirable topological conversion: one fixed
worldline operation acts conditionally because the carrier already stores the
distinction in its fusion channel.

The price is explicit. One must construct `J` and perform the middle-pair
`A/B` charge measurement without measuring or leaking the first-pair fusion
channel prematurely.

## Relationship to the B-sector bridge

The fusion qubit supplies phase control; it does not manufacture the charged
routes `R,S`. If those routes require the invertible `B`-charge reference to
connect the two native qutrit sectors, that reference remains part of `J`.

The new four-anyon packet may replace a separate path-control qubit, but it
does not replace sector connectivity. The complete source workspace contains:

- the encoded qutrit;
- the relational `B` bridge reference;
- the four-anyon orientation fusion qubit;
- the common total-charge compensators and measurement record.

The map `J` must correlate these systems while preserving one global charge
sector.

## Minimal hostiles

### Classical channel preparation

Prepare `0_F` or `1_F` according to a classical coin rather than coherently
encoding the two bridge routes. The deterministic braid produces a mixture,
not an LCU gate.

### Early channel measurement

Measure the first-pair total charge before recombination. The route record is
broadcast and interference is destroyed.

### Wrong pair-charge measurement

Measure a pairing or coarse charge projector that does not resolve the middle
`C,C` charges as `A` versus `B`. The required Hadamard recombination is absent
and the branch need not be reversible.

### Wrong channel--route correlation

Swap which fusion channel carries `R` while leaving the compiler convention
unchanged. The phase is conjugated relative to the bridge holonomy and the
nominal success branch loses rank.

### Spectator fusion qubit

Prepare and braid the four anyons without the incidence isometry `J`. The
fusion gate is exact but the qutrit is untouched.

## Exact falsifiers

- The four-anyon total-vacuum fusion space is assigned dimension other than
  two under the frozen fusion rules.
- The two basis paths do not pair conjugate intermediate charges.
- Deterministic first-pair monodromy is assigned the same eigenvalue on both
  channels.
- A common scalar is mistaken for the relative `omega` phase.
- The map `J` is called physical merely because it is an abstract isometry.
- An arbitrary fusion measurement is called an `X` measurement without the
  displayed middle-pair charge derivation.
- The same-character `C` summand is included in the total-vacuum logical
  subspace.
- A biased row is repaired using phase calibration alone.
- The orientation fusion qubit is claimed to replace the `B` connectivity
  reference.
- A fusion-channel record is discarded before route recombination.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies internalized control, fixed commands acting
on state sectors, route encoding, recombination, record formation, incidence,
and the separation of connectivity from orientation.

The quantum coefficient lens supplies fusion spaces, dual charges,
monodromy eigenspaces, balancing phases, `F`-symbol recoupling, isometries, and
Kraus filtering under biased measurement.

## Disposition

The coherent “braid or do not braid” command is unnecessary. Four fixed anyons
`D_0,C,C,D_0` in total vacuum contain a protected two-dimensional fusion space.
One deterministic full monodromy is projectively `diag(1,omega)` on that
space, so the fusion channel itself controls the cube-root phase.

The recoupling problem is closed algebraically: measuring the middle `C,C`
pair as `A` versus `B` is exactly the required real Hadamard measurement.

The physical frontier is now one finite constructor: the bridge-incidence
isometry `J` correlating `R,S` with the two fusion channels while preserving
global charge and returning the `B` reference. A lattice implementation of
the middle-pair charge measurement remains an actuator obligation, but its
target projector and coefficients are no longer ambiguous.

No build, checker, or Git operation was run for this research-only packet.
