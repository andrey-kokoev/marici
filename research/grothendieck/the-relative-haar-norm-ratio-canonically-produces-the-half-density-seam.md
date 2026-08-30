# The Relative Haar Norm Ratio Canonically Produces the Half-Density Seam

## Two typed metrics, one raw transport

Let

\[
\mathcal H_+=L^2(\mathbb R_+,dx),
\qquad
\mathcal H_\times=L^2(\mathbb R_+,dx/x).
\]

These are independently sourced additive-Haar and multiplicative-Haar
sectors. Apply the same raw dilation constructor

\[
(T_pf)(x)=f(x/p),
\qquad p>0.
\]

Direct change of variables gives

\[
\lVert T_pf\rVert_+^2=p\lVert f\rVert_+^2,
\qquad
\lVert T_pf\rVert_\times^2=\lVert f\rVert_\times^2.
\]

Hence the relative transport ratio is exactly `p`.

## Gauge-invariant formulation

The factor is not assigned to a preferred basis or to a weighted copy of one
Gram matrix. It is the ratio of two typed quadratic forms evaluated on the
same source-authorized transport. Independent unitary changes of frame in
the two sectors preserve that ratio.

Equivalently, the Radon–Nikodym derivative is multiplication by `x`, and its
positive square root is the canonical half-density comparison. In logarithmic
coordinates `x=exp(q)`, this square root is multiplication by `exp(q/2)`.

## Mellin orientation

After the Mellin character weight `p^{-s}`, the additive-Haar energy scales as

\[
p^{1-2\operatorname{Re}(s)},
\]

whereas the multiplicative-Haar energy scales as

\[
p^{-2\operatorname{Re}(s)}.
\]

The additive channel is isometric precisely when

\[
\operatorname{Re}(s)=\frac12.
\]

Thus the half-density offset and the unitary seam are invariant content of the
relative Haar comparison, not a removable diagonal weighting.

## Scope

This closes the relative-Haar orientation rung. It explains why the seam is
at one half, but it does not confine scalar zeros. The missing mate is now
between:

- the pair-label tail–seam Gram current;
- the two endpoint-oriented inverse-scale homotopies;
- this relative Haar modular cocycle.

The next calculation must determine whether the homotopy seam period transforms
by the same cocycle. If it does, the current comparison is source-coherent. If
it does not, the half-density seam and the zero-state boundary current remain
independent structures.

