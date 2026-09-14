# The completed-theta correlation is injective on the arithmetic interval range

## Question

Is the remaining analytic transform

\[
T_Df(s)=\int f(v)\Phi_1(v)\Phi_1(v+s+D)\,dv,
\qquad s\geq0,
\]

injective on the completed arithmetic interval-synthesis range?

## Claim boundary

Yes. The explicit completed atom converts the zero-history equation into a first-order differential equation for a Laplace transform. Arithmetic interval support excludes its sole nonzero formal solution. This proves completed augmented faithfulness on each fixed ratio block. It does not supply a Hilbert metric for the cycle port.

## Explicit atom and support

The recorded first atom is

\[
\Phi_1(u)
=e^{u/2}(2\pi^2e^{4u}-3\pi e^{2u})e^{-\pi e^{2u}}.
\]

Every actual interval begins at \(\log(kbp_j)\geq\log2\). Hence every synthesized \(f=Jc\) is supported in \([\log2,\infty)\). On this half-line \(2\pi e^{2u}-3>0\), so \(\Phi_1(u)\neq0\).

## Laplace reduction

Set

\[
x=e^{2v},
\qquad y=e^{2(s+D)}.
\]

Then \(x\geq4\), while \(s\geq0\) gives \(y\geq e^{2D}>0\). Define

\[
h(x)=\frac{\pi}{2}
f\!\left(\frac12\log x\right)
\Phi_1\!\left(\frac12\log x\right)x^{1/4}
\]

and its Laplace transform

\[
L(y)=\int_4^\infty h(x)e^{-\pi xy}\,dx.
\]

The Gaussian factor in \(\Phi_1\), together with \(f\in L^1\), makes \(h\in L^1([4,\infty))\). Direct substitution gives

\[
y^{-5/4}T_Df(s)
=-2yL'(y)-3L(y).
\]

## Zero-history equation

If \(T_Df(s)=0\) for all \(s\geq0\), then

\[
2yL'(y)+3L(y)=0
\]

for \(y\\geq e^{2D}\). Therefore

\[
L(y)=Cy^{-3/2}
\]

on that ray. But support of \(h\) in \([4,\infty)\) gives

\[
|L(y)|\leq e^{-4\pi y}\|h\|_1.
\]

Polynomial decay \(Cy^{-3/2}\) is compatible with this exponential bound only when \(C=0\). Thus \(L\) vanishes on an open positive ray. Analyticity and uniqueness of the Laplace transform for \(L^1\) functions imply \(h=0\) almost everywhere. Since \(\Phi_1\) has no zero on the arithmetic support, \(f=0\).

Hence \(T_D\) is injective on \(J(\mathcal C_{D,\exp})\).

## Completed augmented faithfulness

Combining this theorem with

\[
\ker J=\ker\partial
\]

proves

\[
\ker\widehat B_D=\ker\partial.
\]

The continuous chord selector is injective on that cycle space. Therefore

\[
(\widehat B_D,\widehat Z_D)
\]

is injective on the completed projective source.

## Disposition

The completed faithfulness gate is closed for every fixed ratio block. Common history remains nonfaithful by itself, but history plus projective route residue is a continuous faithful observer. Remaining forest-coordinate independence requires uniform bounds for completed change maps; physical cycle covariance remains unconstructed.
