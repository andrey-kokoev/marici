# The placewise phase energy dominates the product-phase difference feature

## Product phase

Let

\[
S
=
\{v_1,
\ldots,
v_r\}
\]

and let

\[
\Gamma_S(t)
=
\prod_{k=1}^{r}
\gamma_{v_k}(t),
\]

where every local phase is unimodular:

\[
|\gamma_{v_k}(t)|=1.
\]

Define the product-phase energy density

\[
\boxed{
\kappa_{\Gamma_S}(t)
=
\frac1{4\pi^2}
\int
\frac{
|\Gamma_S(s)-
\Gamma_S(t)|^2
}{|s-t|^2}ds.
}
\]

For each place, define `kappa_(gamma_v)` analogously.

## Telescoping the phase difference

The scalar product difference has the exact expansion

\[
\boxed{
\begin{aligned}
\Gamma_S(s)-
\Gamma_S(t)
&=
\sum_{k=1}^{r}
\left(
\prod_{j<k}
\gamma_{v_j}(s)
\right)\\
&\qquad\cdot
(\gamma_{v_k}(s)-
\gamma_{v_k}(t))
\left(
\prod_{j>k}
\gamma_{v_j}(t)
\right).
\end{aligned}
}
\]

Every product multiplying the local difference has modulus one. Therefore

\[
|\Gamma_S(s)-
\Gamma_S(t)|
\le
\sum_{k=1}^{r}
|\gamma_{v_k}(s)-
\gamma_{v_k}(t)|.
\]

By finite Cauchy--Schwarz,

\[
\boxed{
|\Gamma_S(s)-
\Gamma_S(t)|^2
\le
r
\sum_{v\in S}
|\gamma_v(s)-
\gamma_v(t)|^2.
}
\]

## Pointwise energy domination

Divide by `|s-t|^2`, integrate in `s`, and retain the common normalization. This gives

\[
\boxed{
\kappa_{\Gamma_S}(t)
\le
|S|
\sum_{v\in S}
\kappa_{\gamma_v}(t).
}
\]

The inequality is pointwise in the Mellin spectral variable and character sector.

## Observer Gram domination

Let `D_S^(prod)` be the Hadamard difference row for the single product phase `Gamma_S`, and let `D_S^(loc)` be the orthogonal direct sum of the placewise telescoping difference rows.

Their observer Grams are

\[
\|D_S^{prod}M_m\|_2^2
=
\frac12
\int
\kappa_{\Gamma_S}(t)
|m(t)|^2dt,
\]

\[
\|D_S^{loc}M_m\|_2^2
=
\frac12
\sum_{v\in S}
\int
\kappa_{\gamma_v}(t)
|m(t)|^2dt.
\]

Hence

\[
\boxed{
\|D_S^{prod}M_m\|_2^2
\le
|S|
\|D_S^{loc}M_m\|_2^2.
}
\]

Polarization gives source-form domination

\[
\boxed{
G_S^{prod}
\preceq
|S|G_S^{loc}.
}
\]

## Douglas comparison

By Douglas factorization, there is a bounded source-label-preserving map

\[
\boxed{
T_S:
\overline{
\operatorname{ran}D_S^{loc}
}
\longrightarrow
\overline{
\operatorname{ran}D_S^{prod}
}
}
\]

such that

\[
\boxed{
T_S
D_S^{loc}M_m
=
D_S^{prod}M_m
}
\]

for every admitted observer, and

\[
\boxed{
\|T_S\|
\le
\sqrt{|S|}.
}
\]

Thus the local direct-sum completion canonically dominates the economical product-phase difference feature.

## Kernel inclusion

The Gram domination implies

\[
\boxed{
\ker D_S^{loc}
\subseteq
\ker D_S^{prod}.
}
\]

If every local phase deformation is invisible to an observer, then their product deformation is also invisible.

The converse can fail because local phase differences can cancel in the product.

## Cancellation example

If

\[
\gamma_{v_2}
=
\gamma_{v_1}^{-1},
\]

then

\[
\Gamma_{\{v_1,v_2\}}
=1
\]

and

\[
\kappa_\Gamma
=0.
\]

But generally

\[
\kappa_{\gamma_{v_1}}
+
\kappa_{\gamma_{v_2}}
>0.
\]

Thus no reverse domination by the product-phase energy can hold without a noncancellation hypothesis.

The local feature intentionally retains this canceled positive energy so that place contributions remain separately observable.

## Improvement under orthogonality

The factor `|S|` comes from scalar Cauchy--Schwarz. If the local phase-difference rows are orthogonal in an enlarged place-labelled carrier, their direct-sum norm already contains no cross terms, but the map summing them into the product row still has norm at most `sqrt(|S|)`.

A better constant requires structural cancellation/orthogonality in the target product kernel and is not automatic.

## Place enlargement bound

For

\[
S'
=S\cup\{v\},
\]

\[
\kappa_{\Gamma_{S'}}
\le
(|S|+1)
\left(
\sum_{u\in S}
\kappa_{\gamma_u}
+
\kappa_{\gamma_v}
\right).
\]

The local graph norm enlarges by one positive summand. The comparison constant grows at most as `sqrt(|S|+1)`.

Thus finite semilocal place enlargement remains bounded, though no uniform constant over arbitrarily large place sets follows from this estimate.

## Signed readout compatibility

Both presentations have the same signed projection difference:

\[
\boxed{
Q_{\Gamma_S}-\Pi
=
\sum_{k=1}^{r}
(Q_k-Q_{k-1}).
}
\]

The Douglas map compares their positive difference norms; signed readout equality follows independently from exact telescoping.

Therefore `T_S` forgets only place-resolved positive energy, not the total Tate boundary current.

## Graph-domain inclusion

The pointwise estimate implies continuous inclusion

\[
\boxed{
\mathcal D_{loc,S}
\hookrightarrow
\mathcal D_{prod,S},
}
\]

where

\[
\mathcal D_{prod,S}
=L^2(1+\kappa_{\Gamma_S})
\]

and

\[
\mathcal D_{loc,S}
=L^2
\left(
1+
\sum_{v\in S}
\kappa_{\gamma_v}
\right).
\]

The local-energy completion is stronger and maps boundedly to the product-energy completion.

## Relation to conductor control

For ramified phases,

\[
\kappa_{\gamma_v}
=
\frac{
f(\chi_v)
\log q_v
}{2\pi}.
\]

Therefore the local norm controls total conductor additively even if conductor phase slopes cancel in `Gamma_S`.

This is why the local completion supports strict place transitions while the product-phase completion may lose coercivity.

## Categorical interpretation

The placewise feature is a resolved presentation. The product-phase feature is its bounded quotient/compression under `T_S`.

Symbolically,

\[
\boxed{
\text{place-resolved positive boundary}
\xrightarrow[\|T_S\|\le\sqrt{|S|}]{T_S}
\text{product-phase positive boundary}.
}
\]

Both carry the same signed `C_34` observation.

## Disposition

For every finite semilocal set,

\[
\boxed{
\kappa_{\prod_v\gamma_v}
\le
|S|
\sum_{v\in S}
\kappa_{\gamma_v}.
}
\]

Hence the placewise local-energy graph domain continuously controls the original product-phase difference row, with Douglas norm at most `sqrt(|S|)`. The local completion is the stronger coherent positive realization; the product phase is its bounded place-forgetting image.
