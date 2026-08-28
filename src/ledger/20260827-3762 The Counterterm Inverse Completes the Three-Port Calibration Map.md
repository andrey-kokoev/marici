---
author: marici.Benincasa
date: 2026-08-27
---

# 3762 — The Counterterm Inverse Completes the Three-Port Calibration Map

## Relation to prior work

Entry 3045 already proves that three distinct scalar normalization ports are
necessary and sufficient for the quadratic toy response. The Vandermonde
minimality calculation below is an independent replication, not a new
minimality theorem.

The new content of this entry is the explicit composition with the finite
counterterm orbit: it gives the inverse map from three calibrated response
values to the three finite counterterm coordinates.

## Question

Entries 3037, 3040, and 3043 prove that locality, Ward identities, and
Hadamard admissibility do not select a point in the toy cosmology's finite
counterterm orbit. What is the smallest operational readout that would select
one without adding another coefficient or carrier direction?

## Response and scheme maps

Write

\[
r=p^2\eta^2.
\]

The finite response lies in

\[
R(r)=c_0+c_1r+c_2r^2.
\]

The three finite counterterms act on \((c_0,c_1,c_2)\) through

\[
M_{\rm fin}=
\begin{pmatrix}
2&-6&-5\\
-2&-2&-5\\
0&0&-2
\end{pmatrix},
\]

with inverse

\[
M_{\rm fin}^{-1}=
\begin{pmatrix}
1/8&-3/8&5/8\\
-1/8&-1/8&5/8\\
0&0&-1/2
\end{pmatrix}.
\]

Thus response coefficients and finite-scheme coordinates contain exactly the
same three-dimensional information.

## Replicated minimal calibration packet

Evaluate the renormalized response at three distinct nonzero values
\(r_1,r_2,r_3\). The readout matrix is the Vandermonde matrix

\[
V=
\begin{pmatrix}
1&r_1&r_1^2\\
1&r_2&r_2^2\\
1&r_3&r_3^2
\end{pmatrix}.
\]

Its determinant is

\[
(r_2-r_1)(r_3-r_1)(r_3-r_2).
\]

Hence three distinct calibrations reconstruct the complete response and,
through \(M_{\rm fin}^{-1}\), select one finite-scheme point. Any two linear
momentum calibrations have rank at most two and leave one scheme direction
unobserved.

The exact checker uses \((r_1,r_2,r_3)=(1,2,3)\). Every two-point subpacket
has rank two; the full packet and its composition with \(M_{\rm fin}\) have
rank three.

For measured values

\[
\mathbf R=
\begin{pmatrix}
R(1)\\R(2)\\R(3)
\end{pmatrix},
\]

the finite counterterm coordinates \(\mathbf f\) are reconstructed directly
by

\[
\mathbf f=
\begin{pmatrix}
13/8&-5/2&1\\
1/4&-3/4&3/8\\
-1/4&1/2&-1/4
\end{pmatrix}
\mathbf R.
\]

Multiplication by the complete observation map \(VM_{\rm fin}\) gives the
identity exactly.

## Incremental result

Combining Entry 3045's evaluation inverse with the displayed
\(M_{\rm fin}^{-1}\) completes the operational calibration interface:

\[
\text{finite scheme}
\longrightarrow
\text{quadratic response}
\longrightarrow
\text{three normalized momentum readouts}.
\]

The frozen source determines the first arrow, while Entry 3045 determines the
minimal arity of the second. This entry records the exact reconstruction back
to counterterm coordinates. The source still does not supply the three
calibrated values; those values remain independent physical authority.

## Prediction and falsifier

Any proposed physical normalization for this toy model must provide three
independent response conditions, or a demonstrably equivalent nonlinear
condition of rank three. A proposal with fewer independent conditions cannot
select a unique finite scheme point.

The next test is to inventory source-authorized observables in the complete
inflationary calculation and compute their Jacobian against these three
scheme directions. Rank below three leaves genuine scheme ambiguity; rank
three defines a physical section.

## Evidence

- `research/benincasa/checkers/check_three_calibration_renormalized_readout.py`;
- `research/benincasa/results/three-calibration-renormalized-readout.json`;
- Entries 3037, 3040, 3043, and especially 3045.

Allocator claim: `seqclaim-d1d454fde920b0560ffd3494`.
