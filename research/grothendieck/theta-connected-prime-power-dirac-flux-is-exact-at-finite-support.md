# Theta connected prime-power Dirac flux is exact at finite support

## Reciprocal ingress spinor

For `N>=2`, retain the two centered Mellin sheets

\[
 a_N(z)=
 \begin{pmatrix}
 N^{-1/2-iz}\\
 N^{-1/2+iz}
 \end{pmatrix}.
\]

With the polarized metric `sigma_3=diag(1,-1)`, packet 151 gives

\[
 J_N(z,w)
 ={2i\over N}\sin((\bar w-z)\log N).
\]

## Connected logarithmic weighting

At one prime,

\[
 \log(1-p^{-s})^{-1}
 =\sum_{k\ge1}{p^{-ks}\over k}.
\]

Thus the determinant-line connected packet weights the `p^k` circuit by
`1/k`. Define

\[
 J_p^{\mathrm{conn}}(z,w)
 =\sum_{k\ge1}{1\over k}J_{p^k}(z,w).
\]

The series converges absolutely on compact spectral sets because of the
factor `p^{-k}`. Explicitly,

\[
 J_p^{\mathrm{conn}}(z,w)
 =2i\sum_{k\ge1}{p^{-k}\over k}
 \sin(k(\bar w-z)\log p).
\]

## Exact von Mangoldt diagonal

Divide by the de Branges difference before taking the diagonal:

\[
 {J_p^{\mathrm{conn}}(z,w)\over\bar w-z}
 =2i\sum_{k\ge1}p^{-k}\log p\,
 \operatorname{sinc}(k(\bar w-z)\log p).
\]

Therefore

\[
 \lim_{w\to z}
 {J_p^{\mathrm{conn}}(z,w)\over\bar w-z}
 =2i\log p\sum_{k\ge1}p^{-k}
 ={2i\log p\over p-1}.
\]

The logarithmic weight is `Lambda(p^k)=log p`, not `log(p^k)`: the `1/k`
from the determinant-line logarithm cancels the `k` from differentiating the
Mellin character. This derives the connected prime-power normalization from
composition rather than fitting it afterward.

For a finite prime set `S`, the total connected flux is

\[
 J_S^{\mathrm{conn}}=\sum_{p\in S}J_p^{\mathrm{conn}},
\]

and its diagonal divided-difference energy is the strictly positive finite
sum

\[
 {1\over2i}\lim_{w\to z}
 {J_S^{\mathrm{conn}}(z,w)\over\bar w-z}
 =\sum_{p\in S}{\log p\over p-1}>0.
\]

## Global obstruction

The all-prime sum still diverges. Indeed `log p/(p-1)` is asymptotic to
`log p/p`, whose prime sum diverges. Thus the connected transform repairs the
label typing and removes composite overcounting, but it does not by itself
produce a finite global boundary energy.

The remaining completion must pair this canonical divergence with the
archimedean and seam currents. Subtracting it silently would repeat the
non-pointed finite-part failure of packets 190--191.

## Falsifier

At finite support the construction fails if the determinant-line logarithm
produces any coefficient other than `1/k`, if the divided diagonal does not
give `log p p^{-k}`, or if an additional composite label survives as an
independent connected channel.

## Scope

This proves the exact finite-support connected Dirac current and its positive
diagonal energy. It does not prove convergence, maximal isotropy, a global
Green identity, or RH orientation.
