# The two unitary identifications of the semilocal Jacobi measure have relative scattering operator equal to the Euler phase

## Spectral measures

Let `S` be a finite set of places containing infinity. In the canonical Hardy--Titchmarsh realization of Connes--Consani--Moscovici, the scaling generator is multiplication by `s` on

\[
H_S=L^2(\mathbb R,dm_S),
\]

where

\[
dm_S(s)
=
|E_S^-(s)|^2ds,
\qquad
E_S^-(s)=
\prod_{v\in S}
L_v(1/2-is).
\]

For the archimedean stage,

\[
dm_\infty(s)
=
|E_\infty^-(s)|^2ds.
\]

Put

\[
F_S^-(s)=
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2-is).
\]

Then

\[
\boxed{
dm_S=|F_S^-|^2dm_\infty.}
\]

## First unitary identification

Define

\[
\Omega_S^-:
H_\infty	o H_S,
\qquad
(\Omega_S^-f)(s)
=(F_S^-(s))^{-1}f(s).
\]

Then

\[
\|\Omega_S^-f\|_{H_S}^2
=
\int
|F_S^-|^{-2}|f|^2
|F_S^-|^2dm_\infty
=
\|f\|_{H_\infty}^2.
\]

Thus `Omega_S^-` is unitary.

Because it is a scalar multiplier, it intertwines the canonical scaling operators:

\[
\boxed{
M_s\Omega_S^-
=
\Omega_S^-M_s.
}
\]

## Reciprocal unitary identification

On the real line define

\[
F_S^+(s)=
\overline{F_S^-(s)}
=
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is).
\]

Since

\[
|F_S^+|=|F_S^-|,
\]

the map

\[
\Omega_S^+:
H_\infty	o H_S,
\qquad
(\Omega_S^+f)(s)
=(F_S^+(s))^{-1}f(s)
\]

is also unitary and also intertwines multiplication by `s`.

These are the two stationary identifications supplied by the canonical and dual Euler orientations.

## Relative scattering operator

Define the relative operator on the archimedean spectral space

\[
\mathscr S_S
=(\Omega_S^+)^*\Omega_S^-.
\]

For multiplication unitaries between the weighted spaces, direct calculation gives

\[
\boxed{
(\mathscr S_Sf)(s)
=
\frac{F_S^+(s)}
     {F_S^-(s)}
f(s)
}
\]

or its reciprocal depending on the order of `Omega_plus` and `Omega_minus`.

With the displayed order,

\[
\mathscr S_S(s)
=
\prod_{p\in S}
\frac{L_p(1/2+is)}
     {L_p(1/2-is)}.
\]

Therefore

\[
\boxed{
\mathscr S_S
=M_{J_S^{-1}},
}
\]

where

\[
J_S(s)=
\prod_{p\in S}
\frac{L_p(1/2-is)}
     {L_p(1/2+is)}.
\]

The complete Euler scattering phase is exactly the relative unitary between the two source-derived semilocal identifications.

## Logarithmic derivative

Since `mathscr S_S` is unitary,

\[
\frac1{2i}
\mathscr S_S^{-1}
\partial_s\mathscr S_S
\]

is a real self-adjoint multiplication operator. It is

\[
-V_S
\]

for the displayed orientation. Thus the finite-prime Weil current is the infinitesimal relative phase of the two Hilbertian identifications.

This derives the stationary scattering identity without invoking a determinant or RH.

## Prime transition

Adjoining prime `q` gives

\[
F_{S\cup\{q\}}^\pm
=F_S^\pm
L_q(1/2\pm is),
\]

and therefore

\[
\boxed{
\mathscr S_{S\cup\{q\}}
=
\mathscr S_S\mathscr S_q.
}
\]

All transitions commute. This is the exact scattering version of the prime/contraprime tower.

## Jacobi realization

The cyclic-pair construction represents multiplication by `s` in an orthonormal-polynomial basis as a Hermitian Jacobi matrix. Let

\[
\mathcal J_\infty,
\qquad
\mathcal J_S
\]

be the archimedean and semilocal Jacobi realizations. Transporting `Omega_S^plus-or-minus` through their orthogonal-polynomial transforms produces two unitaries

\[
W_S^\pm:
\ell^2(\mathbb N_0)	o
\ell^2(\mathbb N_0)
\]

satisfying

\[
\mathcal J_S W_S^\pm
=
W_S^\pm\mathcal J_\infty.
\]

Their relative unitary has spectral representation `J_S^(plus-or-minus 1)`. Thus an exact stationary scattering system exists for the semilocal **scaling/Jacobi operators**.

## Why this is not yet the prolate determinant identity

The semilocal prolate candidate is

\[
W_{\lambda,S}
=(H+\tfrac12)^2
+2\lambda^2N_S,
\]

where `N_S` is the grading operator determined by the `S`-dependent orthogonal polynomials.

Connes--Consani--Moscovici explicitly note that the semilocal Hilbert map does not intertwine the Hermite grading:

\[
N_S\Sigma_S
\ne
\Sigma_S N_\infty
\]

unless `S={infinity}`. The coefficients of the general semilocal Jacobi matrix are deferred to future work.

Therefore the exact intertwining of multiplication by `s` does not extend to the prolate operator. In particular, it does not prove

\[
\det_{rel}
\mathcal S_{prolate,S}
=J_S.
\]

## Determinant audit

The relative scattering operator `mathscr S_S` is multiplication by a nonconstant unimodular function on a continuous spectral space. It is not generally of determinant class relative to the identity:

\[
\mathscr S_S-I
\notin
\mathcal L^1.
\]

Hence an ordinary Fredholm determinant

\[
\det(\mathscr S_S)
\]

is not defined. The meaningful invariant is its pointwise scattering determinant/phase or a regularized trace per unit volume.

This matches the semifinite Plancherel framework found previously.

## Relation to the Weil trace

The source now supplies the chain

\[
\boxed{
\text{dual/canonical semilocal unitaries}
\Longrightarrow
\mathscr S_S=J_S^{-1}
\Longrightarrow
\frac1{2i}
\mathscr S_S^{-1}
\mathscr S_S'
=-V_S.
}
\]

Connes's trace theorem independently identifies `V_S`, after observer pairing and principal-value normalization, with the finite-place Weil functional.

What is missing is an operator theorem equating this stationary scattering phase with the boundary scattering of the positive prolate/Halmos dilation.

## Disposition

The Euler phase already has an exact source-derived scattering realization:

\[
\boxed{
\mathscr S_S
=(\Omega_S^+)^*\Omega_S^-
=M_{J_S^{-1}}.
}
\]

This realizes prime and contraprime towers as two unitary wave identifications of the same scaling spectrum. It is unconditional and coherent under adding places.

But it applies to the scaling/Jacobi operators, not the semilocal prolate operators whose positive/negative spectral decomposition is supposed to supply Weil positivity. Constructing the intertwiner between these two scattering systems remains the precise missing bridge.
