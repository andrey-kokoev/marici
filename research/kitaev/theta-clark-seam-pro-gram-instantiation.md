# Theta Clark--seam pro-Gram instantiation stops at missing arithmetic incidence

## Requested common feature map

The proposed cutoff output is

\[
J_Xc=(G_X+f_X,;a\partial_zG_X,;H_X,;P_X,;Q_X).
\]

The current source packets do not yet define these five entries as rows on one
common finite state module:

- \(G_X+f_X\) is source-derived on the \(q\)-flow graph domain;
- \(a\partial_zG_X\) is a source-derived Clark feature;
- \(H_X\) is an independent seam component in the tail--seam direct sum;
- arithmetic primitive and prime-square densities are typed, but their
  incidence maps into the retained boundary module are explicitly missing.

The archimedean row and the full mixed Green residual matrix are likewise not
supplied. Consequently \(J_X\), \(K_X\), the full \(Q_{F,X}\), and the finite
dynamics \((A_X,R_X)\) cannot yet be assembled as the requested matrices.

## First exact incidence witness

The smallest honest common-carrier typing model has five named coordinates
and only the first three admitted:

\[
Q_{m partial}=\operatorname{diag}(1,1,1,0,0).
\]

The primitive and square target rows are \(e_4^T\) and \(e_5^T\). Their
kernel witnesses are \(e_4\) and \(e_5\):

\[
Q_{m partial}e_4=0,
\quad e_4^Te_4=1,
\qquad
Q_{m partial}e_5=0,
\quad e_5^Te_5=1.
\]

This is not a fitted numerical theta model. It is the exact incidence matrix
of the present type inventory. It decides the requested trichotomy at the
earliest possible gate:

\[
\boxed{\text{typed kernel/continuity obstruction}.}
\]

No generalized eigenvalue exists until the missing rows are constructed.

## Endpoint correction

The unnormalized Fourier candidate

\[
w_a=|\widehat\Phi|^2+a^2|\widehat\Phi'|^2
\]

would control a representing kernel only if the Clark derivative acted on
the coefficient Fourier multiplier as assumed. Grothendieck's correction
shows that

\[
\partial_zG(q,z)
=ie^{-q/2}\int_0^\infty r\phi(q+r)e^{izr}\,dr
\]

differentiates the relative tail coordinate. No intertwiner to
\(\widehat\Phi'/\widehat\Phi\) has been derived. Therefore the reciprocal
weight integral is an abstract conditional criterion, not an instantiated
theta endpoint test.

The actual source-native endpoint repair is the \(q\)-flow identity. After
gauging \(1-s=a+ib\),

\[
\|G+f\|_2^2
=\|h'\|_2^2+a^2\|h\|_2^2+a|h(0)|^2.
\]

For \(a=1/2\), its finite feature matrix is

\[
Q_{\rm graph}=\operatorname{diag}(1,1/4,1/2),
\]

and endpoint evaluation has sharp squared domination constant \(2=1/a\).
Generally,

\[
|G(0)|^2\le\frac1{1-\Re s}\|G+f\|_2^2,
\]

uniformly on compact sets bounded away from \(\Re s=1\).

## What is already decided

1. The one-sided first-order tail channel is injective and closed-range in
   each open sector; ordinary tail completion escape is excluded there.
2. The seam is not a bounded function of the tail: translated atoms satisfy
   \(\|g_p\|\to0\) while \(\|h_p\|\to\|\Phi\|_2\).
3. Retaining the seam repairs translation escape, but the full synthesis is
   not bounded below on unrestricted coefficient packets because
   high-frequency modulation escapes through decay of \(\widehat\Phi\).
4. The authorized three-stage subsystem \(\{S,R_f,D\}\) is coherent in both
   allowed orders, with zero typed braid residual.
5. Arithmetic \(P,Q\) cannot be adjoined until their maps from the
   valuation/Fock carrier into the boundary carrier are constructed.

Thus finite feature-Gram positivity does not authorize a full observability
claim. The full Gramian \(W_X(L)\) and the commutator \([A_X,R_X]\) are not
typed matrices yet.

## Required next source packet

Grothendieck must supply, on one labelled cutoff module:

\[
P_X,Q_X:\mathcal H_{\rm valuation/Fock,X}	o
\mathcal H_{\rm boundary,X},
\]

the archimedean incidence row, the full mixed Green matrix, and the action of
the finite dynamics and sheet involution. Only then can the compiler compute
kernel witnesses, minimal fixed constructor families, sharp constants, PBH
ranks, and completion-stable bounds.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_theta_clark_seam_pro_gram_instantiation.py
```

The checker verifies the source packet dispositions, exact partial-incidence
kernel witnesses, and the rational \(a=1/2\) endpoint graph certificate.
