# The Maslov Carry Is Finitely Coherent and Globally Divergent

## Lifted area coordinate

Measure phase-space area in units of (2\pi). Every nonnegative area has a unique decomposition

\[
\frac{\mathcal A}{2\pi}=m+\theta,
\qquad
m\in\mathbb Z_{\ge0},
\qquad
0\le\theta<1.
\]

Here (m) is the Maslov crossing grade and (\theta) is the residual phase fraction.

For two additive area cells, the exact composition law is

\[
(m,\theta)\star(n,\phi)
=
\left(
m+n+\lfloor\theta+\phi\rfloor,
\theta+\phi-\lfloor\theta+\phi\rfloor
\right).
\]

The extra integer is the ordinary carry across a phase-wrapping boundary.

## No finite prime-order anomaly

The carry law is associative and commutative because it is simply addition on the universal cover followed by the unique integer-plus-fraction decomposition. Therefore every finite reordering of additive prime-area increments gives the same total grade and residual phase.

This closes another tempting anomaly route. The Maslov lift does not acquire a finite braid defect merely because phase wrapping occurs. Any finite prime-order discrepancy signals that some cross-area cell or affine-origin transport was omitted.

## Two-axis refinement warning

If both position and frequency spans are refined, area is not the sum of only the matching diagonal rectangles:

\[
(\Delta q_1+\Delta q_2)(\Delta\xi_1+\Delta\xi_2)
=
\Delta q_1\Delta\xi_1
+
\Delta q_2\Delta\xi_2
+
\Delta q_1\Delta\xi_2
+
\Delta q_2\Delta\xi_1.
\]

The cross rectangles are mandatory comparison cells. Omitting them can manufacture a path-dependent grade. This is the metaplectic analogue of dropping seam intervals during prime resegmentation.

## Infinite-cutoff obstruction

For a fixed positive frequency separation and an expanding total position length (L),

\[
m(L)=left\lfloor\frac{\Delta\xi\,L}{2\pi}\right\rfloor
\]

grows without bound. Finite coherence therefore does not provide a completed integer grade. The remaining object must be relative or renormalized:

- a grade difference between reciprocal sectors;
- a finite part after subtracting a source-derived extensive term;
- a spectral-flow current whose endpoint difference is finite;
- or a projective phase retaining only the residual fraction while exporting the divergent grade as boundary data.

No subtraction may be chosen merely to force Krein orientation.

## Consequence for arithmetic currents

The universal carry law itself contains no prime-specific information. It cannot explain RH. Primitive, square, and archimedean currents may provide the source-derived relative normalization, but they are not identified with the carry merely because both are boundary data.

The next theorem must compute the Maslov grade of the actual labelled theta cutoff and compare the two reciprocal sectors before scalar aggregation. The viable invariant is a relative grade whose cutoff divergence cancels by a named source coherence.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/maslov_carry_cocycle.py` verifies associativity, commutativity, equality with total-area lifting, and the necessity of cross rectangles under two-axis refinement.
