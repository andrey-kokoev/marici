# The oriented first-Adams two-by-two block has one exact determinant margin

## Typed assembly

Let the resolved positive two-window block be

\[
G_p^{\mathrm{res}}
=
\begin{pmatrix}
a_p&r_p\\ r_p&d_p\end{pmatrix},
\]

where

\[
\begin{aligned}
a_p&=(1+M_\Phi^2)\|W_L\|^2+\|BW_L\|^2,\\
d_p&=(1+M_\Phi^2)\|W_{2L}\|^2+\|BW_{2L}\|^2,\\
r_p&=(1+M_\Phi^2)\langle W_L,W_{2L}\rangle+g_p,
\end{aligned}
\]

and \(g_p>0\) is the explicit autocorrelation difference already computed.
All three entries are real.

Suppose a source-authorized assembly adds the independently oriented linking
polarization

\[
J_p=
\begin{pmatrix}0&i\ell_p\\-i\ell_p&0\end{pmatrix},
\qquad \ell_p\in\mathbb R.
\]

Then the complete local Hermitian block is

\[
G_p=G_p^{\mathrm{res}}+J_p
=
\begin{pmatrix}
a_p&r_p+i\ell_p\\r_p-i\ell_p&d_p\end{pmatrix}.
\]

This addition is meaningful only after the positive and linking forms have
been transported to the same carrier.  The calculation below is conditional
on that typed assembly theorem.

## Exact positivity criterion

Because \(a_p,d_p>0\), the two-by-two Hermitian block is positive definite if
and only if

\[
\det G_p>0.
\]

Directly,

\[
\det G_p
=a_pd_p-|r_p+i\ell_p|^2
=a_pd_p-r_p^2-\ell_p^2.
\]

Define the resolved area margin

\[
\Delta_p^{\mathrm{res}}:=a_pd_p-r_p^2>0.
\]

Therefore

\[
G_p>0
\iff
\ell_p^2<\Delta_p^{\mathrm{res}}.
\]

Semidefinite descent uses \(\le\), with equality producing a one-dimensional
local radical.

Thus orientation does not alter either diagonal and does not interfere
linearly with the real mixed-tail entry.  It consumes the resolved determinant
margin quadratically.

## Arithmetic normalization

The Stokes readout gives \(s_p>0\), while the theta/Wronskian arithmetic
readout gives

\[
-\frac12\kappa_p>0.
\]

If the typed comparison is constructed with forced scalar
\(\lambda_p=-\kappa_p/(2s_p)\), then the transported linking magnitude is

\[
\ell_p=\lambda_ps_p=-\frac12\kappa_p.
\]

Under that normalization, the exact local positivity gate becomes

\[
\frac{\kappa_p^2}{4}<\Delta_p^{\mathrm{res}}.
\]

This removes \(s_p\) from the final determinant because it is precisely the
boundary normalization divided out by the typed comparison.

## What remains to evaluate

The oriented four-unit problem is therefore not four unrelated identities.
After carrier compatibility is proved, it has one scalar margin:

\[
\Delta_p^{\mathrm{res}}-\frac{\kappa_p^2}{4}.
\]

The incidence term tends to zero superexponentially.  That fact alone does not
supply a uniform margin, because the resolved determinant may also degenerate
with the moving windows.  A proof must compare their rates in the same
source-authorized normalization and check all finite exceptional primes.

The exact remaining steps are:

1. prove the typed assembly map placing both forms on one carrier;
2. evaluate or bound \(\Delta_p^{\mathrm{res}}\) from the explicit window and
   resolved-tail data;
3. prove strict positivity of
   \(\Delta_p^{\mathrm{res}}-\kappa_p^2/4\);
4. establish cutoff-uniform behavior in the declared global topology.

No endpoint Stieltjes metric is substituted in this criterion.  No RH
conclusion is authorized.
