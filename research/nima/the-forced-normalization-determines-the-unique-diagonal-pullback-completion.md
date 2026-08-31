# The forced normalization determines the unique diagonal pullback completion

## Setup

On the algebraic finite-prime source

\[
c_{00}(\mathbb P)=\bigoplus_p\mathbb C e_p,
\]

the local Stokes-to-Wronskian comparison has forced positive scalar

\[
T_0e_p=\lambda_p f_p,
\qquad
\lambda_p=\frac{-\kappa_p}{2s_p}>0,
\]

where \((f_p)_p\) is the orthonormal prime basis of the declared unweighted
Wronskian coefficient target.

Although \(\lambda_p\to0\) superexponentially, this does not create an
algebraic radical: every \(\lambda_p\) is nonzero.  It does determine the
pullback metric exactly.

## Forced source form

Pulling the target Hilbert form back through \(T_0\) gives

\[
\langle x,y\rangle_{\mathrm{pb}}
:=\langle T_0x,T_0y\rangle_{\ell^2}
=\sum_p\lambda_p^2\overline{x_p}y_p.
\]

Hence

\[
\|e_p\|_{\mathrm{pb}}=\lambda_p.
\]

This diagonal weight is unique if all of the following are required:

1. the prime basis remains orthogonal;
2. the target basis \((f_p)\) remains orthonormal;
3. the comparison preserves the positive form.

Indeed, if \(\|e_p\|^2=w_p\), isometry on each basis vector forces
\(w_p=\lambda_p^2\).

## Completion and closed range

The pullback completion is

\[
\mathcal H_{\mathrm{pb}}
=
\left\{x=(x_p):
\sum_p\lambda_p^2|x_p|^2<\infty
\right\}.
\]

The algebraic map extends to

\[
T:\mathcal H_{\mathrm{pb}}\longrightarrow\ell^2(\mathbb P),
\qquad
(Tx)_p=\lambda_px_p.
\]

For every \(x\in\mathcal H_{\mathrm{pb}}\),

\[
\|Tx\|_{\ell^2}^2
=\sum_p\lambda_p^2|x_p|^2
=\|x\|_{\mathrm{pb}}^2.
\]

Conversely, for \(y\in\ell^2\), define \(x_p=y_p/\lambda_p\).  Then

\[
\sum_p\lambda_p^2|x_p|^2=\sum_p|y_p|^2<\infty,
\]

and \(Tx=y\).  Therefore

\[
T:\mathcal H_{\mathrm{pb}}\overset{\sim}{\longrightarrow}
\ell^2(\mathbb P).
\]

is unitary.  In particular, its range is closed and the completed form has
zero radical.

## What is and is not closed

This proves an abstract completion theorem: once the local comparison is
source-authorized and the source norm is its pullback metric, the apparent
superexponential loss disappears exactly, with no arbitrary normalization.

It does **not** prove that this weighted Hilbert completion is the global
rigged topology declared by the arithmetic constructor.  That identification
requires:

- deriving the same weights \(\lambda_p^2\) from the source Green form rather
  than selecting them after observing \(T_0\);
- proving compatibility with prime-power cutoff and the primitive/square/tail
  decomposition;
- showing that the other resolved and linking ports are continuous in the
  same common topology;
- proving that quotient radicals from the full pushout agree, not merely that
  this isolated diagonal form is nondegenerate.

Thus raw unweighted closed range is impossible, while pullback-weighted closed
range is automatic and uniquely normalized.  The remaining issue is source
identification of that completion.  No RH conclusion is authorized.
