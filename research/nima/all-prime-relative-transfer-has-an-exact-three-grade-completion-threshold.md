# All-prime relative transfer has an exact three-grade completion threshold

## Local return bound

For a prime \(p\), the source shell realization gives a return row
\(c_{p,z}\). On the centered seam,

\[
\lVert c_{p,it}\rVert^2
\leq
(\log p)\lVert\phi\rVert_2^2.
\]

The \(k\)-th traversal of the primitive Euler loop carries weight

\[
|q_p|^k=p^{-k/2}.
\]

Hence the weighted prime block has the uniform estimate

\[
\lVert p^{-k/2}c_{p,it}\rVert
\leq
p^{-k/2}\sqrt{\log p}\,\lVert\phi\rVert_2.
\]

## Hilbert and trace thresholds

For the all-prime direct sum, the Hilbert–Schmidt comparison is controlled by

\[
\sum_p p^{-k}\log p.
\]

It converges for \(k\geq2\) and diverges at \(k=1\).

Trace-class control is governed by

\[
\sum_p p^{-k/2}\sqrt{\log p}.
\]

It converges for \(k\geq3\) and diverges for \(k=1,2\).

Thus the source-derived relative transfer has the same three-grade boundary:

1. primitive grade \(k=1\): not uniformly Hilbert–Schmidt;
2. square grade \(k=2\): Hilbert–Schmidt but not trace class;
3. grades \(k\geq3\): trace class.

This is not a convention imposed on the Euler expansion. It follows from the
prime half-density and the seam-shell return bound.

## Sharpness

The upper estimate alone proves the positive inclusions. Sharpness over the
source class follows from a compactly supported source with nonzero endpoint
transform. For all sufficiently large primes, its first shell already contains
the full source, so the return norm is bounded below by a positive constant.

The lower comparison then contains:

\[
\sum_p p^{-k}
\]

for Hilbert–Schmidt norm and

\[
\sum_p p^{-k/2}
\]

for trace norm. Euler's divergence of \(\sum_p1/p\) makes the thresholds
sharp.

No assertion about a particular zero value is needed. The result classifies
the operator family uniformly over admissible sources.

## Architectural consequence

The primitive and square channels cannot be compressed into the trace-class
tail. They must remain as typed boundary data of the relative determinant:

- the primitive channel requires a distributional or renormalized boundary
  carrier;
- the square channel has Hilbert control but still requires relative
  determinant treatment;
- only the connected tail beginning at the third traversal admits an ordinary
  convergent determinant.

This independently recovers the order-three regularization boundary from the
control realization.

## What remains

The classification does not construct the renormalized primitive current or
the square relative determinant. It also does not prove reciprocal
cancellation, global theta–Euler equivalence, or the zero-state-to-flux
identity.

The next gate is to package the first two grades as boundary objects and prove
that reciprocal sewing transports them with the correct adjoint orientation,
while the trace-class tail descends ordinarily.

## DPC verdict

Resolved:

- all-prime operator-ideal thresholds of the local relative transfer;
- sharp separation of primitive, square, and connected-tail grades;
- necessity of order-three determinant regularization.

Withheld:

- source renormalization of the first two grades;
- reciprocal adjoint sewing;
- the complete relative determinant section;
- zero confinement.

## Verification

The checker `check_all_prime_transfer_thresholds.py` verifies the finite
prime-cutoff weight laws and their three distinct accumulation profiles. The
infinite convergence statements use the standard prime-series comparisons
stated above.
