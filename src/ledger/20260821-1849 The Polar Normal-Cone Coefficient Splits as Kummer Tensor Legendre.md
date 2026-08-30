# 1849 — The Polar Normal-Cone Coefficient Splits as Kummer Tensor Legendre

## Radial/projective coordinates

On the normal-blowup chart of Entry 1848, write

\[
\delta_2=\rho,
\qquad
\delta_1=\rho r.
\]

The polar elliptic curve becomes

\[
w^2
=
\rho\,
x(1-x)
\bigl(xh_1+(1-x)h_2\bigr)
\bigl(xr+(1-x)\bigr).
\]

After the root-cover rescaling

\[
W=\frac{w}{\sqrt\rho},
\]

the strict-transform equation is independent of the radial coordinate:

\[
W^2
=
x(1-x)
\bigl(xh_1+(1-x)h_2\bigr)
\bigl(xr+(1-x)\bigr).
\]

## Connection splitting

For the elliptic de Rham basis, every period therefore factors as

\[
\Pi(\rho,r)=\rho^{-1/2}\Pi_{\rm Leg}(r).
\]

Consequently the resolved local connection is

\[
\boxed{
\nabla
=
d
-\frac12d\log\rho\,\operatorname{Id}
+A_{\rm Leg}(r)\,dr.
}
\]

The radial Kummer term is scalar, so its commutator with the Legendre block
vanishes.  There is no mixed radial--projective curvature and no invariant
mixed extension term in this local coefficient family.

## Chart compatibility

On the second normal chart,

\[
\delta_1=\rho',
\qquad
s=\frac{\delta_2}{\delta_1},
\]

the overlap is

\[
\rho'=\rho r,
\qquad
s=r^{-1}.
\]

The corresponding square-root factor is exactly the Kummer/root-cover
transition already typed by the oriented physical current in Entry 1843.
It is not a new coefficient extension or carrier datum.

## Narrow result

On the resolved two-normal cone,

\[
\boxed{
\mathbb V_{\rm polar}
\simeq
\mathcal K_{\rho^{-1/2}}
\otimes
m(r)^*\mathbb H_{\rm Leg}.
}
\]

Thus the local five-site polar block has the same structural form as the
homogeneous three-site elliptic block: a source-derived Kummer character
tensor a Legendre Gauss--Manin variation compiled from labelled normal data.

## Scope

The splitting is a theorem for the local polar double-Morse coefficient
family.  It does not construct or normalize the global physical integration
chain, and it does not exclude extensions involving other five-site master
blocks away from this local quotient.

## Next falsifier

Test whether the local polar elliptic quotient embeds canonically into the
full five-site marked-relative Gauss--Manin system.  The required map must be
derived from source residues/Gysin operations and must intertwine the cyclic
occurrence action; matching local differential equations is insufficient.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_radial_legendre_split.py`
- `research/benincasa/results/five-site-region-pair-polar-radial-legendre-split.json`
- Entries 1843--1848
- allocator claim: `seqclaim-0e8c52d3701de7ab497127f8`
