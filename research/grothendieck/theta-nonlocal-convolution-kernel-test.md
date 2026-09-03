# Theta nonlocal convolution kernel test

Author: `marici.Grothendieck`
Status: canonical convolution candidate refuted
Predecessor: `theta-source-compatible-augmentation-no-go.md`

## Question

Does the theta source canonically define a fixed nonlocal Hilbert-space operator whose homogeneous kernel detects completed-scalar zeros?

## Canonical candidate

Let \(\Phi\in L^1(\mathbb R)\) be the real even theta kernel and define on \(L^2(\mathbb R)\)

\[
(K_\Phi f)(x)=\int_{\mathbb R}\Phi(x-y)f(y)\,dy.
\]

This is a bounded selfadjoint convolution operator. Under the unitary Fourier transform it becomes multiplication by

\[
\widehat\Phi(t)=\xi\!\left(\tfrac12+it\right)
\]

up to the fixed normalization convention.

## Kernel test

The multiplier is the restriction of a nonzero entire function. Its real zero set is therefore discrete and has Lebesgue measure zero. If \(K_\Phi f=0\), then

\[
\widehat\Phi(t)\widehat f(t)=0
\]

for almost every \(t\). Since \(\widehat\Phi\ne0\) almost everywhere, \(\widehat f=0\) almost everywhere, hence

\[
\ker_{L^2}K_\Phi=\{0\}.
\]

Individual scalar zeros produce only distributional Fourier fibers supported at points, not nonzero Hilbert-space kernel vectors. Moreover, because \(\widehat\Phi(t)\to0\) as \(|t|\to\infty\), zero belongs to the continuous spectrum independently of any finite scalar zero; that spectral fact cannot localize the zeros or constrain their real parts.

## Rigged Fourier-fiber test

In the tempered-distribution extension, a real critical-axis zero \(t_0\) does give

\[
\widehat\Phi\,\delta_{t_0}=0.
\]

If the zero has order \(m\), the distributions

\[
\delta_{t_0},\delta_{t_0}',\ldots,
\delta_{t_0}^{(m-1)}
\]

span the point-supported generalized kernel; multiplication by \(\widehat\Phi\) kills exactly these jets. Thus the rigged realization records location and multiplicity of zeros already lying on the real Fourier axis.

It does not test confinement. An off-axis zero is evaluation at a complex Fourier argument and is not a tempered distribution supported on the real spectral line. Choosing the real Fourier dual as the generalized spectrum therefore excludes off-axis parameters in the definition of the carrier rather than proving their absence. The delta fibers also have no finite \(L^2\) norm. Giving them a positive norm requires an independently selected reproducing-kernel or weighted rigging, so no positive Green bulk follows from convolution alone.

## Complex-evaluation RKHS test

Let \(\mathcal H\) be an analytic reproducing-kernel Hilbert space on a connected complex domain containing candidate zeros, and suppose multiplication by the completed scalar,

\[
(M_\xi f)(z)=
\xi\!\left(\tfrac12+z\right)f(z),
\]

is densely defined with each reproducing kernel \(k_w\) in the adjoint domain. Reproduction gives

\[
M_\xi^*k_w=
\overline{\xi(\tfrac12+w)}\,k_w.
\]

Consequently every complex scalar zero, on or off the critical axis, produces a positive-norm adjoint-kernel vector. RKHS positivity does not distinguish the desired locus.

Nor can this multiplication operator be selfadjoint on such a complex evaluation domain. Selfadjointness would make every displayed eigenvalue real, so the nonconstant holomorphic function \(w\mapsto\xi(\tfrac12+w)\) would take only real values on a connected open set. The open mapping theorem would then force it to be constant, a contradiction.

Thus bounded complex evaluations recover all zeros only by losing selfadjointness; restricting evaluations to a real line restores real spectral parameters only by defining away the off-axis question.

## de Branges--Hermite--Biehler test

Write

\[
\Xi(t)=\xi\!\left(\tfrac12+it\right).
\]

A de Branges realization with \(\Xi\) as its real spectral part would require a real entire \(B\) such that

\[
E=\Xi-iB
\]

is Hermite--Biehler:

\[
|E(z)|>|E^\#(z)|
\qquad (\operatorname{Im}z>0).
\]

This inequality gives a positive reproducing kernel, while the real part

