# The plain Stokes-to-Wronskian ratio is only a candidate until half-density twisting

## Correction

The recent ratio

\[
\lambda_p^{\mathrm{cand}}
:=\frac{-\kappa_p}{2s_p},
\qquad
s_p=4(H(L)-H(2L)),
\]

was obtained by matching the numerical output of the plain boundary-Stokes
port to the completed-theta Wronskian output.  That ratio is algebraically
well defined and positive, but it is **not yet a source-authorized comparison
normalization**.

The earlier completion-trace audit already proves why.  Plain Volterra/Stokes
history detects the zero-frequency port, whereas the completion differential

\[
\mathcal C=(\partial_u-\tfrac12)(\partial_u+\tfrac12)
\]

has its natural traces at the two half-density characters

\[
M_-(g)=\int e^{-u/2}g(u)\,du,
\qquad
M_+(g)=\int e^{u/2}g(u)\,du.
\]

The Wronskian odd coordinate belongs to

\[
j_{1/2}=\frac{M_+-M_-}{\sqrt2},
\]

not to the plain zero-frequency jump.  Therefore dividing the Wronskian
output by \(s_p\) compares different spectral ports unless an exponentially
twisted history theorem first identifies them.

## What remains valid

The following calculations remain valid on their own carriers:

- the resolved mixed tail \(g_p\) is explicit and strictly positive;
- the ordinary two-window Gram has its closed erf determinant;
- the resolved determinant has a prime-uniform positive lower bound;
- the plain Stokes value \(s_p\) is positive and fixes its local ordered sign;
- the Euler-to-theta incidence \(\kappa_p\) is explicit, negative, and
  uniformly small;
- \(-\kappa_p/2\) is the completed-theta Wronskian output.

What is not valid without an additional theorem is treating
\(s_p\) and \(-\kappa_p/2\) as readouts of one already-identified generator.

## Status of the recent determinant margin

The matrix calculation

\[
\det
\begin{pmatrix}
a_p&r_p+i\ell_p\\r_p-i\ell_p&d_p
\end{pmatrix}
=
\Delta_p^{\mathrm{res}}-\ell_p^2
\]

is exact.  The uniform estimate

\[
\Delta_p^{\mathrm{res}}-rac{\kappa_p^2}{4}>0.244
\]

is also exact **for the candidate assignment**

\[
\ell_p=-\frac12\kappa_p.
\]

It does not prove that the source linking coefficient equals this candidate.
Accordingly, those packets close a conditional scalar hostile, not the typed
first-Adams assembly gate.

Likewise, the compactness and dense-nonclosed-range calculations for
\(\operatorname{diag}(\lambda_p^{\mathrm{cand}})\) classify that candidate
diagonal comparison only.  They do not classify the still-unconstructed
half-density-twisted comparison.

## Correct next calculation

Construct the twisted histories

\[
(H_-g)(u)=e^{u/2}\int_{-\infty}^u e^{-v/2}g(v)\,dv,
\]

\[
(H_+g)(u)=e^{-u/2}\int_{-\infty}^u e^{v/2}g(v)\,dv,
\]

on their relative graph domains, and compute the twisted window incidence

\[
s_p^{(1/2)}
:=j_{1/2}\bigl(\text{source-derived window boundary packet at }p\bigr).
\]

Only after proving that this packet is the mate of the retained Stokes
boundary generator may one define the typed comparison scalar

\[
\lambda_p^{(1/2)}
=\frac{-\kappa_p}{2s_p^{(1/2)}}.
\]

The equality \(s_p^{(1/2)}=s_p\) must not be assumed; it is precisely the
missing spectral-location comparison.

## Revised frontier

The earliest local gate is again the half-density-twisted history comparison,
not scalar positivity.  After it is constructed, one must recompute:

1. the actual linking magnitude \(\ell_p\);
2. the oriented determinant margin with that magnitude;
3. the all-prime topology of the genuine comparison;
4. common-domain continuity and radical descent.

No RH conclusion is authorized.
