# Multiple-zero observability requires the first nonzero jet

## Bounded question

For the rank-two endpoint/source state observed by Clark-type rows, what jet
order is minimally required at a transmission zero of multiplicity \(m\)?

## Frozen multiplicity convention

Let \(F\) be holomorphic near \(s_0\), with a zero of exact multiplicity
\(m\ge1\):

\[
F^{(k)}(s_0)=0\quad(0\le k<m),
\qquad
F^{(m)}(s_0)\ne0.
\]

Use the normalized jet

\[
\tau_k(F;s_0)=\frac{F^{(k)}(s_0)}{k!}.
\]

This packet addresses a two-coordinate state: endpoint displacement plus one
source direction. It does not reconstruct a full length-\(m\) generalized
zero-dynamics chain.

## Minimal jet-order theorem

Any row whose source coefficient is a linear combination of
\(\tau_0,\ldots,\tau_r\) with \(r<m\) reduces at \(s_0\) to an endpoint-only
row. Arbitrarily many such rows remain blind to the source direction.

At order \(m\), choose a nonzero authorized coefficient \(\gamma_m\) and the
sheet-paired rows

\[
R_+=(1,\gamma_m\tau_m),
\qquad
R_-=(1,-\gamma_m\tau_m).
\]

Their row determinant is

\[
-2\gamma_m\tau_m,
\]

so they are jointly faithful exactly when
\(\gamma_m\tau_m\ne0\). Thus the first nonzero jet order \(m\) is necessary
and sufficient for this rank-two incidence problem.

For a simple zero, \(m=1\), \(\gamma_1=ia\), and the theorem recovers
Grothendieck's Clark rows

\[
(1,F+iaF'),\qquad(1,F-iaF')
\]

at \(F=0\).

## Gramian and conditioning

Writing \(z=\gamma_m\tau_m\), the symmetric pair has Gramian

\[
G_m=
\begin{pmatrix}
1&z\\
1&-z
\end{pmatrix}^{\!*}
\begin{pmatrix}
1&z\\
1&-z
\end{pmatrix}
=
\begin{pmatrix}
2&0\\
0&2|z|^2
\end{pmatrix}.
\]

Hence

\[
\det G_m=4|z|^2.
\]

Finite faithfulness requires only \(z\ne0\). Completion-stable faithfulness
requires a cutoff-independent lower bound on \(|z|\). The family \(z_N=1/N\)
is faithful at every cutoff while its source-direction energy
\(2/N^2\) collapses.

## No fixed finite jet tower handles unbounded multiplicity

Fix a maximum authorized jet order \(r\). The family

\[
F_N(s)=s^N,
\qquad N>r,
\]

has all jets through order \(r\) equal to zero at the origin. Every row built
from that fixed tower is endpoint-only there. Repairing each cutoff by adding
the \(N\)-th jet uses a cutoff-dependent constructor family and therefore does
not define one finite pro-completion interface.

Consequently a fixed finite jet compiler can cover a family only after one
proves a uniform upper bound on zero multiplicity, or supplies a different
source constructor that does not truncate by derivative order.

## Sheet torsor and orientation

The sheet involution exchanges \(R_+\) and \(R_-\), equivalently \(z\mapsto-z\).
The Gramian is invariant and depends only on \(|z|^2\). Therefore the paired
jet port observes the two-coordinate state but does not orient the sheet or the
zero locus. A trusted sheet label or other source reference is additional data.

## Source-authority boundary

The theorem determines which derivative order and row rank would suffice once
the jet port is authorized. It does not derive \(\gamma_m\), prove that higher
theta jets are boundary currents, or authorize an unbounded jet tower.
Grothendieck must derive the actual higher-jet incidence and its cutoff
naturality from the source operator.

## Exact audit and falsifiers

The checker evaluates \(F(s)=s^m\) for \(1\le m\le6\), verifies that every
lower jet pair has rank one and the first nonzero pair rank two, checks the
exact Gramian and sheet swap, and requires the fixed-tower and collapsing-jet
hostiles.

The finite theorem is falsified by a lower-order row that sees the source
direction at an exact multiplicity-\(m\) zero. Uniform completion is falsified
by \(|\gamma_m\tau_m|\to0\), unbounded multiplicity, or a required jet order
that grows with cutoff.

## Claim boundary

This is a finite rank-two jet-incidence theorem. It does not reconstruct the
full generalized zero chain, derive theta higher-jet ports, bound Riemann-zero
multiplicity, orient zeros, prove completion stability, or prove RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
9/10. The alternatives were sufficiency of lower jets and necessity of the
first nonzero jet. Ranks, Gramian, sheet swap, unbounded-multiplicity hostile,
and conditioning collapse were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Lower jets were eliminated exactly; order \(m\) and two rows were proved
minimal for the rank-two state; fixed finite towers were shown incapable of
covering unbounded multiplicity; and observability remained explicitly
non-orienting. Higher-jet source authority is unresolved.
