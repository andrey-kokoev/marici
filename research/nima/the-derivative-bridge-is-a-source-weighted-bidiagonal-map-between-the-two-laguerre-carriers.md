# The derivative bridge is a source-weighted bidiagonal map between the two Laguerre carriers

## Scope

The even and odd Gaussian completion sectors have distinct Laguerre Jacobi weights. This note computes the derivative bridge between them. It is an unbounded typed intertwiner, not an identification of their coefficient matrices.

Let

[
X=pi x^2,qquad y=2X.
]

Use the raw Laguerre vectors

[
f_k(x)=e^{-X}L_k^{-1/2}(2X)
]

in the even sector and

[
g_k(x)=x e^{-X}L_k^{1/2}(2X)
]

in the odd sector.

## Exact raw derivative identity

The Laguerre derivative and parameter-shift identities are

[
rac{d}{dy}L_k^alpha(y)=-L_{k-1}^{alpha+1}(y),
]

[
L_k^{-1/2}(y)=L_k^{1/2}(y)-L_{k-1}^{1/2}(y).
]

Since (partial_x=2pi x,partial_X), they give

[
partial_x f_k
=
-2pileft(g_k+g_{k-1}ight),
]

with (g_{-1}=0).

Thus differentiation is lower bidiagonal from the even Laguerre carrier to the odd one. In particular, it does not send grade (k) to a single odd grade.

## Source normalization

The raw squared norms are

[
n_k^-=
rac1{sqrt{2pi}}
rac{Gamma(k+	frac12)}{k!},
]

[
n_k^+=
rac1{2^{3/2}pisqrtpi}
rac{Gamma(k+	frac32)}{k!}.
]

Define normalized vectors

[
E_k=rac{f_k}{sqrt{n_k^-}},
qquad
O_k=rac{g_k}{sqrt{n_k^+}}.
]

Then the derivative bridge has the exact coefficient formula

[
partial_x E_k
=
-sqrt{2pi(k+	frac12)},O_k
-sqrt{2pi k},O_{k-1}.
]

Equivalently,

[
partial_x E_k
=
-sqrt{pi(2k+1)},O_k
-sqrt{2pi k},O_{k-1}.
]

The half-integer offset in the diagonal coefficient is fixed by the source norms. It is not a free normalization.

## Coefficient operator

For a finite even coefficient sequence (a=(a_k)), the odd output coefficients are

[
(mathsf D a)_j
=
-sqrt{2pi(j+	frac12)},a_j
-sqrt{2pi(j+1)},a_{j+1}.
]

Hence the canonical coefficient-domain candidate is

[
operatorname{Dom}(overline{mathsf D})
=
left{
ainell^2:
left(
sqrt{j+	frac12},a_j+
sqrt{j+1},a_{j+1}
ight)_{jge0}
inell^2
ight}.
]

This is the graph domain inherited from the closed analytic derivative. The bridge is unbounded because its coefficients grow like (sqrt{k}).

## Typed completion intertwining

On the finite Laguerre core, the analytic identity remains

[
A(A+1)partial_x
=
partial_x(A-1)A.
]

Therefore the direct odd completion (A(A+1)) is intertwined with the shifted even-potential completion ((A-1)A). The derivative does not intertwine the direct even operator (A(A+1)) with the direct odd operator.

This distinction is the exact repair of the earlier parity-common-matrix error.

## Consequences and remaining gate

The bridge now has a completely explicit source-coordinate realization:

- even carrier parameter (-	frac12);
- odd carrier parameter (+	frac12);
- lower-bidiagonal derivative;
- source-fixed square-root weights;
- canonical graph-domain candidate.

What remains is to prove that the source incidence and Green/Stokes constructors use this closed graph domain and that their endpoint maps are bounded in its graph norm. No compactness, determinant-class, zero-identification, or RH consequence follows from the bidiagonal formula alone.
