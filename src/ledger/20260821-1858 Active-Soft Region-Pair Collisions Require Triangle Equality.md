# 1858 — Active-Soft Region-Pair Collisions Require Triangle Equality

> **Correction (Entry 1859).**  The four displayed equalities are correct, but
> their interpretation as triangle saturation, collinearity, or Gram support
> is withdrawn.  The (y_i) are radial distances from the soft loop point to
> different centers; the three terms are not the side lengths of one triangle.

## Frozen wall equations

For the representative pair,

\[
q_1=3t+y_3+y_5,
\qquad
q_2=3t+y_2+y_4.
\]

An active-soft endpoint sets one of

\[
y_2,y_3,y_4,y_5
\]

to zero while retaining (q_1=q_2=0).  Eliminating (t) gives the four
cases

\[
\begin{array}{c|c}
\text{soft occurrence}&\text{required metric equality}\\
\hline
y_2=0&y_4=y_3+y_5\\
y_3=0&y_5=y_2+y_4\\
y_4=0&y_2=y_3+y_5\\
y_5=0&y_3=y_2+y_4.
\end{array}
\]

## Geometric meaning

Each equality saturates a labelled triangle inequality among three centers.
For example,

\[
y_2=0,qquad y_4=y_3+y_5
\]

means that the soft center (C_2) lies on the segment joining (C_3) and
(C_5), with the displayed ordering.  The other three cases are its labelled
analogues.

Thus an active-soft region-pair collision is not generic on an edge-soft
divisor.  Its exact support is

\[
\boxed{
\text{edge soft}
\cap
\text{three-center Gram/triangle equality}
\cap
\text{segment chamber}.
}
\]

All three ingredients are already frozen carrier data.

## Correction of the frontier

Entry 1836 correctly treated its radial calculation as conditional and left
existence open.  The existence condition is now solved: its second-Rees
(delta^2\log\delta) endpoint coefficient can occur only on this deeper
existing support, not at a generic point of the soft divisor.

## Narrow result

No new carrier stratum is needed.  The unresolved datum is the value of the
ten-term OFPT source coefficient after restriction to one supported endpoint
chamber.

## Next falsifier

Choose one labelled endpoint, impose its soft and triangle-equality equations
in the exact ten-term double-residue coefficient, and determine whether the
second-Rees logarithmic coefficient is nonzero.  Track any additional
denominator collision before assigning a physical class.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_active_soft_existence.py`
- `research/benincasa/results/five-site-region-pair-active-soft-existence.json`
- Entries 1836 and 1854
- allocator claim: `seqclaim-70ee43a452f173fae51a1103`
