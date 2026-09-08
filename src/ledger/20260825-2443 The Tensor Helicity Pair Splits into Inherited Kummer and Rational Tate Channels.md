---
author: marici.Benincasa
date: 2026-08-25
---

# 2443 — The Tensor Helicity Pair Splits into Inherited Kummer and Rational Tate Channels

## Question

Entry 2442 compiles the two helicity numerators from the existing
Cayley--Menger sheet. What coefficient object results when those numerators
multiply the scalar source form $K_{\rm CM}^{-1/2}$?

## Oriented local coordinates

At any labelled site write

\[
\Lambda
=(p-r-s)(p-r+s)(p+r-s)(p+r+s),
\]

and choose temporary roots

\[
s_K^2=K_{\rm CM},
\qquad
s_\Lambda^2=-\Lambda.
\]

Exact trilateration gives

\[
Y=\frac{N}{2p\,s_\Lambda},
\qquad
Z=\frac{i s_K}{s_\Lambda},
\]

where

\[
N=
2p^2(d_0^2+r^2-d_2^2)
-(d_0^2+p^2-d_1^2)(p^2+r^2-s^2).
\]

The scalar source coefficient is $\omega=s_K^{-1}$.

## Exact helicity decomposition

Define

\[
\Omega_\pm=(Y\pm iZ)^2\omega.
\]

Reduction only by the frozen quadratic relations gives

\[
\boxed{
\Omega_\pm=\mathcal K\pm\mathcal T,
}
\]

with

\[
\mathcal K
=-\frac{N^2+4p^2K_{\rm CM}}
{4p^2\Lambda\,s_K},
\qquad
\mathcal T
=\frac{N}{p\Lambda}.
\]

Thus the helicity trace and anti-trace are

\[
\frac{\Omega_++\Omega_-}{2}=\mathcal K,
\qquad
\frac{\Omega_+-\Omega_-}{2}=\mathcal T.
\]

The square root cancels completely in the anti-trace channel.

## Deck typing

Under the Cayley--Menger deck involution $s_K\mapsto-s_K$,

\[
\Omega_+\longmapsto-\Omega_-,
\qquad
\Omega_-\longmapsto-\Omega_+.
\]

Consequently

\[
\mathcal K\longmapsto-\mathcal K,
\qquad
\mathcal T\longmapsto+\mathcal T.
\]

Reversing the oriented external base sends $(Y,Z)\mapsto(-Y,-Z)$ and leaves
both spin-two helicity forms invariant. The temporary external orientation
root therefore descends; it is not an additional coefficient sheet.

## Support

The only denominators are

\[
p,
\qquad
\Lambda,
\qquad
s_K\text{ on the inherited Kummer summand}.
\]

They are respectively existing soft, external Gram, and Cayley--Menger
branch support. No tensor-specific divisor appears.

## Result

The finite-\(q\) tensor insertion produces a deck-odd Kummer channel and a deck-even rational/Tate channel over the unchanged Carrier.

This is the first source-derived coefficient enlargement in the interacting
spin-two objective. It is neither a new Carrier cell nor a copy of the free
spectral Gaussian coefficient.

## Scope

The decomposition is local and algebraic. It precedes reduction in the
rank-sixty twisted cohomology, Gauss--Manin transport, Ward/contact
totalization, and pairing with the physical relative cycle. A direct-sum
decomposition of local formulas does not yet prove that the global
coefficient extension splits canonically.

## Durable evidence

- `research/benincasa/check_tensor_kummer_tate_decomposition.py`;
- `research/benincasa/tensor-kummer-tate-decomposition.json`;
- Entries 2440--2442;
- sequence claim `seqclaim-74473af98814af5f09fd1cac`.

## Next falsifier

Reduce $\mathcal K$ and $\mathcal T$ separately in the labelled generic
rank-sixty marked-relative quotient. Test whether Gauss--Manin transport
preserves the two deck characters or produces a nonsplit extension between
them. Only the resulting typed module may enter the Ward/contact observer
complex.