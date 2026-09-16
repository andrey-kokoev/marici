# Quarter-turn equivariance lives on the Fourier-saturated total presentations

## Question

Must the additive Fourier quarter turn descend to an endomorphism of each unaugmented semilocal presentation before it can be compatible with the presentation tetrahedron?

## Claim boundary

No. The source-derived four-port orbit is retained as a fiber. Extending each semilocal presentation by that fiber gives exact quarter-turn mixed squares. This minimal product construction establishes uncoupled compatibility; a nontrivial source coupling requires additional naturality data.

Let \(\mathfrak D_k\) be the Fourier-saturated retained carrier with

$$
\mathcal F_k:\mathfrak D_k\longrightarrow\mathfrak D_k,
\qquad
\mathcal F_k^4=\operatorname{id}.
$$

For each semilocal presentation \(V_i\), define the total presentation

$$
\widehat V_{i,k}=V_i\times\mathfrak D_k.
$$

Lift every presentation map by

$$
\widehat C_{ij,k}=C_{ij}\times\operatorname{id}_{\mathfrak D_k},
$$

and define the quarter turn on every total presentation by

$$
\widehat\rho_{i,k}=\operatorname{id}_{V_i}\times\mathcal F_k.
$$

Then, for every \(i,j\),

$$
\widehat\rho_{j,k}\widehat C_{ij,k}
=
\widehat C_{ij,k}\widehat\rho_{i,k}
$$

by direct evaluation on \((v,d)\): both sides equal

$$
(C_{ij}v,\mathcal F_kd).
$$

Moreover,

$$
\widehat\rho_{i,k}^4=\operatorname{id}_{\widehat V_{i,k}}.
$$

Thus all six quarter-turn mixed squares and the fourth-power law are constructed on the Fourier-saturated total presentation system.

## Why descent is not required

An endomorphism on an unaugmented quotient presentation would require Fourier invariance of the forgotten-data kernel. Prior four-port results retain support and character ports precisely because scalar, valuation, or radial projections can discard one of them. Failure of descent therefore supports retaining the vertical fiber rather than forcing a quarter turn onto each shadow \(V_i\).

## Coupling boundary

The product system proves independent coexistence of the \(D\)-fiber and \(V\)-tetrahedron. To claim that arithmetic presentation changes act nontrivially on the Fourier fiber, replace the identity fiber map by a source-derived family

$$
T_{ij,k}:\mathfrak D_k\longrightarrow\mathfrak D_k
$$

and verify

$$
\mathcal F_kT_{ij,k}=T_{ij,k}\mathcal F_k.
$$

No such nontrivial coupling is inferred from the product construction.

## Disposition

The minimal Fourier-saturated total presentation carries exact quarter-turn equivariance for all six semilocal edges. The half-turn formulas previously derived describe the shadows after reciprocal descent. Nontrivial coupling between presentation changes and the four-port fiber remains a separate constructor problem.