# Nonabelian Frame Transport Is Classified by Ordered Holonomy

Let (P) be a connected parameter graph and (G) a possibly nonabelian frame
group. Assign an authorized transport element

\[
g_e\in G
\]

to every oriented edge (e:p\to q), acting on the left.

A local frame change (k_p\in G) transforms the edge transport by

\[
g_e\longmapsto g'_e=k_qg_ek_p^{-1}.
\]

For a based loop

\[
\gamma=e_m\cdots e_1
\]

starting and ending at (p), the ordered holonomy is

\[
H_\gamma=g_{e_m}\cdots g_{e_1}.
\]

Under local frame changes,

\[
H_\gamma\longmapsto k_pH_\gamma k_p^{-1}.
\]

Thus the unbased invariant is a conjugacy class, while a based endpoint frame
retains the actual group element.

## Global trivialization theorem

There are local frames making every edge transport the identity exactly when
every loop holonomy is the identity. On a spanning tree, frames can always be
propagated to trivialize the tree edges. Each remaining chord records one
ordered fundamental-loop holonomy. These chord transports can all be removed
if and only if those holonomies are trivial.

Gauge classes of graph transports are described by the nonabelian pointed set

\[
H^1(P;G)
\simeq
\operatorname{Hom}(\pi_1(P),G)/G,
\]

where (G) acts by simultaneous conjugation. This is not generally a group.
The additive cycle-sum theorem is recovered only when (G) is abelian.

## Exact (S_3) triangle

Orient a parameter triangle as

\[
0\to1\to2\to0.
\]

Take

\[
g_{01}=(12),
\qquad
g_{12}=(23),
\qquad
g_{20}=1.
\]

The ordered holonomy

\[
H=g_{20}g_{12}g_{01}
\]

is a three-cycle. No vertex-frame choices can trivialize all three edges.

By contrast,

\[
g_{01}=(12),
\qquad
g_{12}=(12),
\qquad
g_{20}=1
\]

has identity holonomy and is globally trivializable. There are six
trivializing frame choices, differing by one global (S_3) frame.

The order matters: exchanging two noncommuting edge transports can invert or
change the three-cycle holonomy. An abelian cycle sum would erase this
constructor data.

## Central versus based readout

A conjugacy-class or character readout sees only central flux information. It
can distinguish identity, transposition, and three-cycle sectors in (S_3),
but it does not recover a based endpoint element or the full block algebra.

This matches the established (D(S_3)) hierarchy:

\[
\text{central readout}
\subset
\text{endpoint block algebra}
\subset
\text{ambient operators}.
\]

The present transport theorem explains the first loss: quotienting the base
frame retains holonomy only up to conjugacy. Recovering endpoint orientation
requires a based frame or further noncentral ports.

The earlier result that one transposition-resolved and one three-cycle-resolved
port generate the finite endpoint algebra is an algebraic implementation
template. It does not imply that an arbitrary parameter transport exposes
those ports physically.

## Completion gate

For cutoff-dependent nonabelian transports, exact identity holonomy at every
finite stage does not by itself give a completion-stable frame. The
trivializing vertex gauges must lie in one authorized topology and remain
uniformly controlled. Conversely, a stable nonidentity holonomy can encode an
intended logical gate rather than a defect.

## Falsifiers

- Replacing an ordered nonabelian loop product by an unordered sum.
- Calling conjugate holonomies equal as based endpoint data.
- Declaring a transport trivial because its holonomy is central but nonidentity.
- Treating nonabelian (H^1) as an abelian group.
- Inferring full endpoint algebra from conjugacy-class flux readout.
- Importing (S_3) transports into Fourier--Tate or theta sectors without a
  source coefficient group.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to extend frame-gluing from torsor bits to the established
nonabelian endpoint sector.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Ordered holonomy and simultaneous conjugacy are the exact nonabelian
replacement for additive displacement cocycles.
