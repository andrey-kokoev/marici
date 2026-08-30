# 2267 — The Leading Tensor Ward Grade Does Not Determine Finite-Soft Support

## Hard-to-vary claim

The frozen scalar contact source and its leading tensor Ward grade do not
determine a source-specific finite-soft transfer matrix.  Even cyclicly
equivariant analytic extensions with the same value and first normal jet at
\(q=0\) can have different finite-\(q\) rank-loss support.

## Hostile pair

Use the normalized leading matrix

\[
T_0=
\begin{pmatrix}
2&2&0\\
2&-1&-1\\
2&-1&1
\end{pmatrix}.
\]

Consider two analytic continuations:

\[
T_A(q)=T_0,
\]

and

\[
T_B(q)=T_0
\operatorname{diag}\bigl(1,1-q^2,1-q^2\bigr).
\]

The common factor on the shear plane preserves its rational \(C_3\)
representation and treats both tensor polarizations equally.  Moreover,

\[
T_A(0)=T_B(0),
\qquad
\partial_qT_A(0)=\partial_qT_B(0)=0.
\]

Nevertheless,

\[
\det T_A(q)=-12,
\]

while

\[
\det T_B(q)=-12(1-q^2)^2.
\]

Thus \(T_B\) loses both shear directions at \(q=\pm1\), whereas \(T_A\)
never does.

## Provenance consequence

Entries 2252–2256 establish the soft port, its leading Ward transfer, and an
open rank-three neighborhood.  They do not license choosing a global
finite-soft continuation.

The frozen weighted-correlator source supplies:

- scalar deletion-sector integrands;
- the diagonal Gaussian covariance \(K(y)\);
- the contact-normal packet.

It does not supply either of the following equivalent finite-soft source
objects:

\[
\frac{\delta A_g(p,p')}{\delta h_s(q)}
\]

for a curved-boundary Gaussian quadratic kernel, or a complete labelled
scalar--scalar--tensor wavefunction coefficient at finite tensor momentum.

Therefore the source-specific finite-\(q\) transfer requested by the observer
programme is presently underived, not zero.

## Required frozen enlargement

Before computing rank-loss support, freeze:

1. the finite-\(q\) scalar--scalar--tensor coefficient or curved-metric
   Gaussian kernel;
2. its two polarization conventions and gauge constraints;
3. its occurrence-labelled coupling to the three contact channels;
4. the physical relative contour/readout map.

Only that packet can distinguish \(T_A\), \(T_B\), or another continuation.
No fitted \(\Delta(q)\) is admissible.

## Verification

`research/benincasa/checkers/finite_soft_extension_nonuniqueness.rs` verifies
the common first jet and distinct determinant divisors exactly.
