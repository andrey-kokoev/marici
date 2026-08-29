# Common scalar augmentation produces a rank-one cross-prime mode

## Label-diagonal source

Before scalar pushforward, the completed source is the orthogonal label sum

\[
\mathcal K
=
\bigoplus_{p,k}\mathcal H_{p,k}.
\]

Local Adams histories and their Fourier presentations are diagonal in \((p,k)\). Therefore any cross-prime interaction must enter through an additional assembly arrow.

## Augmentation vector

At off-seam displacement \(\sigma>0\), the primitive Euler coefficient row is

\[
a_{\sigma,p,k}
=
\frac1k p^{-k(1/2+\sigma)}
\]

up to the unit Mellin phase.

Define the label augmentation

\[
U_\sigma(x)
=
\sum_{p,k}
a_{\sigma,p,k}x_{p,k}.
\]

On the label Hilbert factor, its Gram is

\[
U_\sigma^{*}U_\sigma
=
|a_\sigma\rangle\langle a_\sigma|.
\]

Thus all cross-prime terms created solely by the common scalar evaluator form one rank-one coherent mode:

\[
K_{(p,k),(q,\ell)}
=
\overline{a_{\sigma,p,k}}
a_{\sigma,q,\ell}.
\]

No primitive \(pq\) label is created. The labels remain separate; only their outputs meet at one evaluator.

## Off-seam boundedness

The squared row norm is

\[
\|a_\sigma\|^2
=
\sum_{p}\sum_{k\ge1}
\frac1{k^2}p^{-k(1+2\sigma)}.
\]

For every \(\sigma>0\), this converges. On compact off-seam sets

\[
\sigma\ge\varepsilon>0,
\]

it is uniformly bounded.

At the seam, the \(k=1\) contribution contains

\[
\sum_p\frac1p,
\]

so the row is not an ordinary Hilbert vector. The seam augmentation must remain a distributional boundary value in the exponential rigging.

## Green comparison

Let \(G_{\mathrm{diag}}\) be the label-diagonal source Green form. The normalized coherent loading is

\[
K_\sigma
=
G_{\mathrm{diag}}^{-1/2}
U_\sigma^{*}U_\sigma
G_{\mathrm{diag}}^{-1/2}.
\]

It has rank at most one. Therefore its only nonzero eigenvalue is

\[
\lambda_\sigma
=
\left\|
U_\sigma G_{\mathrm{diag}}^{-1/2}
\right\|^2.
\]

The strict common-mode margin is exactly

\[
\delta_{\mathrm{common}}
=
1-\sup\lambda_\sigma.
\]

This is the coherent-diagonal or terminal-loading margin in scalar form.

## Two-atom interpretation

For distinct primes \(p\ne q\), the mixed entry

\[
\overline a_{\sigma,p,1}a_{\sigma,q,1}
\]

is an authorized analytic interaction produced by the common evaluator. It is not a primitive von Mangoldt flux at \(pq\).

A primitive \(pq\) flux would require a new label constructor

\[
e_p\otimes e_q\longrightarrow e_{pq},
\]

which is absent from this augmentation.

## Beyond rank one

If the complete observer has four Fourier character ports and separate wall/tail outputs, the augmentation target is finite-dimensional rather than scalar. Then the cross-prime kernel has rank bounded by the observer-port dimension. The same theorem uses

\[
U_\sigma^{*}U_\sigma
\]

and its finite nonzero singular spectrum.

Any larger cross-prime rank must come from an independently declared assembly constructor.

## Hostiles

Applying augmentation before forming the typed Green block hides whether a mixed term came from a shared evaluator or an unauthorized primitive label product.

A finite-cutoff augmentation row is always bounded, while its norm can diverge at the seam.

Several evaluator ports can cancel after a final scalar projection even when their finite-rank packet is faithful.

## Frontier

Source-authorized cross-prime interaction has now been classified at the first assembly layer:

- local histories are label diagonal;
- common observer aggregation creates a finite-rank coherent mode;
- primitive composite labels require separate constructors.

The next quantitative theorem is the finite-rank loading bound

\[
U_\sigma^{*}U_\sigma
\le
(1-\delta)G_{\mathrm{diag}}
\]

uniformly on compact off-seam regions, followed by a distributional seam boundary theorem.
