# Characterwise semilocal Fourier is Tate scattering and reduces prolate transition growth to a Hankel symbol estimate

## Angular decomposition

Let

\[
C_S
\simeq
C_S^1\rtimes\mathbb R
\]

measurably along the logarithmic module coordinate, and decompose

\[
L^2(C_S)
\simeq
\bigoplus_{
\chi\in\widehat{C_S^1}}
L^2(\mathbb R_s).
\]

Here `s` is the Mellin dual of

\[
t=
\log|c|_S.
\]

The precise decomposition may be a direct integral if the norm-one quotient has a continuous component; the formulas below are fiberwise.

## Tate scattering form of additive Fourier transform

The local functional equation says that additive Fourier transform, after multiplicative Mellin transform, acts on the `chi` fiber as

\[
\boxed{
(\mathscr F_{S,\chi}f)(s)
=
\gamma_S(\chi,s)
f(-s),
}
\]

where

\[
\gamma_S(\chi,s)
=
\prod_{v\in S}
\gamma_v(\chi_v,\tfrac12+is,\psi_v)
\]

is the completed semilocal Tate gamma factor in the unitary normalization.

On the critical line,

\[
|\gamma_S(\chi,s)|=1
\]

for unitary `chi`, after pairing each factor with the source dual convention.

Thus `mathscr F_(S,chi)` is reflection followed by multiplication by a unimodular scattering symbol.

## Half-line projection and Hardy projection

In the logarithmic physical variable, the one-sided module cutoff is

\[
P_L
=1_{(-\infty,L]}.
\]

Translation by `L` reduces it to `P_0`. Under radial Fourier/Mellin transform, `P_0` is represented by a Hardy projection `Pi_-` with the chosen sign convention.

Translation contributes the phase

\[
e^{iLs}.
\]

Consequently the pair `(P_L,Q_L)` on one angular fiber is unitarily equivalent to a pair of Hardy projections whose relative symbol has the form

\[
\boxed{
\sigma_{L,\chi}(s)
=
e^{2iLs}
\gamma_S(\chi,s).
}
\]

The factor `2L` records the physical/Fourier reversal of radial translation. Exact signs depend on whether `Pi_plus` or `Pi_minus` represents `(-infinity,0]`.

## Off-diagonal block as a Hankel operator

Let

\[
H_{\sigma}
=
(I-\Pi_-)
M_\sigma
\Pi_-.
\]

After the characterwise unitary identifications, the prolate transition block is a Hankel operator of this type:

\[
\boxed{
P_LQ_L(I-P_L)
\simeq
H_{\sigma_{L,\chi}}
}
\]

up to reflection and adjoint orientation.

Therefore

\[
\boxed{
\mathfrak p_{L,S}(\chi)
=
\|H_{\sigma_{L,\chi}}\|_{HS}^2
}
\]

when the Hankel operator is Hilbert--Schmidt.

## Hankel Hilbert--Schmidt criterion

For a sufficiently regular scalar symbol `sigma`, the Hankel Hilbert--Schmidt norm is its homogeneous `H^(1/2)`/Besov seminorm:

\[
\boxed{
\|H_\sigma\|_{HS}^2
=
c
\int_\mathbb R
|u|
|\widehat\sigma(u)|^2du
}
\]

or equivalently

\[
\boxed{
\|H_\sigma\|_{HS}^2
=c'
\iint_{\mathbb R^2}
\frac{
|\sigma(s)-\sigma(t)|^2
}{|s-t|^2}dsdt,
}
\]

with constants depending on Fourier convention and with the appropriate one-sided Fourier component for a Hankel rather than full commutator norm.

This converts the semilocal transition problem into a gamma-symbol regularity estimate.

## Why the raw exponential phase needs localization

The symbol

\[
e^{2iLs}
\]

alone is not in homogeneous `H^(1/2)(R)` globally. Its Hankel block represents the growing cutoff transition and must be interpreted with the actual finite phase-space/localized radial carrier.

Therefore one cannot insert `sigma_(L,chi)` into the global double-integral formula without regularization. The correct estimate is localized by the observer or by the finite radial cutoff packet.

