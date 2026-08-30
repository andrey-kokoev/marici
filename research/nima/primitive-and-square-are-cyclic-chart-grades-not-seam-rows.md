# Primitive and square are cyclic chart grades, not seam rows

## The transpose-range question was ill-typed

The tail–seam synthesis transpose acts on linear boundary functionals. The
primitive and prime-square currents occur instead as the first two cyclic
grades of an Euler loop:

\[
\mathfrak c_k(L)=\frac1k\operatorname{Tr}(L^k),
\qquad k\geq1.
\]

They enter through

\[
-\log\det(I-L)=\sum_{k\geq1}\mathfrak c_k(L).
\]

Although each finite arithmetic atom may be represented by a boundary
distribution, the operation producing \(\mathfrak c_k\) is polynomial in
the loop. For \(k>1\), it is not a fixed linear covector on the one-particle
source state. Asking whether the square current lies in the range of the
linear tail–seam transpose therefore confuses two carriers.

## Minimal separation witness

Let

\[
L_1=\operatorname{diag}(1,1),
\qquad
L_2=\operatorname{diag}(0,2).
\]

They have the same primitive grade:

\[
\mathfrak c_1(L_1)=mathfrak c_1(L_2)=2.
\]

Their square grades differ:

\[
\mathfrak c_2(L_1)=1,
\qquad
\mathfrak c_2(L_2)=2.
\]

No downstream function of the primitive scalar alone can reconstruct the
square grade. The square current needs the second cyclic-power carrier, not a
second name for the primitive readout.

## Correct architecture

There are two complete presentations.

The additive presentation contains the completed theta source and its
state-valued tail–seam cut. The multiplicative presentation contains the Euler
loop and its cyclic tower. A comparison constructor must relate the completed
objects:

\[
\mathcal L_\theta
\longrightarrow
\mathcal L_\infty\otimes\operatorname{Det}_{\mathrm{rel}}(I-L).
\]

The first two Euler grades remain explicit because their regularity differs
from the trace-class tail. They are boundary data of the chart transition,
not extra additive state channels to append to the theta seam.

The appropriate arithmetic incidence is therefore graded:

\[
L\longmapsto
\bigl(
\mathfrak c_1(L),
\mathfrak c_2(L),
\mathfrak c_{\geq3}(L)
\bigr).
\]

Only after this cyclic formation may the comparison to the theta boundary
object be tested.

## Double-counting falsifier

If the completed theta presentation is already identified with the full
determinant series, adding separate primitive and square ports to its scalar
current changes the first two formal coefficients from \(1\) and \(1/2\)
to \(2\) and \(1\). That is not a refinement; it is duplication.

Any proposed common boundary matrix must therefore declare whether its first
two grades are:

- coordinates of the Euler chart retained during comparison; or
- genuinely independent theta observables derived before Euler
  factorization.

Without the second derivation, treating them as independent theta rows is
rejected.

## DPC verdict

Resolved:

- the primitive and square currents are cyclic determinant grades;
- the square grade cannot descend from the primitive scalar;
- appending them to the already completed theta current double-counts the
  first two determinant coefficients.

Withheld:

- construction of the complete Euler-to-theta comparison constructor;
- its first and second cyclic incidence cells;
- compatibility with reciprocal sewing and completion;
- the zero-state boundary-flux bridge.

The next finite gate is the two-addition comparison: its undivided theta
section, cyclic determinant grades, and shared moving-seam corner must agree in
both addition orders.

## Verification

The checker `check_cyclic_chart_grade_typing.py` verifies the equal-primitive
and unequal-square witness, direct-sum additivity of cyclic grades, and the
formal double-counting defect.
