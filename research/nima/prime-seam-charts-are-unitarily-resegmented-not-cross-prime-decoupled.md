# Prime seam charts are unitarily resegmented, not cross-prime decoupled

## One boundary history, many prime partitions

For a window length \(L>0\), define the seam-history transform

\[
(\mathcal B_Lf)_j
=
f|_{[jL,(j+1)L]}.
\]

The shell intervals are disjoint and cover the half-line, so

\[
\mathcal B_L^*\mathcal B_L=I.
\]

Each prime length \(L_p=\log p\) therefore gives an isometric chart of the
same source history.

## Cross-prime comparison

For two primes, define the resegmentation map

\[
U_{p,q}=\mathcal B_{L_q}\mathcal B_{L_p}^*.
\]

It concatenates the \(p\)-windows back into the source and cuts the result
into \(q\)-windows. On the incidence image it is unitary:

\[
U_{p,q}^*U_{p,q}=I,
\qquad
\lVert U_{p,q}\rVert=1.
\]

For three prime lengths,

\[
U_{q,r}U_{p,q}=U_{p,r}.
\]

Thus the cross-prime seam charts already form an exact transport groupoid.

## Explicit overlap kernel

The block overlap between shell \(j\) in the \(p\)-chart and shell \(k\)
in the \(q\)-chart is supported on the interval intersection

\[
I_{p,j}\cap I_{q,k}.
\]

For the energy pairing its coefficient is

\[
G_{p,q}(j,k)
=
\int_{I_{p,j}\cap I_{q,k}}|\phi(v)|^2\,dv.
\]

This kernel is sparse at fixed \(p,q\), because only intersecting intervals
communicate. It does not decay in operator norm as the primes separate:
resegmentation remains unitary.

## No orthogonality from relabelling

Prime charts are not independent boundary directions. They are different
segmentations of one state. A source vector supported in the first common
interval is represented faithfully in both charts and has comparison norm
one.

Therefore the orthogonal-prime model from the anomaly summability audit cannot
be justified by seam partitioning. The raw seam geometry supplies maximal
cross-prime coherence, not decoupling.

Any global anomaly convergence must instead come from:

- prime weights inside the actual relative-transfer factors;
- cancellations in the trace polynomial;
- additional source localization beyond interval partitioning; or
- a joint determinant construction that avoids summing pair cells
  absolutely.

## DPC verdict

Resolved:

- the exact source-derived cross-prime resegmentation operator;
- its unitary norm and groupoid composition law;
- the interval-intersection overlap kernel;
- failure of prime-chart orthogonality.

Withheld:

- the weighted relative-transfer cross traces;
- cancellation or conditional convergence of their anomaly cells;
- a joint all-prime determinant construction;
- archimedean and zero-state bridges.

The finite falsifier for a claimed cross-prime decay law is the unit source
state supported in a common interval: both charts represent it with full norm.

## Verification

The checker `check_prime_seam_resegmentation.py` verifies exact energy
preservation, resegmentation composition, interval-overlap support, and
unit-norm common states for many pairs of finite window lengths.
