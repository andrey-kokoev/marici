# The renormalized gamma--endpoint residual is not positive, so the prime Laplacian cannot be an orthogonal summand

## Exact finite-cutoff normalization

For a compactly supported source test \(f\), the completed quadratic form has the normalization

\[
Q(f)
=
E(f)
+
G(f)
-
\sum_{q}
a_q
\operatorname{Re}
\langle f,T_{\ell_q}f\rangle,
\]

where

\[
a_q
=
\frac{\Lambda(q)}{\sqrt q},
\qquad
\ell_q
=
\log q.
\]

In unitary Fourier coordinates, logarithmic source translation becomes

\[
(U_{\ell}m)(t)
=e^{it\ell}m(t).
\]

For a finite prime-power packet \(Q\), define

\[
A_Q
=
\sum_{q\in Q}a_q
\]

and

\[
\Phi_Qm
=
\bigoplus_{q\in Q}
\sqrt{a_q/2}
(I-U_{\ell_q})m.
\]

Then

\[
-\sum_{q\in Q}a_q
\operatorname{Re}
\langle m,U_{\ell_q}m\rangle
=
\|\Phi_Qm\|^2
-
A_Q\|m\|^2.
\]

The factor \(1/2\) in the edge feature is forced by the explicit-formula normalization.

## Gamma multiplier

With the fixed compact-support normalization, the archimedean form is

\[
G(m)
=
\int_{\mathbb R}
g_\Gamma(t)
|m(t)|^2dt,
\]

where

\[
g_\Gamma(t)
=
\frac12
\left(
\operatorname{Re}
\psi(1/4+it/2)
-
\log\pi
\right).
\]

The endpoint form is

\[
E(m)
=
\operatorname{Re}
\left(
m(i/2)
\overline{m(-i/2)}
\right)
\]

up to the already fixed Fourier normalization.

The residual left after extracting the positive prime Laplacian is therefore

\[
R_Q^{\Gamma,\partial}(m)
=
E(m)
+
\int g_\Gamma(t)|m(t)|^2dt
-
A_Q\|m\|^2.
\]

## Endpoint-annihilating packets

Fix \(t_0\in\mathbb R\). Let

\[
h_\varepsilon(z)
=
\exp
\left(
-
\frac{(z-t_0)^2}{2\varepsilon^2}
\right)
\]

and set

\[
m_\varepsilon(z)
=
(z^2+1/4)h_\varepsilon(z).
\]

Then

\[
m_\varepsilon(i/2)
=
m_\varepsilon(-i/2)
=0.
\]

Thus

\[
E(m_\varepsilon)=0.
\]

Normalize \(m_\varepsilon\) in real-boundary \(L^2\). Its squared modulus converges weakly to a point mass at \(t_0\). Continuity of the digamma multiplier gives

\[
\lim_{\varepsilon\downarrow0}
R_Q^{\Gamma,\partial}(m_\varepsilon)
=
g_\Gamma(t_0)-A_Q.
\]

## Negative witness

Whenever

\[
A_Q
>
g_\Gamma(t_0),
\]

the residual is negative on all sufficiently localized endpoint-annihilating packets.

The prime-power sum \(A_Q\) is unbounded under prime cutoff enlargement. Therefore, for every fixed \(t_0\), there are finite prime-power packets \(Q\) for which

\[
R_Q^{\Gamma,\partial}
\not\succeq0.
\]

The endpoint row cannot repair this failure because it vanishes identically on the witness packets.

## What is falsified

The completed form cannot be factored as an orthogonal positive sum

\[
Q_Q
=
\|\Phi_Q\cdot\|^2
+
\|\Phi_{\Gamma,\partial,Q}\cdot\|^2
\]

with

\[
\|\Phi_{\Gamma,\partial,Q}m\|^2
=
R_Q^{\Gamma,\partial}(m).
\]

Thus alternative 1 from the prime-Laplacian search is rejected: the renormalized gamma--endpoint residual has no independent positive Hilbert feature on the full analytic source.

## What is not falsified

The full arithmetic form remains

\[
Q_Q(m)
=
\|\Phi_Qm\|^2
+
R_Q^{\Gamma,\partial}(m).
\]

On a localized packet, the diagonal part of \(\|\Phi_Qm\|^2\) restores \(A_Q\), while its character terms reproduce the hostile prime cosine sum. Therefore negativity of the separated residual does not by itself decide positivity of \(Q_Q\).

It proves that the positive prime Laplacian and gamma--endpoint sector cannot remain orthogonal after renormalization.

## Required replacement

Any surviving positive carrier must couple the prime edge rows to the gamma--endpoint row before removing the diagonal bulk.

Equivalently, one needs a block Gram operator

\[
\mathcal G_Q
=
\begin{pmatrix}
L_Q & X_Q\\
X_Q^* & G_{\Gamma,\partial,Q}
\end{pmatrix}
\succeq0
\]

whose Schur or Witt reduction yields the completed form. The cross operator \(X_Q\) cannot be zero.

A purely diagonal comparison is also excluded by endpoint-annihilating localization and the aligned prime peak. The required coupling must be genuinely nonlocal or noncommuting in the analytic strip carrier.

## Tetrahedral meaning

The prime Laplacian belongs to the positive \(H_{234}\) realization, while the gamma--endpoint row belongs to the \(H_{134}\) boundary realization.

The negative witness shows that these two faces cannot be joined by orthogonal direct sum. Their missing positive tetrahedral cell must contain a nonzero mixed face \(X_Q\).

Thus the tetrahedral analysis predicts exactly the same requirement as the source calculation: the positive filler is a coupled block, not a sum of independently positive place sectors.

## Next gate

The remaining candidate is an exact source-derived mixed operator \(X_Q\) satisfying both:

\[
\mathcal G_Q\succeq0
\]

and

\[
\operatorname{Red}(\mathcal G_Q)
=
Q_Q.
\]

It must arise from the differentiated canonical/dual pairing or the Green boundary form. Choosing \(X_Q\) by Cholesky factorization of the target form would be circular.

## Disposition

The finite-cutoff calculation selects alternative 3: the renormalized gamma--endpoint residual is indefinite for sufficiently large prime packets.

The explicit positive prime Laplacian remains valid, but it cannot be an orthogonal summand of the completed positive carrier. A nonzero source-derived gamma--prime cross channel is necessary.
