# The Laguerre derivative bridge is injective but has no coercive inverse

## Scope

The normalized Laguerre formula makes the derivative bridge explicit, but it does not give a positive lower bound. This note records the missing spectral fact and its consequence for the Green/Stokes constructor.

Let

[
mathsf D:operatorname{Dom}(mathsf D)subset L^2_{mathrm{even}}(mathbb R)
longrightarrow L^2_{mathrm{odd}}(mathbb R)
]

be the closed derivative with domain (H^1_{mathrm{even}}(mathbb R)).

In normalized Laguerre coordinates,

[
mathsf D E_k
=
-sqrt{2pi(k+	frac12)},O_k
-sqrt{2pi k},O_{k-1}.
]

## Injectivity

If (fin H^1(mathbb R)) and (mathsf Df=0), then (f) is almost everywhere constant. A nonzero constant is not in (L^2(mathbb R)). Hence

[
kermathsf D={0}.
]

Thus the derivative incidence loses no actual Hilbert vector.

## No lower bound

Choose a nonzero even (phiin C_c^infty(mathbb R)) and define the unitary dilates

[
phi_R(x)=R^{-1/2}phi(x/R).
]

Then

[
|phi_R|_2=|phi|_2
]

while

[
|mathsf Dphi_R|_2
=
R^{-1}|phi'|_2
longrightarrow0.
]

Therefore no constant (c>0) can satisfy

[
|mathsf Df|_2ge c|f|_2
]

on its domain. Equivalently, (0) lies in the spectrum of (mathsf D^*mathsf D), although it is not an eigenvalue.

The range of (mathsf D) is consequently not closed. Its inverse on the range is unbounded.

## Coefficient-space hostile

Under the unitary Laguerre synthesis, the dilates (phi_R) become unit coefficient vectors (a^{(R)}inell^2) satisfying

[
left|
left(
sqrt{j+	frac12},a_j^{(R)}
+
sqrt{j+1},a_{j+1}^{(R)}
ight)_{jge0}
ight|_{ell^2}
longrightarrow0.
]

This is the exact cancellation hostile for the bidiagonal coefficient matrix. Growing entries do not imply coercivity, because neighboring coefficients can cancel along increasingly long packets.

## Constructor consequence

The derivative bridge may be used in the forward direction on its closed graph domain. It may not be inverted as a bounded incidence coordinate, and it cannot by itself supply a uniform observability margin.

Accordingly:

- radical descent is harmless because the kernel is zero;
- quotient inversion is still unavailable because the range is not closed;
- any Schur formula containing ((mathsf D^*mathsf D)^{-1}) is unauthorized without an additional positive mass or source restriction;
- endpoint traces must be controlled by the full graph norm
  [
  |f|_{H^1}^2=|f|_2^2+|mathsf Df|_2^2,
  ]
  not by derivative energy alone.

In one dimension, the point trace is continuous on (H^1(mathbb R)), so a boundary-incidence port can remain bounded after the (L^2) mass is retained. This does not create a derivative-only lower bound.

## Result

The source-normalized derivative channel is faithful but noncoercive:

[
kermathsf D=0,
qquad
inf_{|f|_2=1}|mathsf Df|_2=0.
]

This distinguishes algebraic label survival from quantitative observability. The next relative Green/Stokes construction must retain the full history mass or another source-authorized infrared anchor; otherwise its proposed inverse or Schur return fails at zero frequency.
