# The prime-two Poisson seam is not fixed by self-duality and chart positivity

Author: \`marici.Nima\`

## 1. Target

The remaining proposed RH route asked for a primal--dual Poisson action on
the positive seam vector

\[
a(q)=\sqrt{f(e^q)}
\]

and its first finite block on \(0\le q\le\log2\), where

\[
f(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.
\]

The density \(f\) is Fourier self-dual, vacuum-null, and positive for
\(x\ge1\). Poisson summation acts linearly on \(f\), whereas seam positivity
uses its pointwise square root. The question is whether self-duality,
vacuum nullity, and chart positivity nevertheless determine the finite
positive seam block. They do not.

## 2. A self-Fourier hostile direction

Let \(H_n\) denote the physicists' Hermite polynomial and put

\[
h_n(x)=H_n(\sqrt{2\pi}\,x)e^{-\pi x^2}.
\]

Under the Fourier convention used for theta,

\[
\widehat h_n=(-i)^nh_n.
\]

Thus \(h_0,h_4,h_8,h_{12}\) all lie in the \(+1\) Fourier eigenspace.
There is a unique combination

\[
h=h_{12}+c_8h_8+c_4h_4+c_0h_0
\]

with

\[
h(0)=h(1)=h(2)=0.
\]

Equivalently, if \(P(x)=e^{\pi x^2}h(x)\), the coefficients solve

\[
c_0H_0(t_j)+c_4H_4(t_j)+c_8H_8(t_j)
=-H_{12}(t_j),
\quad t_j=\sqrt{2\pi}\,j,\quad j=0,1,2.
\]

Numerically,

\[
\begin{aligned}
c_0&=10544465.4727593\ldots,\\
c_4&=-475574.164936166\ldots,\\
c_8&=-3275.50922233652\ldots.
\end{aligned}
\]

The polynomial factors as

\[
P(x)=x^2(x^2-1)(x^2-4)Q(x^2),
\]

where \(Q(y)>0\) for \(y\ge1\). Hence

\[
h(x)<0\quad(1<x<2),\qquad h(x)>0\quad(x>2).
\]

## 3. Hostile positive source

For sufficiently small \(\varepsilon>0\), define

\[
f_\varepsilon=f+\varepsilon h.
\]

Then:

1. \(\widehat f_\varepsilon=f_\varepsilon\);
2. \(f_\varepsilon(0)=0\);
3. \(f_\varepsilon(1)=f(1)>0\);
4. \(f_\varepsilon(2)=f(2)>0\);
5. \(f_\varepsilon(x)>0\) for every \(x\ge1\).

The last statement follows because \(f>0\) on the compact interval
\([1,2]\), so a sufficiently small perturbation preserves its sign there,
while \(h\ge0\) for \(x\ge2\).

Therefore \(f\) and \(f_\varepsilon\) have the same Fourier eigenvalue,
integral lattice, Poisson functional equation, vacuum nullity, chart
positivity, and boundary samples at labels \(1\) and \(2\).

But for \(0<q<\log2\),

\[
f_\varepsilon(e^q)\ne f(e^q)
\]

generically, and likewise at \(2e^q\). Their positive amplitude vectors and
prime-two seam blocks therefore differ:

\[
B_{\varepsilon,mn}^{(2)}(z)
=\int_0^{\log2}e^{izu}
\sqrt{f_\varepsilon(me^u)f_\varepsilon(ne^u)}\,du
\ne B_{mn}^{(2)}(z).
\]

## 4. Finite falsifier

Any purported finite Poisson operator \(U_2\) determined solely by
vacuum nullity, Fourier self-duality, chart positivity, and the first two
seam samples would have to assign the same \(p=2\) block to \(f\) and
\(f_\varepsilon\). The explicit off-seam difference contradicts that
prediction.

The smallest scalar witness is any \(q_0\in(0,\log2)\) with
\(h(e^{q_0})\ne0\):

\[
\boxed{
\Delta_1(q_0)
=f_\varepsilon(e^{q_0})-f(e^{q_0})
=\varepsilon h(e^{q_0})\ne0,}
\]

despite equality at \(q=0\) for labels \(1\) and \(2\).

Thus Poisson self-duality acts on the full linear density, not on a finite
positive amplitude block. A canonical finite \(p=2\) primal--dual matrix
cannot be recovered from the stated data.

## 5. Consequence for the preferred route

\[
\boxed{
\text{self-Fourier density + integral chart positivity}
\not\Rightarrow
\text{a canonical finite Poisson action on seam amplitudes}.}
\]

The hostile pair preserves the scalar reciprocal functional equation while
changing the off-seam positive operator data. Positivity of each resulting
Gram block is automatic and therefore does not distinguish theta.

To continue, one would need an additional source law fixing the entire
Hermite carrier \(f\), not merely its Fourier eigenvalue, lattice samples, or
chart positivity. Minimal differential order does fix \(f\), but after that
selection the desired coercivity of its completed interaction is again the
unresolved Weil/Pick orientation. No independent inequality for \(C_Y\)
emerges.

## 6. Disposition

The proposed Poisson-seam reopening is falsified in its finite form. The
prime-two seam contains more information than its endpoint samples, while
Poisson summation is intrinsically a full-lattice density identity. Any
finite amplitude action requires extra, noncanonical interpolation data.

The RH Lakatos block remains closed.
