# Orthogonal boundary coupling constructs a conservative wall--theta-profile extension

## Two boundary systems

Retain two distinct channels.

The native wall system has a boundary relation

\[
(\Gamma_0^{\mathrm w},\Gamma_1^{\mathrm w})
\]

on the broken-history graph. Its Green boundary form is

\[
\langle \Gamma_1^{\mathrm w}f,
\Gamma_0^{\mathrm w}g\rangle
-
\langle \Gamma_0^{\mathrm w}f,
\Gamma_1^{\mathrm w}g\rangle.
\]

The interior theta-profile system has the source-derived gamma-field and Weyl
family

\[
\gamma_\theta(\lambda)
=(A-\lambda)^{-1}B_\theta,
\qquad
M_\theta(\lambda)
=B_\theta^*(A-\lambda)^{-1}B_\theta,
\]

with its principal-value and zero-mode boundary coordinates on the seam.

No equality between the native wall adjoint and `B_theta` is assumed.

## Orthogonal coupling relation

On the direct-sum graph, couple the two systems through their common labelled
boundary source `c` by imposing

\[
\Gamma_0^{\mathrm w}f=c,
\]

and

\[
\Gamma_1^{\mathrm w}f+M_\theta(\lambda)c=0.
\]

Equivalently, the wall impedance is terminated by the theta Weyl response.
This is the standard orthogonal boundary-triplet coupling pattern: the two
Green boundary forms enter with opposite orientations and cancel on the
interface relation.

For two coupled vectors `(f,c)` and `(g,d)`, substitution gives

\[
\begin{aligned}
&\langle \Gamma_1^{\mathrm w}f,d\rangle
-\langle c,\Gamma_1^{\mathrm w}g\rangle\\
&\quad+
\langle M_\theta(\lambda)c,d\rangle
-\langle c,M_\theta(\mu)d\rangle
=0
\end{aligned}
\]

at equal real boundary parameter, with the off-diagonal parameter defect
controlled by the Weyl divided-difference identity.

## Arithmetic backreaction

The interior Weyl response is not merely a scalar impedance. Expanding it
gives

\[
M_\theta(\lambda)c
=
B_\theta^*(A-\lambda)^{-1}B_\theta c.
\]

Thus the coupled lower equation contains both source incidence and its
contragredient return. The missing backreaction row is supplied by the same
`B_theta` that generates the interior profiles, rather than by the native
adjoint of endpoint evaluation.

This avoids the disproved identities

\[
B_\theta=\pi_0^*,
\qquad
B_\theta=\Gamma_{\mathrm{wall}}^*.
\]

## Seam decomposition

On the seam, replace `M_theta` by its generalized boundary pair

\[
M_{\theta,\pm}(x)
=
B_\theta^*\operatorname{pv}(A-x)^{-1}B_\theta
\pm i\pi B_\theta^*\delta(A-x)B_\theta.
\]

The first term is the ordered Hardy backreaction. The second is the retained
zero-mode/endpoint packet. Both enter the interface relation, so conservative
closure does not discard the full relative response coordinate.

Upper and lower boundary values give the two reciprocal orientations. Their
jump is positive in the spectral measure sense, while their mean retains the
odd ordered current.

## Cutoff and completion

At finite label cutoff the construction is an ordinary finite-dimensional
boundary coupling over a closed history graph. Prime and grade cutoffs commute
with `B_theta`, the source-pulled metric, and the wall traces. Consequently the
coupled relations form a projective family.

Completion is authorized on the retained joint graph because the source
coordinate remains present and both boundary channels are continuous there.
No claim of closed range after a source-forgetting codiagonal is needed.

## What this constructs

This gives a conservative extension with:

1. native geometric wall traces;
2. interior theta-profile incidence;
3. ordered Hardy backreaction;
4. zero-mode endpoint residue;
5. reciprocal upper/lower Weyl charts;
6. a source-retaining arithmetic lower row.

It is a new source-derived coupled extension. It is not yet identified with
the historically named `C_FP` operator or with an independently physical G4
realization. Such identification requires equality of their graph domains,
boundary relations, and Green forms on a common core; type compatibility and
the scalar functional equation are insufficient.
