---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# First Complete Unsplit Wall Class at Weight Minus One

## Record

Status: the complete unsplit source integrand has its first generic nonzero
logarithmic wall class at weight \(-1\). The class is supported on the
already frozen lower-divisor collision. Its coefficient is odd on the
symmetric source wall, so the literal wall period remains zero at this
grade.

No denominator, carrier incidence, support summand, regulator hierarchy,
projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the complete weight }-1\text{ coefficient also has zero logarithmic
residue on }r=0.
}
\]

The finite falsifier was a source-derived nonzero Laurent coefficient after
reducing every pole of order at most four.

## Frozen expansion depth

This entry uses exactly the expansion predeclared in entry 234:

- \(K\) through \(\tau^8\);
- \(K_1^{\rm src}\) through \(\tau^6\);
- the complete unsplit lower factor through relative order \(\tau^2\);
- the exact Jacobian \(da\wedge db=\tau^5dr\wedge dn\).

No occurrence splitting is performed.

Write

\[
K=\tau^6(k_0+\tau k_1+\tau^2k_2+O(\tau^3)),
\]

\[
K_1^{\rm src}
=
\tau^4(\ell_0+\tau\ell_1+\tau^2\ell_2+O(\tau^3)).
\]

The coefficients \(k_0,k_1,\ell_0,\ell_1\) are those of entry 234. The
new coefficients are

\[
\begin{aligned}
k_2={}&
-8n^2rxy^2
+r^4(x+y)^2
+4r^3(x^2-y^2)\\
&-2r^2(x^2+4xy+y^2)
-4r(x^2-y^2)
+5x^2+14xy+5y^2,
\end{aligned}
\]

and

\[
\ell_2
=
4\left[
r^2(x+y)^2
+2r(x^2-y^2)
-3x^2-8xy-3y^2
\right].
\]

The lower factor is

\[
\tau^3D_{\rm low}
=d_0+\tau d_1+\tau^2d_2+O(\tau^3),
\]

with

\[
d_0=-\frac{n}{4xyr^2},
\qquad
d_1=\frac{n^2(r-1)}{4xyr^3},
\]

and

\[
d_2
=
-\frac{n}{
8x^2y^2r^4
}
\left[
2n^2xyr^2-2n^2xyr+2n^2xy
-r^3x+r^3y+r^2x+r^2y
\right].
\]

## Exact Laurent reduction

Let

\[
k_{00}=k_0|_{r=0}
=
4xy(n^2xy-2x-2y).
\]

Expand

\[
-\frac12
K_1^{\rm src}K^{-3/2}
D_{\rm low},da\wedge db
\]

through weight \(-1\), then reduce the \(r^{-4},r^{-3},r^{-2}\) terms
modulo exact forms. The remaining logarithmic coefficient satisfies

\[
\boxed{
k_{00}^{3/2}
\operatorname{Res}_{r=0}F_{-1}
=
-\frac{
12n(x-y)(x+y)(n^2xy-x-y)
}{k_{00}}.
}
\]

Equivalently, on the frozen physical branch,

\[
\boxed{
\operatorname{Res}_{r=0}F_{-1}
=
-\frac{
3n(x-y)(x+y)(n^2xy-x-y)
}{
8x^{5/2}y^{5/2}
(n^2xy-2x-2y)^{5/2}
}.
}
\]

The common lower-half branch scalar is understood exactly as in entries
225--226; it does not affect nonvanishing or support.

## Finite falsifier

The numerator

\[
-3n(x-y)(x+y)(n^2xy-x-y)
\]

is not identically zero. Therefore

\[
\boxed{
\operatorname{Res}_{r=0}F_{-1}\ne0
}
\]

at generic nonsoft, non-symmetric kinematics.

The residue vanishes on the proper subloci

\[
n=0,
\qquad
x=y,
\qquad
n^2xy=x+y,
\]

as well as on excluded singular support of the denominator.

## Coefficient class versus source period

The residue coefficient is odd under

\[
n\longmapsto-n.
\]

The source wall remains the symmetric interval

\[
[-N,N],
\qquad
N^2=\frac{2(x+y)}{xy}.
\]

Hence its symmetric regularized pairing still vanishes:

\[
\int_{-N}^{N}
\operatorname{Res}_{r=0}F_{-1}
=0.
\]

Thus

\[
\boxed{
\text{nonzero wall coefficient class}
\quad\not\Rightarrow\quad
\text{nonzero literal source-chain period}.
}
\]

## Verdict

The continued-vanishing conjecture is falsified. The first canonical
full-source logarithmic class occurs at weight \(-1\):

\[
\boxed{
(-3,-2,-1)=(0,0,\text{generic nonzero})
}
\]

for the complete unsplit occurrence lift.

No new carrier incidence is needed. The new complexity is coefficient
support on the existing marked collision wall.

## Classification

- existing carrier: unchanged exceptional disk and \(r=0\) wall;
- first nonzero complete logarithmic coefficient: weight \(-1\);
- coefficient support: existing lower-divisor collision;
- literal symmetric source-wall period: zero;
- elliptic Gauss--Manin image: uncomputed, not inferred;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_complete_unsplit_first_wall_class.rs`;
- `research/benincasa/complete-unsplit-first-wall-class.json`;
- exact rational Laurent reduction at every admitted integer test point;
- independent factored and expanded numerator comparison;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Map the weight-\(-1\) wall class into the complete nine-master
algebraic--elliptic extension.

Test whether it:

1. lies entirely in the rank-seven algebraic/Tate kernel;
2. has a nonzero image under the infinity-Gysin quotient;
3. is killed by the physical relative chain despite being nonzero as a
   coefficient class.

A nonzero elliptic image would be the first evidence that the literal
lower-occurrence correction reaches the Legendre block. A zero image keeps
the correction in sector-specific algebraic/relative coefficient data over
the unchanged carrier.

## Outcome contract

~~~json
{
  "claim": "The complete weight -1 coefficient has zero logarithmic wall residue.",
  "status": "falsified",
  "complete_residues": {
    "-3": 0,
    "-2": 0,
    "-1": "generic nonzero"
  },
  "residue_numerator": "-3*n*(x-y)*(x+y)*(n^2*x*y-x-y)",
  "source_wall_pairing": 0,
  "carrier_support": "existing r=0 collision wall",
  "new_carrier_incidence": false,
  "next_experiment": "Map the weight -1 wall class into the algebraic-elliptic Gysin extension."
}
~~~
