# The resolved Green strengthening is uniform on every labelled front fiber

## Scope correction

This packet proves norm equivalence for the differentiated fronts \(q_a\) when
the resolved formula is applied to those fronts. It does **not** transport the
primitive windows \(W_a\), whose norms grow like \(\sqrt a\). See
`the-bibounded-comparison-is-only-at-the-differentiated-front-level.md`.

## Bounded resolved tail

The selected resolved form is

\[
\|f\|_{\mathrm{res}}^2
=(1+M_\Phi^2)\|f\|_2^2+\|Bf\|_2^2,
\qquad
B=H_\Phi-M_\Phi I.
\]

The causal theta convolution obeys

\[
\|H_\Phi\|\le M_\Phi.
\]

Therefore

\[
\|B\|
\le\|H_\Phi\|+M_\Phi
\le2M_\Phi.
\]

For every \(f\in L^2\),

\[
(1+M_\Phi^2)\|f\|_2^2
\le
\|f\|_{\mathrm{res}}^2
\le
(1+5M_\Phi^2)\|f\|_2^2.
\]

Thus the resolved norm is globally equivalent to the ordinary Hilbert norm on
the full bilateral carrier, not merely on the window span.

## Labelled reciprocal fronts

For

\[
q_a=U_{-a}f_0-U_af_0,
\qquad
a=k\log p\ge\log2,
\]

the ordinary norm satisfies

\[
m_F^2
\le\|q_a\|_2^2
\le M_F^2
\]

with prime- and grade-independent constants.  Combining the estimates gives

\[
(1+M_\Phi^2)m_F^2
\le
\|q_a\|_{\mathrm{res}}^2
\le
(1+5M_\Phi^2)M_F^2.
\]

Hence every labelled one-dimensional front fiber has a uniformly equivalent
resolved norm.

On the orthogonal prime-grade direct sum,

\[
\mathcal H_F^{\mathrm{res}}
=
\bigoplus_{p,k}^{\ell^2}
\left(\operatorname{span}\{q_{k\log p}\},
\|\cdot\|_{\mathrm{res}}\right),
\]

the identity map

\[
\mathcal H_F\longleftrightarrow\mathcal H_F^{\mathrm{res}}
\]

is bounded in both directions.

## Consequence for the cut-atom comparison

The previously constructed map

\[
J:\mathcal H_F\overset\sim\longrightarrow\mathcal H_I
\]

is bi-bounded.  Composing with the resolved/ordinary norm equivalence yields a
bi-bounded map

\[
{
J:\mathcal H_F^{\mathrm{res}}
\overset\sim\longrightarrow\mathcal H_I
}
\]

when the cut side carries its exact theta-cut \(L^2\) norm.

Thus strengthening the **differentiated front side** by this bounded graph
term does not destroy closed graph, closed range, or zero radical on the
labelled source-generated comparison. This is not yet the primitive-window
resolved comparison used by the first-Adams positive Gram.

## Why the full Green comparison is not yet closed

The seam component

\[
h_a(t)=\mathbf1_{t\le a}\Phi(a-t)
\]

has a moving jump at \(t=a\).  Its distributional derivative contains a wall
delta.  Therefore one cannot silently replace the cut \(L^2\) norm by an
ordinary Sobolev graph norm.  The cut carrier requires its declared
wall-extended Green form, with the jump stored in a separate boundary port.

The remaining theorem is now one-sided and precise:

> Prove that the wall-extended cut-atom Green norm is uniformly equivalent to
> its exact cut \(L^2\) norm on the labelled source-generated range, or compute
> its additional boundary weight and compare that weight with the resolved
> front form.

The resolved front side itself is no longer the obstruction.  Ordered linking
continuity, wall-radical descent, and unlabelled global pushforward remain
open.  No RH conclusion is authorized.