\[
\frac{E+E^\#}{2}=\Xi
\]

has only real zeros, interlacing those of \(B\) under the nondegenerate hypotheses. Therefore constructing such an \(E\) with the stated real part already proves that every zero of \(\Xi\) is real; it is not a consequence of the existing theta Fourier representation.

The theta source canonically supplies \(\Xi\), but it supplies neither a companion \(B\) nor the Hermite--Biehler inequality. Choosing \(B\) by fitting the zeros inserts the desired conclusion. Choosing a differential companion such as \(B=\Xi'\) merely moves the missing theorem to the corresponding Hermite--Biehler or Laguerre inequality, which is at least as strong as the required real-zero property.

## Canonical derivative-companion test

Take the source-derived choice

\[
E(z)=\Xi(z)+i\Xi'(z).
\]

For real \(x\), the boundary expansion of the Hermite--Biehler modulus difference is controlled by the first Laguerre expression

\[
L_1(x)=\Xi'(x)^2-\Xi(x)\Xi''(x).
\]

At the center,

\[
L_1(0)=-\Xi(0)\Xi''(0)>0,
\]

because \(\Xi(0)>0\) and the positive theta kernel gives \(\Xi''(0)<0\). Thus the elementary central moment test passes, but it supplies only boundary-local information.

The full Hermite--Biehler inequality remains exactly the missing confinement statement. If \(z_0\) in the upper half-plane were a zero of \(\Xi\), then

\[
E(z_0)=i\Xi'(z_0),
\qquad
E^\#(z_0)=-i\Xi'(z_0),
\]

so their moduli are equal, contradicting strict Hermite--Biehler inequality. Proving the inequality for the derivative companion therefore excludes nonreal zeros directly; it is not derived by the central moment sign or by PF2 of the theta kernel.

## Laguerre-hierarchy strength test

For a real entire function of the completed scalar's order and genus, membership in the Laguerre--Pólya class is characterized by the full family of generalized Laguerre inequalities on the real axis. Equivalently, all associated Jensen polynomials must be hyperbolic. Membership forces every zero of

\[
\Xi(t)=\xi\!\left(\tfrac12+it\right)
\]

to be real.

The first inequality is the derivative-companion boundary expression

\[
\Xi'^2-\Xi\Xi''\ge0.
\]

Even if established globally, this single inequality is only one necessary member of the hierarchy. The theta moments determine every finite Jensen polynomial and every finite differential expression, but the source construction supplies no arrow from finitely many verified members to the unbounded hierarchy. Invoking the complete hierarchy proves the desired real-zero statement through the Laguerre--Pólya characterization and therefore cannot serve as an independently derived positivity premise.

Thus the hierarchy is a valid reformulation and a source-computable sequence of finite falsifiers, but not a completed confinement mechanism.

## First Laguerre source-integral test

Using

\[
\Xi(t)=\int_{\mathbb R}\Phi(x)e^{itx}dx,
\]

direct differentiation and symmetrization give

\[
\Xi'(t)^2-\Xi(t)\Xi''(t)
=\frac12\iint_{
\mathbb R^2}(x-y)^2
\Phi(x)\Phi(y)e^{it(x+y)}dxdy.
\]

After setting \(s=x+y\), this is the Fourier transform of the nonnegative even density

\[
H(s)=\frac14\int_{\mathbb R}d^2
\Phi\!\left(\frac{s+d}{2}\right)
\Phi\!\left(\frac{s-d}{2}\right)dd,
\]

up to the fixed Fourier normalization. Therefore global first-Laguerre positivity is equivalent to \(H\) having a nonnegative Fourier transform, or equivalently to the corresponding Bochner positive-definiteness property.

Pointwise positivity of \(H\), and strict log-concavity or PF2 of \(\Phi\), do not by themselves establish positive-definiteness of \(H\). The source calculation identifies the exact missing property but does not prove it. This separates the already proved positive mixture bound from the Fourier-sign condition required by the first global Laguerre inequality.

## Two-point Bochner minor

Let \(g=\log\Phi\). Evenness and strict concavity imply that, for each fixed \(d\),

\[
s\longmapsto
 g\!\left(\frac{s+d}{2}\right)
+g\!\left(\frac{s-d}{2}\right)
\]

is even, strictly concave, and maximized at \(s=0\). Therefore

\[
\Phi\!\left(\frac{s+d}{2}\right)
\Phi\!\left(\frac{s-d}{2}\right)
\le
\Phi\!\left(\frac d2\right)^2,
\]

strictly for \(s\ne0\). Integrating against \(d^2/4\) gives

\[
0<H(s)<H(0)
\qquad(s\ne0).
\]

Hence every two-point Bochner matrix

\[
\begin{pmatrix}
H(0)&H(s)\\
H(s)&H(0)
\end{pmatrix}
\]

is positive definite. This is a genuine consequence of the proved theta log-concavity, but positive-definiteness of a function requires all finite Bochner matrices. The first unproved gate is the three-point determinant; the two-point bound alone does not establish nonnegativity of the Fourier transform.

## Three-point Bochner test

For the equally spaced points \(0,s,2s\), write

\[
h_0=H(0),\qquad h_1=H(s),\qquad h_2=H(2s).
\]

The Bochner determinant factors exactly as

\[
\det
\begin{pmatrix}
h_0&h_1&h_2\\
h_1&h_0&h_1\\
h_2&h_1&h_0
\end{pmatrix}
=(h_0-h_2)
\left(h_0(h_0+h_2)-2h_1^2\right).
\]

The two-point theorem makes the first factor positive. Hence the new condition is

\[
H(s)^2\le
\frac{H(0)(H(0)+H(2s))}{2}.
\]

Even if log-concavity of \(H\) were established, it would give the differently directed bound

\[
H(s)^2\ge H(0)H(2s),
\]

so it does not settle the determinant. Expanding the new condition at \(s=0\) yields the necessary local inequality

\[
H(0)H^{(4)}(0)\ge H''(0)^2.
\]

Thus the first unresolved finite positive-definiteness gate has been reduced to an explicit three-point inequality, with a fourth-derivative source falsifier. No implication from the existing PF2 estimate supplies it.

## Disposition

The source-derived translation-invariant nonlocal operator is fixed and selfadjoint but does not turn scalar zeros into homogeneous Hilbert-space modes. Promoting point evaluations to states requires a rigged-space or boundary-functional construction, and any positivity or domain claim for that promotion is additional structure rather than a consequence of theta convolution.
