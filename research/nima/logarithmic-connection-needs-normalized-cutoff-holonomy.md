# The logarithmic connection needs normalized cutoff holonomy

## The remaining ambiguity

A source-derived logarithmic connection fixes a meromorphic determinant section up to a constant on each connected cutoff object. It does not by itself force those constants to compose coherently across different cutoff-addition paths.

Let \(X\) be a finite labelled cutoff, and let \(p\) and \(q\) be two admissible additions. Write the determinant increment for an inclusion as

\[
C_{X,p}(z)=\frac{\Delta_{X\cup\{p\}}(z)}{\Delta_X(z)}.
\]

The two paths around the addition square have holonomy

\[
H_{X;p,q}(z)=
\frac{C_{X\cup\{p\},q}(z)C_{X,p}(z)}
{C_{X\cup\{q\},p}(z)C_{X,q}(z)}.
\]

## What the connection proves

If the connection increments are additive on the square, then

\[
d\log H_{X;p,q}=0.
\]

This proves only that \(H_{X;p,q}\) is constant in the spectral parameter. It does not prove that the constant is \(1\).

The distinction is exact. Multiplying any one edge constructor by a nontrivial constant phase preserves its logarithmic derivative, residues, and local divisor while producing nontrivial cutoff holonomy.

## The required normalization cell

Choose a source-authorized basepoint \(z_*\) at which every finite determinant is defined and nonzero. Require

\[
\Delta_X(z_*)=1
\]

for every cutoff, or equivalently require every inclusion increment to equal \(1\) at \(z_*\). Then connection additivity gives constant holonomy and basepoint evaluation gives

\[
H_{X;p,q}(z_*)=1.
\]

Therefore \(H_{X;p,q}=1\) identically.

This is a genuine coherence cell, not a cosmetic normalization. It upgrades a family of locally authoritative connections into one functorial determinant section over the cutoff category.

## Higher paths

For three additions, pairwise squares are not enough unless their normalization cells satisfy the braid relation. The finite cutoff system should therefore be compiled as follows:

1. objects are labelled cutoffs;
2. arrows are source-authorized additions;
3. each arrow carries a determinant increment and typed current increment;
4. each admissible square carries a normalized comparison cell;
5. comparison cells satisfy the braid and distant-commutation relations on higher permutohedral faces.

This is the determinant-line instance of the dependency-aware repair compiler, with additions rather than temporal repairs. No time interpretation is required.

## Schatten-three anomaly placement

The third-order regularized determinant may carry a multiplicative anomaly when operations are composed rather than joined as independent direct sums. Primitive and square currents must therefore be tested as candidate anomaly coordinates.

They succeed only if their combined edge contribution makes every authorized square holonomy equal to \(1\), not merely spectrally constant. A surviving constant phase is a typed obstruction.

## Finite falsifier

At two independently added primes, compute both determinant-increment products before scalar completion. Reject the construction if either condition fails:

\[
d\log H_{X;p,q}=0,
\qquad
H_{X;p,q}(z_*)=1.
\]

The first failure is connection curvature. The second is constant normalization holonomy. Either prevents the finite determinant family from defining a coherent section over the cutoff category.

