# Multiplication and derivative generate a source-authorized odd Sonin test chart

## Question

Can the missing odd real-character Sonin chart be constructed from the existing even Sonin test space without importing an unrelated source?

## Claim boundary

Yes on the Schwartz/Sonin test rung. Multiplication by the coordinate and differentiation preserve the two Sonin gaps in the required crossed way and generate a Fourier-invariant odd companion. This does not yet prove the weighted Hilbert isometry or surjectivity onto an independently defined full odd Sonin Hilbert space.

## Even Sonin core

Let \(E_\lambda\subset\mathcal S(\mathbb R)_{\rm ev}\) be the even Sonin test core satisfying

$$
f(x)=0
\quad\text{and}\quad
\widehat f(x)=0
$$

for \(|x|<\lambda\). Assume the existing source Fourier action preserves this core.

## Two odd generators

Define

$$
Xf(x)=xf(x),
\qquad
Df(x)=f'(x).
$$

Both are odd Schwartz functions. Since \(f\) vanishes on the gap, so do \(Xf\) and \(Df\). Their Fourier transforms are

$$
\mathcal F(Xf)
=-\frac1{2\pi i}D(\mathcal Ff),
$$

$$
\mathcal F(Df)
=2\pi iX(\mathcal Ff).
$$

Because \(\mathcal Ff\) vanishes on the Fourier gap, both transformed functions also vanish there.

## Odd companion

Set

$$
O_\lambda
=XE_\lambda+DE_\lambda
\subset\mathcal S(\mathbb R)_{\rm odd}.
$$

The displayed identities imply

$$
\mathcal F O_\lambda=O_\lambda.
$$

On this odd space,

$$
\mathcal F^2=-I,
$$

so its Fourier spectrum is \(\{i,-i\}\). Therefore

$$
E_\lambda\oplus O_\lambda
$$

carries all four Fourier characters.

## Semilocal extension

At each finite prime, retain the same Fourier-invariant local seed

$$
\sigma_p=oldsymbol 1_{\mathbb Z_p}
-p^{-1}oldsymbol 1_{p^{-1}\mathbb Z_p}.
$$

Tensoring \(O_\lambda\) with these finite seeds produces an odd/sign-character semilocal test chart. Fourier acts on the archimedean odd factor and fixes the finite seeds, so the semilocal test chart is order-four compatible.

## Topology

Multiplication by \(x\), differentiation, and Fourier transform are continuous on Schwartz space. Hence \(O_\lambda\), equipped with the quotient topology from

$$
E_\lambda\oplus E_\lambda
\longrightarrow O_\lambda,
\qquad
(f,g)\longmapsto Xf+Dg,
$$

is a source-generated locally convex test space with continuous Fourier action.

## Hilbert boundary

Neither \(X\) nor \(D\) is bounded on unweighted \(L^2\). Consequently the even Sonin Hilbert isometry does not automatically extend to this odd companion. A graph-weighted completion or a primary-source odd isometry theorem is still required before claiming Hilbert equivalence.

## Disposition

The missing odd real-character Sonin chart is constructed on the semilocal Schwartz test rung as \(O_\lambda=XE_\lambda+DE_\lambda\). Together with the even chart it supports all four Fourier characters and the full response quarter turn. Hilbert completion remains open.