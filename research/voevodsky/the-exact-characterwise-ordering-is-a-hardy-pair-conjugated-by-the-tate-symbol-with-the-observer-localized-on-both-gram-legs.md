# The exact characterwise ordering is a Hardy pair conjugated by the Tate symbol with the observer localized on both Gram legs

## Radial Mellin notation

Fix an angular character `chi`. Let

\[
\Pi
\]

be the Hardy projection corresponding to the logarithmic half-line `(-infinity,0]` after radial Fourier/Mellin transform. Let

\[
E_L=M_{e^{iLs}}
\]

encode translation of the cutoff boundary to `L=log Lambda`.

Then the physical cutoff is

\[
\boxed{
P_L
=E_L\Pi E_L^*.
}
\]

Let

\[
R f(s)=f(-s)
\]

be radial reflection. With the selected Hardy orientation,

\[
R\Pi R
=I-\Pi.
\]

The characterwise additive Fourier transform is the Tate scattering operator

\[
\boxed{
S_\chi
=M_{\gamma_\chi}R,
}
\]

where `|gamma_chi|=1` on the unitary axis.

## Fourier cutoff before recentering

The Fourier-conjugate cutoff is

\[
Q_L
=S_\chi P_LS_\chi^*.
\]

Using

\[
RE_L
=E_L^*R
\]

and `R Pi R=I-Pi`, obtain

\[
\boxed{
Q_L
=M_{\gamma_\chi}E_L^*
(I-\Pi)
E_LM_{\gamma_\chi}^*.
}
\]

This is the exact characterwise order before moving the physical boundary back to zero.

## Recentered pair of projections

Conjugate both cutoffs by `E_L*`. Then

\[
E_L^*P_LE_L
=\Pi.
\]

Since all scalar multipliers commute, define

\[
\boxed{
\sigma_{L,\chi}(s)
=
e^{-2iLs}
\gamma_\chi(s).
}
\]

The recentered Fourier cutoff is

\[
\boxed{
\widetilde Q_{L,\chi}
=M_{\sigma_{L,\chi}}
(I-\Pi)
M_{\sigma_{L,\chi}}^*.
}
\]

Changing the Fourier/reflection convention replaces `e^(-2iLs)` by `e^(2iLs)` and/or conjugates `gamma`; none of the norm estimates changes.

Thus the exact characterwise pair is

\[
\boxed{
P=\Pi,
\qquad
Q=M_\sigma(I-\Pi)M_\sigma^*.
}
\]

## Observer ordering

Convolution by the semilocal observer becomes multiplication by its Mellin transform:

\[
A_{g,\chi}
=M_{m_{g,\chi}}.
\]

For `h=g*g*`,

\[
H_{g,\chi}
=A_{g,\chi}A_{g,\chi}^*
=M_{|m_{g,\chi}|^2}.
\]

The positive and outside Gram legs are therefore exactly

\[
\boxed{
B_{L,\chi}(g)
=Q\PiM_m,
}
\]

\[
\boxed{
C_{L,\chi}(g)
=Q(I-\Pi)M_m,
}
\]

with the second physical/annular regulator inserted into `C` before removing its cutoff.

The observer multiplier is on the right of the Hardy projection. It must not be silently moved across `Pi`.

## Exact sewing pairing

At finite radial and angular regulators, the sewing entry is

\[
\boxed{
\mathcal E_{L,\chi}(g)
=
\langle
B_{L,\chi}(g),
C_{L,\chi}(g)
\rangle_{HS}.
}
\]

Equivalently,

\[
\boxed{
\mathcal E_{L,\chi}(g)
=
\operatorname{Tr}
\left(
M_m^*
\Pi Q(I-\Pi)
M_m
\right).
}
\]

This is the exact observer-localized ordering.

## Relation to the Tate Hankel block

Define

\[
H_\sigma
=
\Pi M_\sigma(I-\Pi).
\]

The off-diagonal cutoff block is

\[
\begin{aligned}
\Pi Q(I-\Pi)
&=
\Pi M_\sigma(I-\Pi)
M_\sigma^*(I-\Pi)\\
&=
H_\sigma
M_\sigma^*(I-\Pi).
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_{L,\chi}(g)
=
\operatorname{Tr}
\left(
M_m^*H_\sigma
M_\sigma^*(I-\Pi)M_m
\right).
}
\]

