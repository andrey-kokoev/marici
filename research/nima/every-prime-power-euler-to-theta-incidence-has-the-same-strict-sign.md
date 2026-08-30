# Every prime-power Euler-to-theta incidence has the same strict sign

## Result

The Euler-to-theta sampling coefficient is strictly negative at every prime:

\[
c_p<0,
\qquad
\eta_p<0.
\]

No global monotonicity theorem for \(\Phi\) is needed. Every arithmetic sampling point satisfies

\[
k\log p\ge\log2,
\]

and on this entire region each individual completed-theta label has negative derivative.

Thus primitive, square, and connected-tail incidence terms all have the same sign and cannot cancel.

## One-label derivative

For

\[
h_\lambda(u)=e^{u/2}e^{-\lambda e^{2u}},
\]

the completed label is

\[
\phi_\lambda(u)
=
\left(\partial_u^2-\frac14\right)h_\lambda(u)
=
2\lambda
\left(
2\lambda e^{2u}-3
\right)
e^{5u/2-\lambda e^{2u}}.
\]

Differentiating gives

\[
\phi_\lambda'(u)
=
-\lambda e^{5u/2-\lambda e^{2u}}
Q(\lambda e^{2u}),
\]

where

\[
Q(x)=8x^2-30x+15.
\]

The larger root of \(Q\) is

\[
x_+
=
\frac{15+\sqrt{105}}8.
\]

It satisfies

\[
x_+<\frac{26}{8}<4.
\]

Therefore

\[
Q(x)>0
\qquad
(x\ge4).
\]

## Arithmetic sampling region

Every positive theta label has

\[
\lambda_n=\pi n^2\ge\pi.
\]

At a prime-power sampling point

\[
u=k\log p,
\qquad
p\ge2,
\qquad
k\ge1,
\]

we have

\[
e^{2u}=p^{2k}\ge4.
\]

Hence

\[
\lambda_ne^{2u}
\ge
4\pi
>
4.
\]

It follows that

\[
Q(\lambda_ne^{2u})>0
\]

for every \(n,p,k\), and consequently

\[
\phi_{\lambda_n}'(k\log p)<0.
\]

The completed source is the sum over the paired labels \(\pm n\), while the wall is killed by the completion operator. Absolute convergence permits termwise differentiation. Therefore

\[
\Phi'(k\log p)<0
\]

for every prime \(p\) and grade \(k\ge1\).

## Incidence sign

The full incidence scalar is

\[
c_p
=
2(\log p)
\sum_{k\ge1}
p^{-k/2}\Phi'(k\log p).
\]

Every coefficient outside \(\Phi'\) is positive and every sampled value is strictly negative. Thus

\[
c_p<0.
\]

The Euler-relative coefficient is

\[
\eta_p
=
2(1-p^{-1/2})
\sum_{k\ge1}
p^{-(k-1)/2}\Phi'(k\log p),
\]

so likewise

\[
\eta_p<0.
\]

The same proof gives separately

\[
c_p^{(1)}<0,
\qquad
c_p^{(2)}<0,
\qquad
c_p^{(\ge3)}<0.
\]

Therefore the connected tail reinforces rather than cancels the strict two-grade incidence.

## Three-port sign frame

The intrinsic Euler coordinate satisfies

\[
h_p^{\mathrm{Euler}}>0.
\]

Since

\[
c_p=\eta_ph_p^{\mathrm{Euler}}<0,
\]

the propagated theta vector is a negative multiple of \(\Phi'\).

The analytic ports then give

\[
J_{\mathrm{Wr}}(c_p\Phi')
=
-\frac12c_p>0,
\]

and, because \(\Phi''(0)<0\),

\[
J_{\mathrm N}(c_p\Phi')
=
c_p\Phi''(0)>0.
\]

Thus the source sign frame is consistent:

- Euler intrinsic orientation: positive;
- Euler-to-theta incidence coefficient: negative;
- oriented Wronskian output after propagation: positive;
- oriented seam-normal output after propagation: positive.

Changing any one convention alone breaks this agreement.

## No raw uniform lower bound

Strict nonvanishing prime by prime does not imply

\[
\inf_p|\eta_p|>0.
\]

Indeed, the first sampling point moves to

\[
\log p\to\infty,
\]

where \(\Phi'\) decays superexponentially. Hence

\[
\eta_p\to0
\]

faster than any power along the primes.

This is not completion loss if the source incidence-line norm carries the same sampling scale. It does rule out a lower frame bound in an unweighted prime counting norm.

The correct normalized local generator is

\[
\widetilde e_p
=
|\eta_p|^{-1}e_p
\]

only if that reweighting is derived as the pullback metric of the source sampling map. It cannot be introduced as an arbitrary repair.

## Constructor consequence

The arithmetic-to-theta mate square is now pointwise faithful:

\[
\nu_p^{\mathrm{Euler}}
\longmapsto
c_p\Phi'
\ne0.
\]

Primitive, square, and tail channels remain separately typed and all preserve the same orientation.

The remaining quantitative theorem is metric rather than algebraic:

> Prove that the theta-sampling pullback metric is the source-authorized norm on the Euler incidence line and remains compatible with cutoff completion.

If so, the vanishing raw size of \(\eta_p\) is absorbed by the correct source geometry, just as the Euler half-density was earlier.
