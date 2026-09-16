# The scalar Euler cumulants reassemble absolutely on the Euler half-plane

## Question

Do the normalized first two cumulants converge compatibly with the connected determinant tail on any nonempty analytic domain?

## Claim boundary

The scalar Euler cumulant series converge absolutely and compact-locally on \(\operatorname{Re}s>1\), and reassemble uniquely once an Euler orientation is fixed. Matching their signs to the operator compiler requires an explicit local identification of the return block with \(x_p\) or \(-x_p\); that identification is not supplied here. This does not continue the operator compiler into the critical strip.

## Local expansion

For

$$
x_p(s)=p^{-s},
$$

one has, when \(|x_p(s)|<1\),

$$
-\log(1-x_p)
=x_p+\frac12x_p^2+
\sum_{k\ge3}\frac1k x_p^k.
$$

These are the scalar grade-one, grade-two, and grade-at-least-three Euler cumulants for the inverse factor \((1-x_p)^{-1}\). The direct factor \((1-x_p)\) has all three signs reversed. An operator return convention must select between them.

## Compact-local convergence

Fix compact \(Q\subset\{\operatorname{Re}s>1\}\), and choose \(\epsilon>0\) with \(\operatorname{Re}s\ge1+\epsilon\) on \(Q\). Then

$$
\sum_p\sup_{s\in Q}|x_p(s)|
\le
\sum_p p^{-1-\epsilon}<\infty.
$$

Consequently the primitive series converges absolutely and uniformly on \(Q\). The square series is dominated by \(\sum_pp^{-2-2\epsilon}\), and the connected series by

$$
\sum_p\sum_{k\ge3}\frac1k p^{-k(1+\epsilon)},
$$

so both also converge uniformly on \(Q\). Termwise holomorphy and the Weierstrass theorem give holomorphic limits.

## Reassembly

Let

$$
L_1(s)=\sum_p x_p(s),
\qquad
L_2(s)=\sum_p x_p(s)^2,
$$

and

$$
L_{\ge3}(s)=
\sum_p\sum_{k\ge3}\frac1k x_p(s)^k.
$$

Then

$$
L_1(s)+\frac12L_2(s)+L_{\ge3}(s)
=
\log\zeta(s)
$$

in the branch normalized by decay as \(\operatorname{Re}s\to+\infty\). Equivalently, the regularized determinant factors and the first two counterterms multiply to the ordinary Euler determinant. Including the already constructed Gaussian Mellin line gives the completed finite-to-infinite compiler on \(\operatorname{Re}s>1\).

Differentiating compact-locally yields the prime contribution to the unified logarithmic contour differential,

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
$$

Thus the scalar first two Euler cumulants are compatible with the scalar connected tail wherever absolute convergence is available. Equality with the operator-determinant cumulants remains conditional on the local sign/orientation identification.

## Continuation boundary

This result does not prove that the operator-valued \(\det_3\) section and its separate cumulant factors continue across \(\operatorname{Re}s=1\). The scalar completed zeta function has a known meromorphic continuation, but importing that continuation as the operator determinant compiler would require equality of the continued operator section, not merely equality on the Euler half-plane.

## Disposition

All scalar Euler cumulant pieces converge and reassemble analytically on \(\operatorname{Re}s>1\). A subsequent primary-source comparison with the semilocal Sonin multiplier fixes the relevant orientation: \(K_p=-p^{-s}\), so the compiler produces the direct factor \(1-p^{-s}\). The remaining internal task is continuation of that operator/line-valued section toward the critical strip with multiplicities preserved.