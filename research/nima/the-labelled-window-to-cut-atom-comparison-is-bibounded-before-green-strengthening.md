# The labelled window-to-cut-atom comparison is bi-bounded before Green strengthening

## Keep the prime-grade fibers

The algebraic comparison

\[
J_0(q_{a_{p,k}})=u_{p,k}
\]

must be completed on the retained labelled direct sum, not after collapsing all
fronts into one unlabelled \(L^2(\mathbb R)\) space.

Let

\[
\mathcal H_F
=
\bigoplus_{p,k}^{\ell^2}
\operatorname{span}\{q_{a_{p,k}}\},
\]

with each front fiber carrying its ordinary \(L^2\) norm, and let

\[
\mathcal H_I
=
\bigoplus_{p,k}^{\ell^2}
\operatorname{span}\{u_{p,k}\},
\]

with the theta cut norm.  Different labels are orthogonal by construction.
Euler coefficients may be inserted diagonally on both sides and cancel from
the comparison estimates.

## Uniform front norms

For \(a>0\),

\[
q_a=U_{-a}f_0-U_af_0.
\]

The translated Gaussian Gram gives

\[
\|q_a\|_2^2
=2\|f_0\|_2^2-2\langle U_{-a}f_0,U_af_0\rangle
=\sqrt2\left(1-e^{-2\pi a^2}\right).
\]

This function is strictly increasing because

\[
\frac d{da}\|q_a\|_2^2
=4\sqrt2\pi a e^{-2\pi a^2}>0.
\]

Every prime-power scale obeys

\[
a_{p,k}=k\log p\ge\log2.
\]

Hence

\[
0<m_F^2
:=\sqrt2\left(1-e^{-2\pi(\log2)^2}\right)
\le\|q_{a_{p,k}}\|_2^2.
\]

Also, translated Gaussians become orthogonal at large separation, so directly
from the triangle inequality,

\[
\|q_a\|_2\le2\|f_0\|_2=:M_F.
\]

Thus all labelled front fibers have uniformly equivalent scalar norms.

## Uniform cut-atom norms

The exact theta cut identity gives

\[
\|u_{p,k}\|_{\mathrm{cut}}^2
=\|g_{a_{p,k}}\|_2^2+
\|h_{a_{p,k}}\|_2^2
=\|\Phi\|_2^2.
\]

Therefore every cut-atom fiber has the same nonzero norm

\[
m_I=M_I=\|\Phi\|_2.
\]

## Bi-bounded extension

For a finite labelled packet \(c=(c_{p,k})\),

\[
\left\|\sum c_{p,k}q_{a_{p,k}}\right\|_{\mathcal H_F}^2
=
\sum|c_{p,k}|^2\|q_{a_{p,k}}\|_2^2,
\]

while

\[
\left\|J_0\sum c_{p,k}q_{a_{p,k}}\right\|_{\mathcal H_I}^2
=
\|\Phi\|_2^2\sum|c_{p,k}|^2.
\]

Consequently

\[
\frac{\|\Phi\|_2}{M_F}\|x\|_{\mathcal H_F}
\le
\|J_0x\|_{\mathcal H_I}
\le
\frac{\|\Phi\|_2}{m_F}\|x\|_{\mathcal H_F}.
\]

Thus \(J_0\) extends uniquely to a boundedly invertible map

\[
{
J:\mathcal H_F\overset\sim\longrightarrow\mathcal H_I.
}
\]

Its graph is closed, its range is closed, and neither side has a comparison
radical.

## Why label retention is essential

If all fronts are first summed in one unlabelled \(L^2\) carrier, nearby
logarithmic scales can nearly cancel.  The cut atoms have a moving seam jump
and need not obey the same cancellation estimate.  No bi-bounded theorem is
claimed after that pushforward.

The proof works because prime and grade idempotents remain orthogonal in the
source-labelled completion.  This is exactly the carrier on which the
first-Adams constructor and theta incidence were proved labelwise.

## Remaining Green gate

This closes ordinary labelled-Hilbert graph closure of the endpoint--cut
comparison.  It does not yet show equivalence after strengthening the front
norm to the selected resolved Green norm

\[
(1+M_\Phi^2)\|q_a\|_2^2+\|Bq_a\|_2^2,
\]

or after adding the ordered linking polarization.  The next theorem must prove
uniform comparison of that strengthened norm with the cut-atom Green norm on
each labelled fiber and then verify radical compatibility.

Nor does this result authorize unlabelled prime pushforward.  Full global
pushout closed range remains open.  No RH conclusion is authorized.
