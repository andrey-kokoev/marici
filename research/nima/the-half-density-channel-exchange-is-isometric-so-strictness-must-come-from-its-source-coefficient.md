# The half-density channel exchange is isometric, so strictness must come from its source coefficient

## Canonical channel identification

The twisted graph spaces are defined by

\[
\mathcal H_-=U_-^{-1}\mathcal H_{\mathrm{rel}},
\qquad
\mathcal H_+=U_+^{-1}\mathcal H_{\mathrm{rel}}.
\]

There is a canonical exchange map

\[
Q
=
U_-^{-1}U_+:
\mathcal H_+\longrightarrow\mathcal H_-.
\]

In pointwise coordinates,

\[
(Qf)(u)=e^u f(u).
\]

By the pullback definitions,

\[
\|Qf\|_{\mathcal H_-}
=
\|f\|_{\mathcal H_+}.
\]

Thus \(Q\) is unitary between the two typed history fibers.

## Consequence for the odd coupling

If the bulk odd operator factors as

\[
J=\alpha Q,
\]

then its normalized relative norm is exactly

\[
\|S_-^{-1/2}JS_+^{-1/2}\|
=
|\alpha|.
\]

The auxiliary contraction theorem reduces to the scalar source condition

\[
|\alpha|<1.
\]

The channel geometry itself supplies no strictness: the unweighted exchange \(Q\) has norm one and would make the auxiliary form semidefinite at saturation.

## Candidate half-density coefficient

The completion factorization contains the fixed connection coefficient \(1/2\):

\[
\mathcal C
=
\left(\partial_u-\frac12\right)
\left(\partial_u+\frac12\right).
\]

The exact theta boundary columns also show a factor \(1/2\) between the even forcing port and the odd derivative port. These facts identify

\[
\alpha=\frac12
\]

as the smallest source-native candidate. If the source Green identity proves

\[
J=\frac12Q,
\]

then

\[
\delta_{\mathrm{aux}}
=
1-\|K\|
=
\frac12
\]

uniformly over labels and transported fibers.

## Authority warning

The shared numerical factor \(1/2\) is not yet a derivation of the bulk operator. Boundary compression and differential factorization constrain \(J\), but another operator may have the same trace compression.

The required identity is operator-valued:

\[
U_-JU_+^{-1}
=
\frac12 I
\]

on a common reduced history core, extended by closure. Only this proves that no dark bulk component is present.

## Reflection and labels

The canonical exchange \(Q\) intertwines valuation labels and transforms under reflection to its inverse channel exchange. Therefore \(\alpha Q\) has the correct structural typing once the causal sign is fixed.

## Next exact test

Derive the mixed Green form between the two first-order completion channels. If its conjugated cross term is exactly \(\frac12I\), the auxiliary contraction problem closes with margin \(1/2\). If it contains any residual operator \(R\),

\[
U_-JU_+^{-1}
=
\frac12I+R,
\]

then the real gate is the bound

\[
\left\|\frac12I+R\right\|<1.
\]

This is now the narrowest bulk calculation.
