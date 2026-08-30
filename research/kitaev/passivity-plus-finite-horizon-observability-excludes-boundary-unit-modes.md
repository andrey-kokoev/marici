# Passivity plus finite-horizon observability excludes boundary unit modes

## Question

Which source law is strong enough to exclude the unit eigenvalue of the
boundary loop without assuming a one-step small-gain bound?

## Passive boundary realization

Let \(L\) be the normalized boundary return operator and suppose the source
provides a defect output \(O\) satisfying

\[
I-L^*L=O^*O.
\]

This identity says that norm not returned to the boundary is recorded in a
typed output channel. It implies \(\|L\|\le 1\), but does not imply strict
contraction. If \(Ly=y\), then

\[
\|y\|^2-\|Ly\|^2=\|Oy\|^2=0.
\]

Thus every unit fixed mode is invisible to the dissipation output. Passivity
alone permits such a mode.

## Telescoping observability theorem

For a positive integer \(m\), define

\[
W_m=\sum_{k=0}^{m-1}(L^*)^kO^*OL^k.
\]

The defect identity telescopes exactly:

\[
W_m=I-(L^*)^mL^m.
\]

If the finite-horizon output is uniformly observable,

\[
W_m\ge\varepsilon I
\]

for some \(\varepsilon>0\), then

\[
\|L^m\|\le q,
\qquad
q=\sqrt{1-\varepsilon}<1.
\]

Hence \(L\) may have one-step norm one, yet its \(m\)th power is a strict
contraction. In particular, \(1\) is not in its spectrum and

\[
(I-L)^{-1}
=(I+L+\cdots+L^{m-1})(I-L^m)^{-1}.
\]

Since \(\|L\|\le 1\),

\[
\|(I-L)^{-1}\|
\le
\frac{m}{1-\sqrt{1-\varepsilon}}.
\]

This is a completion-stable Schur-complement certificate whenever \(m\) and
\(\varepsilon\) are uniform over the cutoffs and parameter compactum.

## Why this is stronger than pointwise detectability

For a fixed cutoff, it is enough to rule out nonzero vectors satisfying both

\[
Ly=y,
\qquad
Oy=0.
\]

But cutoffwise absence of such vectors supplies no uniform inverse bound.
The Gramian inequality supplies quantitative separation of every normalized
boundary state from the lossless unobserved sector.

The theorem therefore turns the remaining boundary problem into a finite
source question:

> Does every boundary state lose a uniformly detectable amount of energy
> through the seam, archimedean, primitive, or square output within a fixed
> number of returns?

## Multiple typed outputs

If the authorized outputs are \(O_j\), use

\[
I-L^*L=\sum_j O_j^*O_j.
\]

The observability Gramian becomes

\[
W_m=
\sum_{k=0}^{m-1}
\sum_j
(L^*)^kO_j^*O_jL^k.
\]

This preserves typing: duplicated even Clark rows do not become odd
information merely because they appear twice. The source must identify which
rows carry primitive, square, seam, archimedean, and sheet-odd loss.

## Reciprocal covariance is not strictness

Suppose a sector involution relates the two loops by a similarity or adjoint
relation. It then transports unit modes between sectors or constrains their
location. It does not exclude them. In particular:

- a unitary loop is perfectly conservative and may have eigenvalue \(1\);
- a reciprocal pair can carry reflected unit modes;
- determinant symmetry can pair zeros while leaving both present.

The needed extra law is not reciprocity itself but observable escape from the
lossless boundary subspace.

## Minimal hostile fixtures

### Passive but not strict

Take \(L=1\) and \(O=0\). The defect identity holds, every Gramian vanishes,
and the Schur complement \(I-L\) is zero.

### Loss exists but misses the fixed mode

Take

\[
L=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
O=
\begin{pmatrix}
0&1
\end{pmatrix}.
\]

Then \(I-L^*L=O^*O\), but the first coordinate is a lossless invisible fixed
mode. Adding arbitrarily strong observation of the second coordinate does not
repair it.

### Finite observability without uniform completion

Let

\[
L_N=
\begin{pmatrix}
\sqrt{1-N^{-2}}&0\\
0&0
\end{pmatrix},
\qquad
O_N=
\begin{pmatrix}
N^{-1}&0\\
0&1
\end{pmatrix}.
\]

The defect identity holds and every finite system is observable, but the
smallest Gramian eigenvalue tends to zero. The inverse norm of \(I-L_N\)
diverges. Pointwise strictness is not completion stability.

## Source instantiation required

The theorem becomes theta-bearing only after the source derives:

1. the normalized loop \(L_s\) from \(B_s\), \(C_s\), \(D_s\), and the
   connected bulk inverse;
2. a sector-native positive metric;
3. an exact defect identity with independently typed output rows;
4. a fixed observation horizon;
5. a cutoff-independent Gramian lower bound on compact subsets of each open
   sector.

If the natural metric is Krein rather than Hilbert, the positive defect
identity must be replaced by a source-valid chartwise or Pontryagin-space
statement. No positivity may be imported from the desired scalar conclusion.

## Disposition

The abstract missing law is now sharper than small gain: a passive
realization plus uniform finite-horizon observability implies stable boundary
invertibility.

This explains why seam and current rows may matter even when none is
pointwise injective. Their time-ordered returns can jointly observe the
lossless sector. It also identifies the decisive falsifier: a normalized
sequence of boundary states whose total typed loss over every fixed return
horizon tends to zero.

## Claim boundary

This packet proves an abstract Hilbert-space theorem. It does not establish
the theta defect identity, specify the boundary rows, prove a common positive
metric, or show that a fixed observation horizon survives restricted-product
completion.
