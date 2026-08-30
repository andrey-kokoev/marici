# The resolved disagreement return is trace class with an explicit margin bound

## Inputs

Let

\[
J_{\mathrm{dis}}:
\ell^2(\mathbb P)
\longrightarrow
\mathcal H_{\mathrm{aux}}
\]

be the prime-labelled disagreement incidence. The super-polynomial window
estimate gives

\[
J_{\mathrm{dis}}\in\mathfrak S_1
\subset
\mathfrak S_2.
\]

Let the reciprocal theta-history blocks be

\[
D_\pm
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi).
\]

If

\[
M_\Phi<1,
\]

then

\[
D_\pm
\ge
\frac{(1-M_\Phi)^2}{2}I,
\]

and therefore

\[
\|D_\pm^{-1}\|
\le
\frac{2}{(1-M_\Phi)^2}.
\]

## Schur return

Define the endpoint return

\[
R_\pm
=
J_{\mathrm{dis}}^*
D_\pm^{-1}
J_{\mathrm{dis}}.
\]

Because \(J_{\mathrm{dis}}\) is Hilbert--Schmidt and
\(D_\pm^{-1}\) is bounded,

\[
R_\pm\in\mathfrak S_1.
\]

Moreover,

\[
\|R_\pm\|_{\mathfrak S_1}
\le
\|D_\pm^{-1}\|
\|J_{\mathrm{dis}}\|_{\mathfrak S_2}^2,
\]

so

\[
\|R_\pm\|_{\mathfrak S_1}
\le
\frac{2}{(1-M_\Phi)^2}
\sum_p
\|d_p\|_\nu^2.
\]

This is a finite, cutoff-independent bound.

## Positivity

Each \(D_\pm^{-1}\) is positive. Hence

\[
R_\pm\ge0.
\]

The return is therefore a positive trace-class endpoint correction on each
reciprocal sheet.

Its sheet difference

\[
R_+-R_-
\]

is self-adjoint trace class and carries the resolved reciprocal orientation.

## Finite-cutoff convergence

Let

\[
J_X=J_{\mathrm{dis}}P_X,
\qquad
R_{\pm,X}=J_X^*D_\pm^{-1}J_X.
\]

Since

\[
J_X\to J_{\mathrm{dis}}
\]

in Hilbert--Schmidt and trace norm,

\[
R_{\pm,X}\to R_\pm
\]

in trace norm.

Thus every Fredholm determinant built from a declared bounded scalar multiple
of \(R_{\pm,X}\) converges locally uniformly to the completed determinant.

## Determinant availability

For any bounded parameter \(z\),

\[
\det(I-zR_\pm)
\]

is an ordinary Fredholm determinant.

This determinant is authorized at the disagreement Schur-return level because
the operator is trace class. It does not authorize a determinant for the full
multiplication remainder, which remains noncompact on the continuous
analytic carrier.

## Euler-weighted version

If the source incidence includes coefficients \(a_p\), replace
\(d_p\) by \(a_pd_p\). Then

\[
\|R_{\pm,a}\|_{\mathfrak S_1}
\le
\frac{2}{(1-M_\Phi)^2}
\sum_p|a_p|^2\|d_p\|_\nu^2.
\]

Every fixed polynomial-order Euler profile is admissible because the
disagreement norms decay super-polynomially.

## Exact-normalization qualification

The bound uses the completed convolution in the normalization for which

\[
\|H_\Phi\|=M_\Phi<1.
\]

If the history carries a coefficient \(\alpha_p\) or wall scale
\(\lambda_p\), the inverse bound becomes

\[
\|D_{p,\pm}^{-1}\|
\le
\frac{2}{
\left(
\sqrt{\lambda_p}
-
|\alpha_p|M_\Phi
\right)^2
}.
\]

Uniform trace-class control requires a uniform positive denominator.

## What this closes

Conditional on the already isolated wall/history normalization diagram, the
entire analytic Schur-return chain is complete:

\[
\text{trace-class incidence}
\longrightarrow
\text{bounded reciprocal resolvent}
\longrightarrow
\text{positive trace-class return}
\longrightarrow
\text{Fredholm determinant}.
\]

No local endpoint inverse is used.

## Remaining constructor gate

The return is analytically valid, but the first Adams edge still requires the
quadratic Green identity proving that this specific incidence and resolvent
are the source pullback of the window-to-theta comparison.

Only after that identity may the determinant be interpreted as an arithmetic
Adams-cell invariant.

## Hostile

Form the same return using normalized unit disagreement vectors. The incidence
ceases to be compact, and the trace-class proof fails even though every
finite-prime Schur complement exists.

## Frontier

The completion architecture is now forced:

\[
\text{soft disagreement}
\xrightarrow{\mathfrak S_1}
\text{theta auxiliary resolvent}
\xrightarrow{}
\text{trace-class endpoint return}.
\]

The live obstruction is source functoriality, not operator completion.
