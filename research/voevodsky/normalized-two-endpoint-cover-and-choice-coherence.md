# Normalized two-endpoint cover and partition-choice coherence

## Question

Can the remaining cover, overlap width, and coordinate normalization be fixed explicitly, and do different admissible choices preserve the closed-form domain?

## Claim boundary

This packet chooses one analytic auxiliary cover and proves bounded-change coherence between admissible partitions. It does not claim the choice is canonical or preserve positivity without updating constants.

## Normalization

Identify the physical interval \((-L,L)\) with the angular interval \((0,2\pi)\) by

\[
\theta=\frac{\pi(x+L)}{L}.
\]

Choose a physical overlap of width \(h_x=L\), hence angular overlap

\[
h_\theta=\frac{\pi h_x}{L}=\pi.
\]

Use the septic smoothstep on each of the two periodic overlap transitions and complementary endpoint windows. The windows are nonnegative, sum to one, and are subordinate to proper endpoint arcs.

The previously computed leakage becomes

\[
C_{\rm loc}
\le
\frac{224\sqrt5\,\pi}{25h_\theta^2}
=
\frac{224\sqrt5}{25\pi}.
\]

More generally, for physical overlap \(h_x\),

\[
C_{\rm loc}(L,h_x)
\le
\frac{224\sqrt5\,L^2}{25\pi h_x^2}.
\]

## Choice coherence

Let \(\{\chi_j\}\) and \(\{\widetilde\chi_j\}\) be two admissible finite partitions with finite first absolute Fourier moments. For each paired chart, the commutator difference obeys

\[
\lVert[\Lambda,M_{\chi_j}]-[\Lambda,M_{\widetilde\chi_j}]\rVert
\le
C_{\rm loc}(\chi_j)+C_{\rm loc}(\widetilde\chi_j).
\]

Hence any declared localization formula built from finitely many such commutator cells with bounded coefficients changes by an explicitly bounded order-zero form. Closedness and the form domain are preserved for that declared formula under the bounded perturbation. Numerical lower bounds and positivity margins must be shifted by the same explicit constant; choice coherence does not make positivity invariant for free. The formula itself must state whether it uses a linear partition, a square partition, or another localization convention; partition of unity alone does not choose that convention.

## Disposition

The auxiliary localization data are now fully instantiated:

- interval-to-circle coordinate;
- two endpoint arcs;
- overlap width \(h_x=L\);
- explicit septic partition;
- leakage bound \(224\sqrt5/(25\pi)\);
- bounded-change comparison for alternative admissible partitions.

The remaining local positivity work is no longer localization: it is interval enclosure of the finite low block and its coupling to the signed tail.

## Verification

- `research/voevodsky/checkers/check_normalized_endpoint_cover_coherence.py`
- `research/voevodsky/results/normalized_endpoint_cover_coherence.json`
