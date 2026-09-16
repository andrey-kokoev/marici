# The endpoint Douglas constant is the Christoffel leverage at negative one quarter

## Objective

Convert the finite-rank endpoint Schur inequality into a scalar extremal quantity and identify its completed limit.

The relevant quantity is the Christoffel leverage of the gamma--prime shifted moment form at the endpoint coordinate

\[
x_E
=
-
\frac14.
\]

## Remainder moment matrix

Fix \(t_0>0\). Let

\[
C_r
=
H_r^{R,+}(t_0)
=
(
r_{i+j+1}
)_{0\le i,j\le r},
\]

and let

\[
v_r(x)
=
(
1,x,x^2,\ldots,x^r
)^T.
\]

The endpoint vector is

\[
v_r
=
v_r(x_E).
\]

The required shifted endpoint inequality is

\[
C_r
\succeq
c_E
v_rv_r^*,
\qquad
c_E
=
\frac14

e^{t_0/4}.
\]

## Christoffel leverage

Assume first that \(C_r\) is positive definite. Define

\[
\mathcal L_r(x_E)
=
v_r(x_E)^*
C_r^{-1}
v_r(x_E).
\]

Then the rank-one update criterion gives

\[
\boxed{
C_r
-
c_E
v_rv_r^*
\succeq0
\quad\Longleftrightarrow\quad
c_E
\mathcal L_r(x_E)
\le
1.
}
\]

For singular \(C_r\), the exact criterion is

\[
v_r(x_E)
\in
\operatorname{ran}
C_r^{1/2}
\]

and

\[
c_E
v_r(x_E)^*
C_r^\dagger
v_r(x_E)
\le
1.
\]

Thus endpoint positivity is one scalar leverage bound at each rank.

## Extremal polynomial form

The reciprocal Christoffel leverage is

\[
\boxed{
\lambda_r(x_E)
=
\frac1{
\mathcal L_r(x_E)
}
=
\inf
\left\{
\mathcal Q_r^R(p):
\deg p\le r,

p(x_E)=1
\right\},
}
\]

where

\[
\mathcal Q_r^R(p)
=
\sum_{i,j=0}^r
\overline{c_i}
c_j
r_{i+j+1}
\]

for

\[
p(x)
=
\sum_{j=0}^r
c_jx^j.
\]

The endpoint condition is therefore

\[
\boxed{
\lambda_r(-1/4)
\ge
\frac14

e^{t_0/4}.
}
\]

This formulation does not require choosing a matrix square root or Douglas contraction.

## Monotonicity in rank

The admissible polynomial set enlarges with \(r\), so

\[
\lambda_{r+1}(x_E)
\le
\lambda_r(x_E).
\]

Equivalently,

\[
\mathcal L_{r+1}(x_E)
\ge
\mathcal L_r(x_E).
\]

Hence fixed-rank endpoint checks become harder, never easier, as the source packet is enlarged.

A completed endpoint contraction exists only if

\[
\inf_r
\lambda_r(-1/4)
\ge
c_E.
\]

Packetwise positivity without a uniform lower bound is insufficient.

## Measure interpretation

Suppose the remainder shifted functional has a determinate positive representing measure \(\mu_R^+\) on the real moment line:

\[
\mathcal Q^R(p)
=
\int
|p(x)|^2
\,d\mu_R^+(x).
\]

Then

\[
\lambda_r(x_E)
=
\inf_{
\deg p\le r,
p(x_E)=1
}
\int
|p(x)|^2
\,d\mu_R^+(x).
\]

Under polynomial density in \(L^2(\mu_R^+)\), the limit is the mass of the atom at \(x_E\):

\[
\boxed{
\lim_{r\to\infty}
\lambda_r(x_E)
=
\mu_R^+(
\{x_E\}
).
}
\]

Indeed, every admissible polynomial contributes at least the atomic mass, and polynomial approximation to the indicator of the atom gives the reverse inequality.

Therefore the completed endpoint leverage condition is equivalent to

\[
\boxed{
\mu_R^+
(
\{-1/4\}
)
\ge
\frac14

e^{t_0/4}.
}
\]

## Exact mass under a positive completed measure

If the full completed heat source has a positive Stieltjes representation

\[
\Theta(t)
=
\int_{[0,\infty)}

e^{-tx}
\,d\nu(x),
\]

then

\[
R(t)
=
\Theta(t)
-

e^{t/4}
\]

has the formal signed measure

\[
d\nu(x)
-
\delta_{-1/4}.
\]

Applying one shifted moment multiplies by \(x\). Hence the shifted remainder measure is

\[
\boxed{
d\mu_R^+(x)
=
x

e^{-t_0x}
\,d\nu(x)
+
\frac14

e^{t_0/4}
\delta_{-1/4}.
}
\]

Its endpoint atomic mass is exactly

\[
c_E
=
\frac14

e^{t_0/4}.
\]

Thus the endpoint leverage inequality is saturated in the completed positive model:

\[
\lim_{r\to\infty}
\lambda_r(-1/4)
=
c_E.
\]

The gamma--prime remainder must carry precisely the counter-atom needed to cancel the negative shifted endpoint contribution.

## Source-side significance

The preceding exact mass formula is conditional on the positive completed measure. Source-side, it identifies what must be proved without assuming that measure:

1. \(C_r\succeq0\) for every \(r\);
2. \(\lambda_r(-1/4)\ge c_E\) for every \(r\);
3. the decreasing Christoffel sequence does not fall below \(c_E\);
4. ideally, \(\lambda_r(-1/4)\to c_E\).

The fourth statement is the sharp endpoint extraction law.

## Relation to completed-heat decay

Prior completed-heat decay analysis extracts the endpoint coefficient from large translation/localizer moments. The Christoffel formulation extracts the same coefficient from increasing polynomial degree at one fixed heat time.

These are two limits of one object:

1. translation to large heat time isolates the fastest negative-rate endpoint mode;
2. increasing polynomial degree isolates its atom in the remainder moment measure.

A comparison theorem between these limits could turn the known endpoint asymptotic into the required uniform leverage bound. Such a theorem has not yet been established.

## Rotor distinction

For a moving hostile rotor, the defect coordinates occur at different spectral locations and contribute a higher-dimensional model space. The scalar Christoffel leverage at \(-1/4\) controls only the fixed endpoint atom.

No bound on

\[
\mathcal L_r(-1/4)
\]

can absorb independent rotor evaluations at \(\pm\gamma\).

## Tetrahedral interpretation

The finite-rank Douglas contraction has norm

\[
\|c_r\|^2
=

c_E
\mathcal L_r(-1/4).
\]

Successor naturality under rank inclusion requires these contractions to be restrictions of one completed endpoint vector. Uniform contractivity is exactly

\[
\sup_r
c_E
\mathcal L_r(-1/4)
\le
1.
\]

Thus the terminal endpoint horn is governed by one monotone scalar sequence of Christoffel leverages.

## Disposition

The endpoint gate has a sharp scalar form:

\[
\boxed{
\lambda_r(-1/4)
\ge
\frac14

e^{t_0/4}
\quad
\text{for every }r.
}
\]

In a completed positive representation, the lower bound is asymptotically exact because it is the mass of the gamma--prime counter-atom at \(-1/4\). The remaining source theorem is to derive this uniform Christoffel bound directly from the coupled digamma--prime moments.