This reproduces the earlier conclusion: the bare semilocal transition may fail to be trace class, while the observer-weighted Hankel pairing is meaningful.

## Observer-weighted Hankel target

Let `m_(g,chi)(s)` be the angular Mellin multiplier of the observer. Smooth compact support in `C_S` gives rapid decay of `m` and its derivatives in both `s` and `chi`.

The typed characterwise transition is

\[
\boxed{
H_{\sigma_{L,\chi}}
M_{m_{g,\chi}}
}
\]

or the corresponding two-sided polarized product. Its Hilbert--Schmidt norm is finite under standard symbol estimates.

The desired bound becomes

\[
\boxed{
\|H_{\sigma_{L,\chi}}
M_{m_{g,\chi}}\|_{HS}^2
\le
C_{g,N}
(1+|\chi|)^{-N}
(1+L),
}
\]

for every `N`, after using observer decay to dominate polynomial gamma-factor growth.

Summing over `chi` then gives the full observer-weighted semilocal estimate.

## Gamma-factor derivative estimates

At an archimedean place, logarithmic derivatives of the gamma factor are combinations of digamma/polygamma functions. Stirling estimates give, on vertical lines,

\[
\partial_s^j
\log\gamma_v(\chi_v,s)
=
O_j
\left(
(1+|s|+|\chi_v|)^{1-j}
\right)
\]

with logarithmic interpretation at `j=1`, according to normalization.

At a finite place, the gamma factor is a monomial conductor term times a rational function of `p^(-is)`. Derivatives are bounded polynomially in conductor and local angular frequency on compact `s` packets.

Thus for every fixed derivative order there is a polynomial bound

\[
\boxed{
|\partial_s^j
\gamma_S(\chi,s)|
\le
C_{S,j}
(1+|s|+|\chi|)^{d_j}.
}
\]

Combined with rapid observer decay, this is sufficient for angular summability. Establishing the exact `L` dependence still requires the localized Hankel calculation.

## Source of the logarithm

The logarithmic factor `1+L` is not expected from gamma growth. It comes from the length of the prolate transition window generated by the phase `e^(2iLs)`.

The gamma symbol perturbs the transition by a scattering phase whose derivatives grow at most polynomially in `chi`. Therefore the target separates naturally:

\[
\boxed{
\text{radial prolate logarithm}
\times
\text{polynomial gamma conductor growth}
\times
\text{rapid observer decay}.
}
\]

## Exact remaining lemma

Choose an observer-localized Hankel norm `||-||_(H_g)` matching the two-cutoff trace ideal. Prove

\[
\boxed{
\|H_{e^{2iLs}\gamma_S(\chi,s)}}
M_{m_{g,\chi}}
\|_{HS}^2
\le
C_{S,M}
(1+L)
(1+|\chi|)^d
p_M(g)^2,
}
\]

where `p_M` is a fixed Schwartz seminorm independent of `L` and `chi`.

Then angular Fourier decay of `g` permits choosing `M` so the character sum converges.

## Typing limitations

This packet assumes the characterwise Tate decomposition and records the operator form it forces. To turn it into a theorem for `X_S`, one must verify:

1. the exact unitary Mellin decomposition of the conull quotient carrier;
2. the local gamma-factor normalization for the chosen basic character;
3. the Hardy projection convention for the one-sided module cutoff;
4. the relation between the finite `(Lambda,R)` regulator and the localized Hankel norm;
5. trace-ideal convergence after summing angular fibers.

No equality with the completed Weil form is claimed here.

## Disposition

The characterwise semilocal transition is a Tate-scattering Hankel problem:

\[
\boxed{
P_\Lambda Q_\Lambda(I-P_\Lambda)
\quad\leadsto\quad
H_{e^{2iL s}\gamma_S(\chi,s)}.
}
\]

The sought polynomial angular estimate follows from a localized `H^(1/2)` bound for this symbol together with standard polynomial gamma-factor derivative estimates. The remaining analytic core is the observer-localized Hankel inequality uniform in `L` and `chi`.
