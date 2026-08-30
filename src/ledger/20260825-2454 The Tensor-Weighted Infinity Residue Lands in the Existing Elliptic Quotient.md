---
author: marici.Benincasa
date: 2026-08-25
---

# 2454 — The Tensor-Weighted Infinity Residue Lands in the Existing Elliptic Quotient

## Question

The tensor multiplier grows quartically at infinity, so ordinary residue
naturality does not apply without a filtered reduction.  Does its logarithmic
boundary class require a new elliptic coefficient object?

Sequence claim: `seqclaim-7603cae9c695254a6b379c12`.

## Frozen infinity chart

On the (q_{\mathcal G_{12}})-residue surface use

\[
b=s^{-1},\qquad a=t/s,\qquad c=-E.
\]

The compactified Cayley--Menger equation is

\[
W^2=F(t)+s^2G(t)+s^4H,
\]

with

\[
F(t)=x^2t^4-(x^2+y^2-z^2)t^2+y^2.
\]

The tensor multiplier has the exact expansion

\[
Q^{\rm even}=s^{-4}q_4(t)+s^{-2}q_2(t)+q_0(t).
\]

## Logarithmic coefficient

Expanding

\[
Q^{\rm even}\frac{ds}{s}\wedge
\frac{dt}{\sqrt{F+s^2G+s^4H}}
\]

and removing the higher normal poles leaves

\[
\frac{
q_0F^2-\frac12q_2GF
+q_4\left(-\frac12HF+\frac38G^2\right)
}{F^{5/2}},dt.
\]

An exact Hermite reduction gives

\[
\boxed{
\frac{\mathrm{Num}}{F^{5/2}}dt
\equiv
(c_0+c_2t^2)\frac{dt}{\sqrt F}.
}
\]

The checker constructs the unique odd polynomial (R) of degree at most nine
such that the difference is

\[
d\!\left(\frac{R}{F^{3/2}}\right).
\]

Thus the tensor-weighted boundary class lies explicitly in

\[
H^1(D_\infty)
=\langle\omega_0,\omega_2\rangle,
\qquad
\omega_0=\frac{dt}{W},\quad
\omega_2=\frac{t^2dt}{W}.
\]

## Support audit

The complete reduced denominators are

\[
\operatorname{den}(c_0)=32x^2y^2\Lambda(x,y,z),
\]

\[
\operatorname{den}(c_2)=16y^4\Lambda(x,y,z).
\]

After the physical specialization (E=x+y+z), these denominators are
unchanged.  They lie entirely on the frozen soft and signed-energy/triangle
Gram arrangement.  Both coefficients are generically nonzero.

## Result

\[
\boxed{
R_\infty(Q^{\rm even}\Omega_7)
=c_0\omega_0+c_2\omega_2
\in\mathbb V_{\rm ell}(-1).
}
\]

The quartic tensor growth changes the filtered representative but creates
neither a new elliptic block nor a new support divisor.

## Classification

- target: existing rank-two elliptic Gauss--Manin quotient;
- new coefficient rank: zero;
- pole support: existing soft/Gram/signed-energy arrangement;
- new Carrier support: none.

## Durable evidence

- `research/benincasa/check_tensor_infinity_gysin_elliptic.py`;
- `research/benincasa/tensor-infinity-gysin-elliptic.json`;
- the explicit infinity-Gysin normalization of the rank-nine source sector.

## Scope and next falsifier

This computes one source-normalized occurrence generator.  Cyclic transport
supplies the other vertices, but the physical period pairing and the full
admissible score/polarization recovery still require a combined observer
test.  That is the next gate.
