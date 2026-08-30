# Two-copy label pairs have canonical hyperbolic centers

## Bounded question

Can the difference-coordinate transport in the first Laguerre form be derived
exactly from theta labels, leaving only one genuinely oscillatory variable?

## Labelled completed kernel

On the positive completed chart, the `n`-th contribution has the form

\[
 K_n(u)
 =\pi n^2e^{5u/2}
 \bigl(2\pi n^2e^{2u}-3\bigr)
 e^{-\pi n^2e^{2u}},
 \qquad u\ge0,
\]

up to the fixed overall convention from packet 107.  Every factor is positive
on this chart.

For a two-copy label pair `(n,m)`, set

\[
 S=u+v,
 \qquad D=u-v.
\]

Then

\[
 n^2e^{2u}=n^2e^{S+D},
 \qquad
 m^2e^{2v}=m^2e^{S-D}.
\]

## Arithmetic centering

Put

\[
 c_{nm}=\log(m/n),
 \qquad D=c_{nm}+\delta.
\]

The two scale energies become

\[
 n^2e^{S+D}=nm\,e^Se^\delta,
 \qquad
 m^2e^{S-D}=nm\,e^Se^{-\delta}.
\]

Therefore their exponential sum is

\[
 \boxed{
 n^2e^{S+D}+m^2e^{S-D}
 =2nm\,e^S\cosh\delta.}
\]

The product of completion polynomials is also symmetric:

\[
 (2\pi qe^\delta-3)(2\pi qe^{-\delta}-3),
 \qquad q=nm\,e^S,
\]

and all remaining product factors depend only on `S` and `nm`.  Hence the
full pair density `K_n(u)K_m(v)` is an even function of `delta`.

## Label swap and the moving-endpoint obstruction

The first Laguerre source carries the weight

\[
 D^2=(\delta+c_{nm})^2.
\]

Algebraically, swapping the labels replaces `c_nm` by `-c_nm`. On an
untruncated centered fiber the two formal weights would combine as

\[
 (\delta+c_{nm})^2+(\delta-c_{nm})^2
 =2(\delta^2+c_{nm}^2)>0.
\]

On the positive chart, however, `u,v>=0` imposes `-S<=D<=S`, so the centered
interval is `-S-c_nm<=delta<=S-c_nm` and is generally not reflection-
invariant. Label swap is accompanied by `D -> -D`; it preserves `D^2` rather
than supplying an independent centered weight at the same point. The odd
cross term therefore cannot be discarded before reciprocal-chart sewing.

The durable result is that the bulk density has an exact arithmetic center,
while all failure of centered cancellation is supported at the moving chart
endpoints.

## Exact reduction of the obstruction

After full reciprocal-chart sewing, the first Laguerre form becomes a Fourier
transform in the sum coordinate:

\[
 \mathcal L_1[X](x)
 =\int_{\mathbb R}e^{ixS}\,d\mu_{\rm ar}(S),
\]

where `mu_ar` contains the centered hyperbolic bulk together with the moving-
endpoint terms. Positivity of the full separation measure is the universal
squared-separation theorem already known; this packet does not prove separate
positivity of the truncated one-chart pieces.

This refines the separation measure with substantially more structure: every
conditional `D` fiber has a canonical arithmetic center, while the exact
failure of local reflection is a typed modular-boundary contribution.

## Explanation

The 45-degree rotation from `(u,v)` to `(S,D)` separates two roles:

\[
 \boxed{
 \begin{array}{c|c}
 D&\text{arithmetic ratio, hyperbolic centering, moving endpoint}\\
 S&\text{global scale, Fourier phase, unresolved orientation}
 \end{array}}
\]

The apparent destructive interference is not between arbitrary planes. The
interior difference density is symmetrized by reciprocal label geometry, but
its truncated endpoints are not. A proof must control both that modular seam
and the subsequent global sum-scale phase.

## Next gate

The immediate question is whether reciprocal modular sewing cancels or
positively repairs the explicit endpoint mismatch. Only then may one ask
whether `mu_ar(S)` has a stronger positive-definite or variation-diminishing
structure forcing its Fourier transform to remain nonnegative.

The smallest falsifier is a completed, label-preserving pair packet whose
conditional bulk has the exact hyperbolic center above but whose sewn endpoint
term has the wrong sign. Such a packet would close the proposed local repair
before any global Fourier test.
