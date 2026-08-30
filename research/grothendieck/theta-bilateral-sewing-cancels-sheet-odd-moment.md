# Completed bilateral sewing cancels the sheet-odd shear moment

Status: exact cancellation of one declared defect line; full Green descent
remains open

On the positive tail chart, the arithmetic shear has forcing

\[
 g_a(r)=(ar-1)f(r),
 \qquad r\ge0,                                        \tag{1}
\]

and Clark reflection gives `g_{-a}(r)=(-ar-1)f(r)`.  Therefore

\[
 \int_0^\infty(g_a^2-g_{-a}^2)dr
 =-4a\int_0^\infty r f(r)^2dr\ne0.                  \tag{2}
\]

This is the correct one-sided result.

## The completed forcing is even on oriented scale

After all-prime aggregation, the source forcing is

\[
 \mathfrak f(r)=e^{-r/2}\Phi(r),
 \qquad r\ge0.                                       \tag{3}
\]

The completed theta kernel is even under modular reflection.  Introduce the
oriented bilateral scale coordinate `q in R`; the two tail charts sew to

\[
 \boxed{
 \mathfrak f_{\rm bil}(q)
 =e^{-|q|/2}\Phi(|q|),
 }                                                     \tag{4}
\]

which is even.

The global fold is one operator `1-aq`, not two unrelated one-sided folds.
Its two Clark orientations have squared forcing difference

\[
 [(aq-1)^2-(-aq-1)^2]\mathfrak f_{\rm bil}(q)^2
 =-4aq\,\mathfrak f_{\rm bil}(q)^2.                  \tag{5}
\]

The integrand is odd.  Absolute convergence follows from the completed theta
decay, so

\[
 \boxed{
 \int_{\mathbb R}
 [(aq-1)^2-(-aq-1)^2]
 \mathfrak f_{\rm bil}(q)^2dq=0.
 }                                                     \tag{6}
\]

Thus the sheet-odd first-moment defect cancels exactly after genuine
bilateral modular sewing.

## Why this is not the premature cancellation

Equation (6) uses two facts absent from the positive-tail calculation:

1. all arithmetic labels have first been aggregated into the completed even
   kernel `Phi`; and
2. the two charts are represented by one oriented coordinate `q`, so modular
   reflection acts as `q -> -q`.

For the primitive one-sided seed, extending `f(r)` evenly is not a
label-preserving modular operation.  Applying (6) before arithmetic
completion would therefore be illegitimate.  The cancellation is supplied
by completed modular sewing, not by spectral independence of the norm line.

## Updated defect count

At the fully completed bilateral forcing level, the architecture returns to

\[
 \boxed{
 \text{positive sheared bulk}
 +\text{arithmetic aggregation/sewing}
 -\text{primitive seam line}.
 }                                                     \tag{7}
\]

This removes only the sheet-odd norm moment.  It does not yet prove that:

- the two sheared bulk kernels sew with the required sign;
- sampling introduces no additional cross-label defect; or
- the arithmetic logarithmic cocycle dominates the primitive seam.

The next full identity must apply the Green form on the oriented bilateral
scale before projecting to the scalar Clark output.  Any derivation that
subtracts two positive-half-line norm formulas and stops at (2) has not yet
performed the modular sewing represented by (4).
