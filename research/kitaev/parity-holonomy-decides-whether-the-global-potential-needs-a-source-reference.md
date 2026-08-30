# Parity Holonomy Decides Whether the Global Potential Needs a Source Reference

Suppose the twisted gain data admit at least one global potential

\[
\ell_e
=\phi_{t(e)}-\varepsilon_e\phi_{s(e)}.
\]

Existence does not automatically give uniqueness. Let \(\phi\) and
\(\widetilde\phi\) be two solutions and define

\[
d_v=\widetilde\phi_v-\phi_v.
\]

Subtracting the edge equations gives the homogeneous sign transport

\[
d_{t(e)}=\varepsilon_e d_{s(e)}.
\]

Thus the ambiguity is the space of global sections of the parity local
system.

## Even parity holonomy

Assume every loop has parity \(+1\). Choose a root value \(d_{v_0}=c\). Sign
transport determines every other value uniquely:

\[
d_v=\sigma_vc,
\]

where \(\sigma_v\) is the parity along any path from the root to \(v\). The
all-even loop condition makes \(\sigma_v\) path-independent.

Therefore the potential space is a one-dimensional affine torsor. A source
reference is needed to fix \(c\). Depending on the realization, that reference
could be the tensor unit, vacuum normalization, determinant value, or another
distinguished source object.

The ambiguity need not be an ordinary constant. If some edges exchange the
rays but all loops are even, it is a signed constant \(\sigma_vc\).

## Odd parity holonomy

If a loop \(C\) has parity \(-1\), homogeneous transport around it gives

\[
d_{v_0}=-d_{v_0}.
\]

Over the real numbers,

\[
d_{v_0}=0.
\]

Connectedness then forces \(d_v=0\) at every vertex. Hence an existing global
potential is unique.

The odd loop fixes its center and removes the additive frame ambiguity. This
does not restore an ordered global polarization: the same odd loop exchanges
the repair and drift rays. Uniqueness of the twisted potential and existence
of an ordered frame are distinct properties.

## Cohomological statement

The solution set, when nonempty, is an affine torsor over

\[
H^0(G;\mathbb R_\varepsilon).
\]

For a connected graph,

\[
\dim H^0(G;\mathbb R_\varepsilon)
=
\begin{cases}
1,&\text{all loop parities are even},\\
0,&\text{some loop parity is odd}.
\end{cases}
\]

This is the exact reference-count theorem.

## Exact triangle fixtures

Take tree-edge parities

\[
\varepsilon_{01}=+1,
\qquad
\varepsilon_{12}=-1.
\]

For an even closing edge \(2\to0\) with parity \(-1\), the homogeneous
solutions are

\[
(d_0,d_1,d_2)=(c,c,-c).
\]

One reference scalar remains.

For an odd closing edge with parity \(+1\), the equations force

\[
d_0=d_1=d_2=0.
\]

The potential is unique.

## Orientation-double-cover boundary

Passing to the orientation double cover removes odd loop parity and restores an
ordered polarization. It also restores a one-dimensional normalization
ambiguity on each connected lifted component, subject to deck compatibility.
Thus the cover trades canonical twisted centering for an ordered frame plus a
reference choice.

## Source-authority boundary

The compiler counts the references but cannot choose one. If the actual
Fourier--Tate graph has only even parity holonomy, Grothendieck must identify
the source object fixing the remaining scalar. If it has an odd loop, the
potential value is forced by the loop center, but the interpretation remains
twisted.

## Falsifiers

- Claiming uniqueness in an all-even connected graph without a reference.
- Treating signed-constant ambiguity as an ordinary constant across exchange
  edges.
- Claiming an odd loop permits a global ordered polarization.
- Introducing a vacuum reference when odd holonomy already fixes the twisted
  potential, without explaining its separate role.
- Passing to the orientation double cover while retaining the uniqueness claim
  from the base.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to determine exactly when Deutsch's global potential is a
canonical explanation and when it still needs an external source origin.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Parity holonomy alone counts the ambiguity: one signed scalar in the
even case, none in the odd twisted case.
