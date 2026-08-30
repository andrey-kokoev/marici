# The Raw T7 Bulk-Period Rank Test Fails the UV Definition Gate

## Proposed test

The previous frontier requested the seven values

\[
\left(\int_{\Gamma_{\rm BD}}e_1,\ldots,
\int_{\Gamma_{\rm BD}}e_6,
\int_{\Gamma_{\rm BD}}v_{\rm alg}\right)
\]

at one generic point, followed by Gauss--Manin transport and restriction to
the two-dimensional residual quotient of (T_7).

## Source audit

The printed nine-master basis is

\[
e_1=y_{23}y_{31}\varphi_{001},\quad
e_2=y_{23}\varphi_{001},\quad
e_3=y_{23}\varphi_{002},
\]

with the analogous (e_4,e_5), and (e_6=\varphi_{002}), where

\[
\varphi_{00k}=\frac{dy_{12}\,dy_{23}\,dy_{31}}
{q_{\mathcal G_{12}}^k}.
\]

On the source Cayley--Menger chamber at large Euclidean loop momentum (r),

\[
y_{12}\sim y_{23}\sim y_{31}\sim r,
\qquad q_{\mathcal G_{12}}=E+y_{12}\sim r,
\]

while the normalized (d=3) measure is the ordinary positive loop measure
(d^3\ell\), with radial factor (r^2dr). Consequently the cutoff growth of
((e_1,ldots,e_6)) is

\[
(\Lambda^4,\Lambda^3,\Lambda^2,
  \Lambda^3,\Lambda^2,\Lambda).
\]

The (e_1) integrand is positive on the literal chamber, so its leading
divergence cannot be removed by angular cancellation. The ordinary
Bunch--Davies (i\epsilon) prescription specifies the energy-pole boundary
value but is not an ultraviolet subtraction prescription.

## Correction

\[
\boxed{
\text{the raw seven-period vector is not defined at }d=3
\text{ without additional UV normalization.}
}
\]

Therefore its residual rank cannot yet falsify or complete the physical
readout calculus. Numerical quadrature with a convenient cutoff would insert
new, cutoff-dependent coefficient data.

## Sharpened frontier

The next admissible test is one of the following equivalent source-level
constructions:

1. analytically continue the source measure from a convergence domain in
   (d), specify the finite-part/counterterm map, and prove the residual rank
   is scheme independent; or
2. derive a chain-level projection to
   (T_7/(\operatorname{im}_{\log}+\operatorname{im}_{\rm Cut})) whose paired
   integrand is ultraviolet finite before integration.

The second is sharper. It asks whether the two residual quotient functionals
annihilate the source-derived UV counterterm subspace. If they do, the physical
rank test becomes canonical without constructing seven separately divergent
periods. If they do not, the current source packet lacks the renormalization
data required to define the claimed physical readout.

## Reproduction

```text
python research/nima/checkers/check_t7_bulk_period_uv_gate.py
```
