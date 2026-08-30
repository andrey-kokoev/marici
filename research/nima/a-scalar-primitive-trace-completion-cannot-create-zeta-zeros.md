# A scalar primitive trace completion cannot create zeta zeros

The Hilbert--Schmidt Euler scattering model exposes a decisive zero-mechanism constraint.

In the right off-seam half-plane,
\[
\|S(z)\|<1.
\]
Therefore
\[
I-S(z)
\]
is invertible, and its regularized determinant satisfies
\[
\det_2(I-S(z))\neq0.
\]
For the diagonal prime operator this is also immediate from every local eigenvalue:
\[
|r_p(z)|<1.
\]

At finite cutoff,
\[
\det(I-S_X)
=
\det_2(I-S_X)\exp\bigl(-\operatorname{tr}S_X\bigr).
\]
Suppose one attempts to continue the primitive term by a finite holomorphic scalar \(\tau(z)\) and defines
\[
D(z)
=
\det_2(I-S(z))e^{-\tau(z)}.
\]
Both factors are zero-free. Hence
\[
D(z)\neq0
\]
throughout its holomorphic domain.

Consequently no scalar holomorphic regularization of the missing primitive trace can turn the diagonal Schur determinant into a function with zeta zeros. This is not a technical inconvenience. It proves that the zero mechanism must enter through a genuinely noninvertible constructor, not through an exponential correction.

There are only several legitimate possibilities:

1. The primitive completion is not a global scalar logarithm. It is a determinant-line section whose transition data can carry a divisor.
2. Endpoint, archimedean, or reciprocal sewing changes the operator itself:
   \[
   S(z)\longmapsto \widetilde S(z),
   \]
   and \(1\) may enter the spectrum of \(\widetilde S(z)\).
3. The completed object is a boundary pencil
   \[
   \Theta(z)-M(z)
   \]
   whose kernel collisions are not eigenvalue-one events of the diagonal Euler operator.
4. The regularized primitive trace develops logarithmic singularities at the zero divisor, in which case claiming it as an independently holomorphic source object would be circular.

This sharply separates the Euler carrier from the RH explanation. The diagonal Schur packet provides:

- exact prime labels;
- passive local delays;
- the \(k\ge2\) determinant packet;
- strict off-seam invertibility.

It cannot by itself provide nontrivial zeros in the right half of the strip.

The determinant-line version can be stated precisely. A nowhere-vanishing local exponential trivializes a determinant line only on a chart. To obtain a global section with zeros, the transition cocycle must be nontrivial or the section must fail to be invertible. The divisor then belongs to the sewing of local trivializations, not to any individual Euler exponential.

This returns the programme to the boundary-intersection picture:
\[
\text{zero-free Euler Schur carrier}
\to
\text{primitive/archimedean sewing}
\to
\text{finite boundary pencil}
\to
\text{Lagrangian nontransversality}.
\]

The spectral identification theorem must therefore show that
\[
\det(\Theta(z)-M(z))
\]
equals the completed \(\xi\)-section up to a nowhere-zero factor. It must not claim that the zero set arises from
\[
\det_2(I-S)e^{-\tau}.
\]

The minimal hostile chooses
\[
\tau(z)=-\log\zeta\!\left(\frac12-iz\right)-\log\det_2(I-S(z))
\]
on a zero-free chart and declares the result source-derived. This reproduces the desired scalar identity locally but places every zero and monodromy into an unauthorized branch of \(\tau\).

A second hostile retains the diagonal contraction after all sewing. Then \(1\) never reaches the spectrum, so any claimed zeta zero must have been inserted through scalar normalization.

The next source-native calculation is now clear:

> Identify the first constructor cell whose completion can lose transversality even though the prime-diagonal Euler carrier remains strictly contractive.

The likely candidates are the primitive wall-to-trace incidence, reciprocal-sheet sewing, and the archimedean endpoint relation. That cell, rather than the Euler product alone, must carry the zero divisor.
