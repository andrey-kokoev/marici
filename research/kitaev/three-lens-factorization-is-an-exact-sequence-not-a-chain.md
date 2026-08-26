# Three-lens factorization is an exact sequence, not a chain

## Bounded question

How do ordered noncommutative holonomy, determinant-line phase, and additive
phase current actually factor on one finite carrier graph?

The answer corrects a tempting hierarchy. Ordered holonomy descends to a
determinant phase. An additive phase current is not generally a further
quotient: it is a lift of that phase through the universal cover, and winding
is the obstruction.

## Frozen packet

Let \(P\) be a connected finite graph with oriented edge transports

\[
U_e\in U(n),
\qquad
U_{\bar e}=U_e^{-1}.
\]

For an ordered based path

\[
\gamma=e_m\cdots e_1,
\]

define

\[
H_\gamma=U_{e_m}\cdots U_{e_1}\in U(n).
\]

A vertex-frame change \(K_v\in U(n)\) acts by

\[
U_e\longmapsto K_{t(e)}U_eK_{s(e)}^{-1}.
\]

For a loop based at \(v\), \(H_\gamma\) changes by conjugation with \(K_v\).
Thus an unframed ordered readout is the conjugacy class of \(H_\gamma\); a
based endpoint frame retains the actual matrix.

## The two exact sequences

The coefficient lenses are governed by

\[
1\longrightarrow SU(n)
\longrightarrow U(n)
\xrightarrow{\det}U(1)
\longrightarrow1
\]

and

\[
0\longrightarrow2\pi\mathbf Z
\longrightarrow\mathbf R
\xrightarrow{\exp(i\cdot)}U(1)
\longrightarrow1.
\]

The first arrow sequence is a quotient:

\[
H_\gamma\longmapsto \det H_\gamma.
\]

It forgets the special-unitary part of the ordered transport.

The second sequence runs in the opposite reconstruction direction. An additive
phase \(a_\gamma\in\mathbf R\) must satisfy

\[
e^{ia_\gamma}=\det H_\gamma.
\]

It is a choice of lift, unique only modulo \(2\pi\mathbf Z\) on one isolated
loop. A compatible lift over a parameter family can fail to exist globally.

Therefore the correct architecture is

\[
U(n)\xrightarrow{\det}U(1)\xleftarrow{\exp(i\cdot)}\mathbf R,
\]

not a monotone chain

\[
U(n)\longrightarrow U(1)\longrightarrow\mathbf R.
\]

## Information losses and obstructions

### Ordered to determinant

The exact kernel is \(SU(n)\). Two holonomies can have identical determinant
phase while differing by a noncentral special-unitary component.

### Additive to determinant

Exponentiation has kernel \(2\pi\mathbf Z\). Distinct additive currents can
produce the same phase.

### Determinant to additive

This direction is a lifting problem. Along a closed parameter loop, a phase map

\[
u:S^1\longrightarrow U(1)
\]

admits a single-valued continuous real lift on \(S^1\) exactly when its winding
number is zero.

Thus the additive lens requires both a branch frame and vanishing winding on
the domain where a global scalar current is claimed.

## Smallest determinant-kernel witness

In \(U(2)\), let

\[
H_0=I,
\qquad
H_\theta=
\begin{pmatrix}
e^{i\theta}&0\\
0&e^{-i\theta}
\end{pmatrix}.
\]

Then

\[
\det H_0=\det H_\theta=1,
\]

but \(H_\theta\neq H_0\) for generic \(\theta\), and the two matrices are not
conjugate because their spectra differ. A determinant-phase readout cannot
reconstruct the ordered holonomy class.

A minimal separating context is any authorized noncentral character, matrix
element in a based frame, or endpoint port whose value differs on these two
classes. Which one is admissible belongs to source authority.

## Smallest winding witness

Let

\[
u(t)=e^{it},
\qquad
0\le t\le2\pi,
\]

with the endpoints identified. The phase is a continuous loop in \(U(1)\). Its
lift on the interval is \(a(t)=t\), but

\[
a(2\pi)-a(0)=2\pi.
\]

