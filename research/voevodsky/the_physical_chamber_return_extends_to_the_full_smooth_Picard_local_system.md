# The physical-chamber return extends to the full smooth Picard local system

## Smoothness input

The raw log-smoothness certificate gives an exhaustive singularity test for the compactified branch quartic. Its controlling determinant is

\[
\det N=-2E^2(AB)^2,
\]

where

\[
E=x+y+z,
\quad A=(x-y)^2-z^2,
\quad B=(x+y)^2-z^2.
\]

Inside the strict positive triangle chamber,

\[
E>0,
\quad x-y-z<0,
\quad x-y+z>0,
\quad x+y-z>0,
\]

so \(A<0\), \(B>0\), and \(EAB\ne0\). The coordinate-stratum minors are also nonzero there. The remaining axis coefficient contains

\[
E^4-(x^2+y^2-z^2)E^2+x^2y^2,
\]

which expands as a polynomial with strictly positive coefficients for \(x,y,z>0\). Hence the compact branch curve and its double cover remain smooth throughout the convex exchange path.

## Picard transport

The previous location calculation showed that the four split fibers remain distinct and their \(W=\pm Q\) component labels continue without permutation. Smooth proper transport therefore upgrades this from a location statement to a statement in the full integral Picard local system:

\[
d_i(y,x,z)\longmapsto d_i(x,y,z).
\]

The chamber return matrix on the primitive \(A_1^3\) lattice is exactly the identity.

## Consequence

There is now no smooth-family loophole: canonical physical-chamber Gauss--Manin transport does not supply a route swap or sign change. Any nontrivial return needed to identify the wall-extension \(v_{\rm alg}\) covector with a fixed-pyramid route must come from additional relative/Gysin structure, not from absolute Picard continuation.

This separates the two systems cleanly:

- absolute split-fiber Picard transport: canonical and label-preserving;
- relative one-wall extension transport: orientation-twisted and \(v_{\rm alg}\)-valued;
- missing coherence comparison: a map between them.

Verification:

- `research/voevodsky/checkers/check_physical_chamber_full_smooth_return.py`
- `research/voevodsky/results/physical_chamber_full_smooth_return.json`
