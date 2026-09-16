# The semilocal Sonin multiplier fixes the determinant return orientation

## Question

Does the source select the sign of the local return block in the determinant compiler?

## Claim boundary

Yes for the compiler attached to the semilocal Sonin presentation. The primary-source multiplier is the direct inverse Euler factor \(1-p^{-s}\), forcing the local determinant convention \(I+K_p=I-x_p\), hence \(K_p=-x_p\). This does not authorize a different external G4 loading.

## Source multiplier

The semilocal Sonin amplification has exact Mellin effect

$$
M_S(s)=
\prod_{p\in S\setminus\{\infty\}}
(1-p^{-s}),
$$

with \(s=1/2+it\) on the critical line. Thus the source uses the direct inverse local Euler factor, not its reciprocal.

## Return orientation

Write \(x_p(s)=p^{-s}\). To represent the local source multiplier by an ordinary determinant, one must have

$$
\det(I+K_p(s))=1-x_p(s).
$$

On the one-dimensional local return line this uniquely gives

$$
K_p(s)=-x_p(s).
$$

The opposite convention \(K_p=+x_p\) would produce \(1+x_p\), while representing \((1-x_p)^{-1}\) would require an inverse determinant. Neither equals the primary-source Sonin multiplier.

## Cumulant signs

For \(K_p=-x_p\),

$$
\operatorname{Tr}K_p=-x_p,
\qquad
\operatorname{Tr}K_p^2=x_p^2,
$$

and

$$
\log\det(I+K_p)
=-x_p-\frac12x_p^2-
\sum_{k\ge3}\frac1k x_p^k
=
\log(1-x_p).
$$

Therefore the finite-stage regularized compiler

$$
\exp\left(\operatorname{Tr}K-rac12\operatorname{Tr}K^2\right)
\det_3(I+K)
$$

has exactly the direct-Euler orientation required by \(M_S\).

## Spectral current

Differentiating gives

$$
\partial_s\log M_S(s)
=
\sum_{p\in S}
\frac{(\log p)p^{-s}}{1-p^{-s}},
$$

with the corresponding \(t\)-derivative sign determined by \(s=1/2+it\). This is the same direct-factor orientation used by the reflected scattering ratio and finite-prime Weil current.

## Boundary

The sign is fixed only after naming the Sonin multiplier as the determinant section being compiled. It does not select between the mixed primitive-square and forward theta-shell source arrows proposed for an external G4 feature packet.

## Disposition

The local operator-to-Euler orientation gate is closed for the semilocal determinant compiler: \(K_p=-p^{-s}\) and the compiled section is the direct inverse-Euler product \(M_S\). The remaining internal determinant task is continuation/completion of this operator-valued section beyond the absolute Euler half-plane.