# Parity must come from ordered source incidence

## Formal grading is not source authority

Any operator

\[
D:V\longrightarrow W
\]

can be embedded formally into a graded differential on `V` direct sum `W`.
Declaring `V` even and `W` odd gives

\[
d=
\begin{pmatrix}
0&0\\
D&0
\end{pmatrix},
\qquad
d^2=0.
\]

This construction is algebraically canonical once the ordered arrow `V to W`
is fixed. But the opposite order produces the shifted dual complex. Scalar
norms do not distinguish them.

Therefore the super-grading required by the Cartan mechanism must be generated
by a source-authorized incidence direction, not assigned after observing the
desired anticommutator sign.

## Exact rectangular witness

Let

\[
D:\mathbb Q^2\longrightarrow\mathbb Q,
\qquad
D=(1\;0).
\]

As an even-to-odd differential, it has

\[
\dim H^{\mathrm{even}}=1,
\qquad
\dim H^{\mathrm{odd}}=0,
\]

and graded index `+1`.

Reverse the incidence and use

\[
D^T:\mathbb Q\longrightarrow\mathbb Q^2.
\]

The nonzero singular value and every quadratic energy are unchanged. But now

\[
\dim H^{\mathrm{even}}=0,
\qquad
\dim H^{\mathrm{odd}}=1,
\]

and the graded index is `-1`.

The same ungraded relation therefore carries opposite higher obstruction under
the two ordered source typings.

## Determinant-line consequence

Reversing a two-term complex dualizes its determinant line. A torsion or
determinant section is correspondingly inverted, and its phase and index signs
reverse. This is not visible in the positive forms `D^*D` and `DD^*`, whose
nonzero spectra agree.

Thus the determinant bridge cannot be constructed from a Gram matrix alone.
It needs the ordered complex.

## Source interpretation

For the theta-tail system, plausible ordered incidences include:

- source constant channel to forced tail channel;
- direct tail to reciprocal seam channel;
- primitive and square states to boundary-current carrier;
- seam states into the two Hardy deficiency sectors;
- domain states through the Green operator to boundary readouts.

Each arrow determines a cohomological shift. Deleting the constant source
channel or treating a boundary readout as a state can change the Euler class
and prevent a normal Koszul contraction even when the scalar differential
equation still looks valid.

This gives a new interpretation of the constant augmentation: it may be needed
not only to homogenize the forced equation but also to balance the graded
source complex.

## Supertrace constraint

For odd `d` and `Q`, the supertrace of their supercommutator vanishes whenever
the trace is defined:

\[
\operatorname{str}(dQ+Qd)=0.
\]

Hence a finite-dimensional identity

\[
dQ+Qd=aI
\]

requires equal even and odd dimensions. More generally,

\[
dQ+Qd=aN
\]

requires `str(N)=0`.

Any imbalance must be carried by a boundary index, anomaly line, or infinite
Fredholm correction. It cannot be silently discarded.

## DPC

Before using Koszul signs or a Cartan anticommutator, require:

1. the ordered source incidence underlying every differential;
2. the induced cohomological degrees;
3. cone and dualization shifts;
4. even and odd source dimensions or Fredholm indices;
5. the supertrace of the proposed number operator;
6. determinant-line orientation;
7. preservation of grading under reciprocal and cutoff transport;
8. explicit typing of every boundary anomaly carrying an imbalance.

Reject:

- parity assigned only to repair a cube sign;
- reversing an incidence without dualizing the determinant line;
- inferring parity from a positive Gram matrix;
- deleting a source channel that changes the graded Euler class;
- a finite Cartan identity with nonzero supertrace on the right;
- grading that collapses under completion.

## Verdict

The graded double-category picture survives, but its parity must be derived
from ordered source incidence. The finite rectangular witness shows that
ungraded operator data and quadratic energy cannot recover that orientation.

