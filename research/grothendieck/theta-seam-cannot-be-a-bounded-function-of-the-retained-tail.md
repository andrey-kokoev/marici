# The theta seam cannot be a bounded function of the retained tail

## Defect audit endpoint

The doubled Clark bulk closes to an exact Gram trace. The continuous forcing
norm is a canonical reservoir current. The Jordan coupling is removed by the
source-derived scale shear, and its sheet-odd first moment cancels only after
genuine bilateral reflection. The remaining mixed seam has an exact Gram
realization.

That realization exposes a genuine operator obstruction.

## Exact cut decomposition

For a translated source label `p>=0`, define

\[
 g_p(t)=\Phi(t+p),
 \qquad
 h_p(t)=\mathbf1_{0\le t\le p}\Phi(p-t),
 \qquad t\ge0.
\]

The feature `g_p` is the part of the translated bilateral source remaining in
the positive chamber; `h_p` is the part crossing the modular seam. Their Gram
kernels give the exact cut decomposition

\[
 A(|p-r|)=\langle g_p,g_r\rangle+\langle h_p,h_r\rangle.
\]

Thus the full translated source embeds isometrically into

\[
 \mathcal H_{\rm tail}\oplus\mathcal H_{\rm seam}.
\]

The seam space has infinite rank; locally its kernel begins with the Brownian
covariance `Phi(0)^2 min(p,r)`.

## No bounded reconstruction from the tail

Suppose a bounded operator

\[
 \Gamma:\mathcal H_{\rm tail}\to\mathcal H_{\rm seam}
\]

satisfied

\[
 h_p=\Gamma g_p
\]

for every source translation in the arithmetic orbit. Then

\[
 \lVert h_p\rVert
 \le\lVert\Gamma\rVert\,\lVert g_p\rVert.
\]

But direct change of variables gives

\[
 \lVert g_p\rVert^2
 =\int_p^\infty\Phi(u)^2\,du
 \longrightarrow0,
\]

whereas

\[
 \lVert h_p\rVert^2
 =\int_0^p\Phi(u)^2\,du
 \longrightarrow\lVert\Phi\rVert_{L^2(\mathbb R_+)}^2>0.
\]

Therefore

\[
 \boxed{
 \text{no bounded }\Gamma\text{ can reconstruct the seam feature from the
 retained tail on the full translation orbit}.}
\]

In fact the norm ratio diverges:

\[
 \frac{\lVert h_p\rVert}{\lVert g_p\rVert}\longrightarrow\infty.
\]

Since the arithmetic samples include `p=log n` with no upper bound, this is
not an irrelevant large-translation regime.

## Meaning of the obstruction

As the source is translated, its state does not disappear. Its norm migrates
from the retained positive tail into the seam coordinate. Projecting away the
seam creates precisely the appearance of a partner escaping at infinity.

Hence the scalar physical readout cannot be justified as a bounded Schur
complement of the tail alone. Any proof using such a contraction is closed.

The surviving architectures are narrower:

1. retain `H_seam` as an independent component of the physical state;
2. use an explicitly typed unbounded closed boundary relation with a graph
   norm controlling both `g_p` and `h_p`;
3. construct a determinant/Pfaffian of the full block system before scalar
   projection;
4. prove that the actual admissible zero-state domain excludes the escaping
   translation directions by an independently sourced constraint.

## Connection to the spectral wave

For compactly supported translation packets `c`, the seam feature

\[
 s_c(t)=\int_t^\infty\Phi(p-t)c(p)\,dp
\]

is a legitimate Hilbert vector. The bare spectral wave used in the theta
transform is not automatically in that packet Hilbert space. It needs a
cutoff, resolvent domain, or renormalized boundary pairing.

Thus there are two linked domain failures:

\[
 \boxed{
 \text{unbounded tail-to-seam reconstruction}
 +\text{untyped bare spectral seam wave}.}
\]

Together they prevent the finite Gram closure from being promoted directly
to the completed scalar readout.

## Typed falsifier

The bounded-coupling proposal has the exact rejection witness

```json
{
  "code": "tail_to_seam_coupling_unbounded",
  "label_family": "p -> infinity (including p=log n)",
  "tail_norm_squared": "integral_p^infinity Phi(u)^2 du -> 0",
  "seam_norm_squared": "integral_0^p Phi(u)^2 du -> ||Phi||_2^2",
  "operator_norm_lower_bound": "||h_p||/||g_p|| -> infinity",
  "bounded_boundary_constructor": null
}
```

## Honest frontier

The first real obstacle is no longer positivity of the bulk or cancellation
of a finite defect. It is construction of the physical full block state and
its scalar boundary readout when an infinite-rank seam carries asymptotically
all translated source norm.

The next admissible attack is an unbounded closed-relation or full block
determinant construction. Replacing the seam by a fitted finite-rank repair or
a bounded tail function is now prohibited by the exact norm-ratio theorem.

