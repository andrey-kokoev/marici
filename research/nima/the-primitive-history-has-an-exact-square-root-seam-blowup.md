# The primitive history has an exact square-root seam blowup

## Off-seam Hilbert family

Let

\[
s=\frac12+\sigma+it,
\qquad
\sigma>0.
\]

The primitive history coefficient at prime \(p\) is

\[
p^{-1/2-\sigma-it}.
\]

Using the local history estimate

\[
\|\mathcal H_p\|^2\le5\log p,
\]

the global primitive history norm is bounded by

\[
\|\mathcal H_P(\sigma)\|^2
\le
5\sum_p\frac{\log p}{p^{1+2\sigma}}.
\]

Define the prime zeta function

\[
P(z)=\sum_pp^{-z}.
\]

Then

\[
-P'(1+2\sigma)
=
\sum_p\frac{\log p}{p^{1+2\sigma}}.
\]

Thus the primitive history is Hilbert-continuous for every \(\sigma>0\).

## Exact seam asymptotic

The prime zeta singularity is

\[
P(1+\eta)
=
\log\frac1\eta+O(1)
\]

as \(\eta\downarrow0\). Therefore

\[
-P'(1+\eta)
\sim
\frac1\eta.
\]

With \(\eta=2\sigma\),

\[
\sum_p\frac{\log p}{p^{1+2\sigma}}
\sim
\frac1{2\sigma}.
\]

Hence the primitive history norm has the sharp scale

\[
\|\mathcal H_P(\sigma)\|
=
O(\sigma^{-1/2}),
\]

and, at the level of the source majorant, this order cannot be improved.

This is not a failure of the off-seam construction. It is the exact Hilbert-to-distributional transition at the seam.

## Square channel

The square history coefficient remains

\[
\frac12p^{-1-2it}
\]

at \(\sigma=0\). Its history norm is controlled by

\[
\frac54
\sum_p\frac{\log p}{p^2}<\infty.
\]

Therefore the square history extends strongly to the seam in its Hilbert grade, while the primitive history does not.

## Correct uniformity statement

For every compact off-seam region with

\[
\sigma\ge\varepsilon>0,
\]

one has

\[
\sup_{\sigma\ge\varepsilon}
\sum_p\frac{\log p}{p^{1+2\sigma}}
\le
\sum_p\frac{\log p}{p^{1+2\varepsilon}}
<\infty.
\]

All operator, trace, and mixed-form bounds may be demanded uniformly on such regions.

No estimate may be uniform through \(\sigma=0\) in the primitive Hilbert norm.

## Rigged boundary value

A divergent Hilbert norm does not itself prevent a distributional seam value. Let \(\mathcal E_P\) be a source test space of prime-labelled histories with seminorms strong enough that

\[
\sum_pp^{-1/2}
\left|
\langle h_p,\varphi_p\rangle
\right|
<\infty
\]

for every \(\varphi\in\mathcal E_P\).

Then the primitive seam history can exist in the continuous dual

\[
\mathcal E_P'
\]

even though it does not belong to the Hilbert middle space.

The boundary theorem must prove weak convergence

\[
\mathcal H_P(\sigma)
\longrightarrow
\mathcal H_P(0)
\quad\text{in }\mathcal E_P'
\]

as \(\sigma\downarrow0\), not convergence in the Hilbert norm.

## No automatic boundary distribution

The off-seam estimate alone does not prove the dual limit. A family may have norm \(O(\sigma^{-1/2})\) and still oscillate or diverge against a permitted test vector.

The source must specify:

- the prime-scale test seminorms;
- density of finite prime packets;
- continuity of every local history and endpoint trace;
- domination permitting passage to the limit;
- compatibility with reciprocal and cutoff maps.

Only then is the seam value typed as a distribution rather than declared by analytic continuation.

## Mixed form scale

Suppose the square history has bounded norm and the mixed Green form is bounded by Cauchy–Schwarz. Then the naive off-seam estimate is

\[
|b_\alpha(\sigma;x,y)|
\le
C_\varepsilon
\|x\|_{\mathcal P_\sigma}
\|y\|_{\mathcal Q}
\]

uniformly for \(\sigma\ge\varepsilon\).

Near the seam, the Hilbert-space operator norm may grow at most at the primitive scale

\[
O(\sigma^{-1/2})
\]

under the local history majorant. A distributional boundary value must therefore be established weakly and may involve cancellation with the declared wall channel. It cannot be inferred from uniform Hilbert boundedness.

## Unauthorized renormalization hostile

Multiplying the primitive history by

\[
\sqrt{\sigma}
\]

would produce a bounded Hilbert family, but it changes the source incidence coefficient and forces the seam vector toward a normalized residue rather than the original primitive current.

Such a renormalization is permissible only if the source declares a residue or boundary-normal operator. It cannot be inserted merely to restore uniformity.

## Correct first-edge theorem

The first Adams edge should be a holomorphic or strongly continuous operator family

\[
B_\alpha(\sigma):
\mathcal P_\sigma\to\mathcal Q,
\qquad
\sigma>0,
\]

with:

1. uniform bounds on every \(\sigma\ge\varepsilon>0\);
2. chart and reciprocal covariance;
3. the oriented Green/Stokes identity;
4. weak extension to a declared dual boundary space at \(\sigma=0\);
5. no claim of primitive Hilbert continuity at the seam.

## Current frontier

The completion scale is now quantitative:

\[
\|\mathcal H_P(\sigma)\|
\asymp_{\mathrm{majorant}}
\sigma^{-1/2}.
\]

The remaining theorem is to construct the prime-scale test space and prove that the mixed Green/Stokes family has a weak seam limit there, with any singular part landing in the already declared constant–delta wall.