Hence no single-valued continuous real lift exists on the parameter circle.
The additive current is locally defined but has monodromy one.

Cutting the circle at a chosen point produces a lift, but the cut is additional
frame data. It is not recovered from the phase loop itself.

## Graph form

Taking determinants edgewise gives

\[
d_e=\det U_e\in U(1).
\]

An additive edge potential \(a_e\in\mathbf R\) satisfies

\[
e^{ia_e}=d_e.
\]

On a spanning tree, branches can always be chosen recursively after fixing one
root frame. Each chord then carries an integer cycle residual

\[
k_C=rac{1}{2\pi}
\left(
\sum_{e\in C}\epsilon_e a_e-\arg\prod_{e\in C}d_e
\right)
\in\mathbf Z.
\]

Changing edge branches changes representatives but preserves the integral
cycle class. A globally compatible additive phase convention exists exactly
when the relevant winding class vanishes.

This is the additive analogue of the ordered-holonomy obstruction, but its
coefficient group is the deck group \(2\pi\mathbf Z\), not the original
nonabelian transport group.

## Relation to the obstruction tower

The finite packet realizes three distinct gates.

1. The determinant map has global multiplicity: its fibres contain
   special-unitary holonomies.
2. The exponential map has discrete multiplicity: additive lifts differ by
   \(2\pi\mathbf Z\).
3. A determinant-phase family can have monodromy: nonzero winding prevents a
   global additive lift.

Completion adds a fourth issue. Even when winding vanishes at every cutoff, a
chosen sequence of additive lifts may escape by multiples of \(2\pi\) unless a
common branch convention or uniform bound is retained.

## Shared Carrier geometry versus coefficient lens

Shared Carrier geometry supplies:

- paths, loops, spanning trees, chords, and cycle incidence;
- the distinction between local trivializations and global loop obstruction;
- support change and completion questions.

The quantum or matrix coefficient lens supplies:

- the group \(U(n)\);
- ordered multiplication;
- conjugation gauge;
- the determinant homomorphism and its \(SU(n)\) kernel.

The phase coefficient lens supplies \(U(1)\). The additive lift supplies the
covering group \(\mathbf R\) and deck lattice \(2\pi\mathbf Z\).

Carrier geometry alone does not choose any of these coefficient groups.

## Consequence for scalar diagnostics

A scalar additive record can be related to an ordered plant only after two
independent proof obligations:

1. the plant's special-unitary or noncommutative kernel is irrelevant, gauged,
   or observed by additional ports;
2. the determinant phase admits the claimed globally compatible additive lift.

Failure of the first is lost operator content. Failure of the second is phase
monodromy. They cannot be repaired by the same reference.

A based noncentral port can separate the determinant kernel but does not choose
a logarithm branch. A branch reference can choose an additive origin but does
not reconstruct the \(SU(n)\) component.

## Exact falsifiers

- Two nonconjugate \(U(n)\) holonomies with equal determinant disprove ordered
  reconstruction from determinant phase.
- A phase loop with nonzero winding disproves a global additive lift.
- Two additive lifts differing by \(2\pi k\) disprove uniqueness without a
  branch frame.
- A cutoff family whose chosen lift integers diverge disproves
  completion-stable additive reconstruction.
- A claimed universal chain from ordered to phase to additive, without a lift
  datum, is mistyped.

## Claim boundary

This is an exact finite coefficient theorem for authorized \(U(n)\) graph
transport. It does not assert that a theta/Tate, optical, gravitational, or
other sector carries \(U(n)\) transport. Such a sector must derive its own
coefficient group, determinant channel, and lift authority.

## Process calibration

Pre-objective: excitement 9.5/10, confidence 8/10, expected information gain
8.5/10. The frozen target was an exact fibre/kernel classification and one
minimal separating-context theorem. The main confound was mistaking a finite
coefficient template for sector-native physics.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
9.5/10. The optionality space changed materially: the proposed three-lens chain
was eliminated and replaced by a span of two exact sequences; determinant
kernel and logarithmic monodromy are now separate obstructions requiring
different references. No sector-native coefficient authority was added.