This identifies precisely where the Tate-symbol Hankel operator enters.

## Controlled observer reordering

Use

\[
(I-\Pi)M_m
=M_m(I-\Pi)-[\Pi,M_m].
\]

Then the sewing term splits exactly into

\[
\boxed{
\begin{aligned}
\mathcal E_{L,\chi}(g)
&=
\operatorname{Tr}
\left(
M_m^*H_\sigma
M_\sigma^*M_m(I-\Pi)
\right)\\
&\quad-
\operatorname{Tr}
\left(
M_m^*H_\sigma
M_\sigma^*[\Pi,M_m]
\right).
\end{aligned}
}
\]

The second term contains the observer Hardy commutator. For smooth rapidly decreasing `m`,

\[
[\Pi,M_m]
\in
\mathcal L^2
\]

with

\[
\|[\Pi,M_m]\|_{HS}^2
=c
\int|u||\widehat m(u)|^2du.
\]

It is therefore a controlled boundary correction.

## Localized Tate commutator

The Tate Hankel block is one corner of

\[
[\Pi,M_\sigma].
\]

Because the observer multiplier occurs on both Gram legs, the relevant estimates involve

\[
H_\sigma M_m,
\qquad
M_m^*H_\sigma,
\qquad
H_\sigma[\Pi,M_m].
\]

The previously proved bound for

\[
[\Pi,M_\sigma]M_m
\]

controls the first expression. Taking adjoints controls the second with the conjugate symbol. The third is a product of a localized/regulated Hankel block with a rapidly decaying Hilbert--Schmidt observer commutator.

Thus the ordering corrections introduce no new power of `L`; they alter only the observer seminorm constant and finite boundary term.

## Trace-ideal caveat

Without the second physical regulator, the outside leg can fail to be Hilbert--Schmidt. The characterwise formula is therefore first interpreted with:

- finite angular projection `K_N`;
- finite annular cutoff `P_R-P_Lambda`;
- observer multiplier `M_m`.

Only after obtaining bounds uniform in those regulators may one pass to the combined limit.

The displayed unregulated trace formulas are shorthand for that regulated limit.

## Characterwise logarithmic bound

Under the localized Hardy-commutator estimate and the observer-commutator bound, one obtains for the finite-regulator sewing entry

\[
\boxed{
|\mathcal E_{L,\chi}(g)|
\le
C_{g,N}
(1+|\chi|)^{-N}
(1+L)
}
\]

as a safe trace-norm bound. A Cauchy--Schwarz refinement may improve `1+L` to `sqrt(1+L)` when both localized legs admit the corresponding square bounds.

Summing over angular characters gives

\[
\boxed{
\sum_\chi
|\mathcal E_{L,\chi}(g)|
=O_g(1+L).
}
\]

This is sufficient for traceability and at-most-leading-order control. It does not yet show the sewing is `o(L)` or has a finite limit.

## What has been completed

The prior operator-order caveat is now resolved algebraically:

\[
\boxed{
P=\Pi,

Q=M_{e^{-2iLs}\gamma_\chi}
(I-\Pi)
M_{e^{-2iLs}\gamma_\chi}^*,

A_g=M_{m_{g,\chi}}.
}
\]

Every movement of `M_m` across a Hardy projection produces the explicit correction `[Pi,M_m]`.

## Remaining asymptotic gate

To prove equality of finite parts or positivity, one still needs more than the `O(L)` majorant. One must show one of:

1. cancellation of the linear term in the signed sewing pairing;
2. convergence of the recentered Tate--Hankel block against the observer boundary commutator;
3. identification of its limit with the endpoint--gamma completion.

This is now a scalar/fiberwise Hankel asymptotic rather than an operator-typing problem.

## Disposition

The exact characterwise ordering is

\[
\boxed{
\mathcal E_{L,\chi}(g)
=
\operatorname{Tr}
\left(
M_m^*
\Pi
M_\sigma(I-\Pi)M_\sigma^*
(I-\Pi)
M_m
\right),
}
\]

with

\[
\sigma=e^{-2iLs}\gamma_\chi.
\]

The observer-localized Hardy estimates apply after adding the explicit `[Pi,M_m]` correction. The remaining problem is the large-`L` limit of this fiberwise sewing pairing.
