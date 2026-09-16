# The labelled Kothe incidence globalizes the source-forced mixed channel before scalar prime pushforward

## Labelled source

Let

\[
\mathcal M=\{(p,k):p\text{ prime},\ k\ge1\},
\qquad
a_{p,k}=\frac1k p^{-k/2}.
\]

Use the projective exponential Kothe source

\[
\mathcal A_{exp}
=
\bigcap_{\delta>0}
\ell^1(\mathcal M,e^{\delta k\log p}).
\]

Finite labelled packets are dense and cutoff truncations converge in every
seminorm.

## Global tail and seam synthesis

For each label \(m=(p,k)\), let \(G_m\) and \(H_m\) be the translated copies of
the common theta Hankel and seam maps. Translation preserves their operator
norms. Define the labelled maps

\[
\mathbf Gc=(a_mc_mG_m)_m,
\qquad
\mathbf Hc=(a_mc_mH_m)_m
\]

in the corresponding direct-sum operator ideals.

Because

\[
|a_{p,k}|\le p^{-k/2}
\]

and every exponential Kothe seminorm dominates this weight, the maps are
continuous on \(\mathcal A_{exp}\). On each fixed Hilbert rung,

\[
\mathbf G\in\mathcal S_2,
\qquad
\mathbf H\in\mathcal B,
\]

with the connected \(k\ge3\) return nuclear by the already established absolute
prime-power estimate.

## Mixed global channel

Their shared labelled source forces

\[
\boxed{
\mathbf K_{ts}=\mathbf G\mathbf H^*,
\qquad
\mathbf K_{st}=\mathbf H\mathbf G^*.}
\]

The ideal property gives

\[
\|\mathbf K_{ts}\|_2
\le
\|\mathbf G\|_2\|\mathbf H\|,
\]

and similarly for \(\mathbf K_{st}\). Hence both global mixed channels are
Hilbert--Schmidt on every admitted fixed rung.

The symmetric and oriented geometric-algebra components

\[
\mathbf K_{sym}
=\frac12(\mathbf K_{ts}+\mathbf K_{st}),
\]

\[
\mathbf K_{or}
=\frac1{2i}(\mathbf K_{ts}-\mathbf K_{st})
\]

are therefore well-defined and continuous.

## Prime diagonality

The source retains the label projections \(P_m\). Since both realizations are
label diagonal,

\[
P_n\mathbf G P_m=\delta_{mn}\mathbf G_m,
\qquad
P_n\mathbf H P_m=\delta_{mn}\mathbf H_m.
\]

Consequently

\[
P_n\mathbf K_{ts}P_m
=
\delta_{mn}\mathbf G_m\mathbf H_m^*.
\]

Thus no cross-prime coupling is manufactured before the declared scalar
pushforward. Any later cross-prime term must come from a separately typed
codiagonal or completed observer, not from the local Green construction.

## Arity-two continuity

The polarized coefficient map

\[
(c,d)
\longmapsto
\mathbf G(c)\mathbf H(d)^*
\]

obeys a projective bound

\[
\|\mathbf G(c)\mathbf H(d)^*\|_2
\le
C_{\delta}
q_\delta(c)q_\delta(d).
\]

Therefore it descends to a continuous linear map on the completed projective
symmetric two-copy source

\[
\operatorname{Sym}^2_\pi\mathcal A_{exp}.
\]

This is exactly the arity required by the primitive-square crossing; no
quadratic map is falsely treated as linear on one source copy.

## Cutoff naturality

Label truncations commute with both synthesis maps. Their mixed products
therefore converge in Hilbert--Schmidt norm on each fixed rung, while the
connected return converges in nuclear norm. The arity-two mixed channel is
cutoff-natural before scalar prime summation.

## Result and remaining boundary

The source-forced tail--seam mixed channel now has a global labelled,
arity-two, cutoff-natural realization. What remains outside this theorem is:

1. the archimedean gamma row;
2. the completed endpoint vertical sector;
3. the final scalar/observer pushforward that mixes labels;
4. identification of the resulting complete arity-two functional with the
   Weil kernel.

No positivity claim is used or obtained in this globalization.
