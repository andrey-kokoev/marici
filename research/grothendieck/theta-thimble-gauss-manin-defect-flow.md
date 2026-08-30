# Gauss--Manin flow of the oriented thimble defect

## Flat relative cycles

Fix a Stokes chamber and let \(\Gamma_j(z)\) be one of its oriented thimbles.
Define logarithmic moments

\[
M_{j,k}(z)=
\int_{\Gamma_j(z)}(\log x)^k x^{z/2}G(x)\,\frac{dx}{x}.
\]

The endpoints are either decaying sectors or zeros of \(G\). Hence the
integrand vanishes at every relative endpoint. Because the thimble class is
Gauss--Manin flat inside the chamber, differentiation produces no endpoint
term.

For \(z=a+ib\),

\[
\boxed{
\partial_b M_{j,k}=\frac{i}{2}M_{j,k+1}.
}
\]

In particular, with

\[
I_j=M_{j,0},\qquad J_j=M_{j,1},\qquad K_j=M_{j,2},
\]

we have

\[
\partial_b I_j=\frac{i}{2}J_j,\qquad
\partial_b J_j=\frac{i}{2}K_j.
\]

This is exact within a chamber. It fails only at a Stokes wall, where the
oriented basis jumps.

## Ordered cone transport

Put

\[
T_{jk}=\Re\left(\lambda J_j\overline{I_k}\right),
\qquad
\lambda=\beta-i\alpha.
\]

Then

\[
\boxed{
\partial_bT_{jk}
=\Re\left[
\lambda'J_j\overline{I_k}
+\frac{i\lambda}{2}
\left(K_j\overline{I_k}-J_j\overline{J_k}\right)
\right].
}
\]

The proof is direct differentiation, using

\[
\partial_b\overline{I_k}
=-\frac{i}{2}\overline{J_k}.
\]

The two-thimble numerator is

\[
\mathcal N=T_{11}+T_{22}+T_{12}+T_{21}.
\]

Its derivative is therefore controlled by moments only through order two on
the same canonical cycles.

## Defect-ratio flow

Define

\[
A=T_{11},
\qquad
D=-(T_{22}+T_{12}+T_{21}),
\qquad
\delta=\frac DA.
\]

Where \(A>0\),

\[
\boxed{
\delta'=\frac{D'A-DA'}{A^2}.
}
\]

Thus the observed chamber monotonicity \(\delta'\leq0\) is equivalent to the
finite coupled moment inequality

\[
\boxed{D'A-DA'\leq0.}
\]

No contour derivatives, saddle velocities, or zero locations appear. The
source topology enters only by selecting the oriented thimble block; chamber
transport is then a closed moment calculation.

## Entry-layer strategy

The first chamber data suggest:

1. certify \(\delta<1\) on a short interval immediately above the first wall;
2. prove \(D'A-DA'\leq0\) for the remainder of the chamber; and
3. transport the entry margin to the third-saddle wall.

On the ray \(a=1/2\), sampled values decrease from \(0.4344\) at \(b=7\) to
\(0.2444\) at \(b=9.6\). The wall diagnostic near \(b=6.03\) has still larger
margin than required.

## Falsifier

The differential mechanism is killed by the first point in the proposed
monotonicity zone where

\[
D'A-DA'>0.
\]

If that occurs while \(\delta<1\), positivity may survive but monotone defect
transport does not. The mechanism must not be repaired by moving the start of
the zone after seeing the violation unless a new source-defined boundary is
identified.

## Status

The Gauss--Manin moment identities and quotient identity are exact. The sign
of \(D'A-DA'\) for the theta thimble block remains to be proved uniformly.
Exact-path evaluations at \(b=7,8,9,9.6\) are all negative, respectively
approximately `-0.1151`, `-0.0894`, `-0.0454`, and `-0.0129`.

Artifact:

- checkers/theta_thimble_gauss_manin_identity.py
- results/theta-thimble-gauss-manin-identity.json
