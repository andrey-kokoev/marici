# The ordered Stokes linking form is bounded on the explicit wall graph

## Why the wall coordinate is necessary

On the rapid core, the ordered boundary identity is

\[
\langle O,Dv\rangle
=-\langle DO,v\rangle
=-2v(0),
\qquad
DO=2\delta_0.
\]

Point evaluation is not continuous in the bare Lebesgue \(L^2\) norm.  Thus
the Stokes linking form cannot extend to the resolved GNS carrier by itself.

The source construction already retains the wall as a separate boundary port.
Implement that typing explicitly.

## Joint GNS-plus-wall carrier

Let \(\mathcal D_{\rm wall}\) be the rapid source core containing all windows,
and define the wall graph embedding

\[
\mathcal E f
=
\bigl(\mathcal Rf,\gamma_0f\bigr),
\qquad
\gamma_0f=f(0),
\]

where

\[
\mathcal Rf=(f,Bf,M_\Phi f).
\]

Equip its graph with

\[
\|f\|_{G,\rm wall}^2
:=
\|\mathcal Rf\|_{\tau^{(3)}}^2+|\gamma_0f|^2.
\]

By construction,

\[
|\gamma_0f|
\le\|f\|_{G,\rm wall}.
\]

The completion is the closed graph of the wall trace over the resolved GNS
space.  The trace need not be bounded on all \(L^2\); it is bounded on this
source-authorized graph because its value is retained as an independent
coordinate.

## Bounded ordered Stokes functional

Define

\[
\mathfrak s(f):=-2\gamma_0f.
\]

Then

\[
|\mathfrak s(f)|
\le2\|f\|_{G,\rm wall}.
\]

Thus \(\mathfrak s\) extends uniquely and continuously to the completed wall
graph.

For the adjacent-window difference

\[
v_p=W_{2L}-W_L,
\]

one recovers

\[
\mathfrak s(v_p)
=-2v_p(0)
=4(H(L)-H(2L))
=s_p>0.
\]

Reversing the ordered slots changes the sign, as required by reciprocal
orientation.

## Linking polarization

Let \(c\in\mathbb R\) be any already source-derived loading coefficient on a
fixed labelled block.  The skew-Hermitian real boundary form becomes the
Hermitian complex linking polarization

\[
\mathfrak L_c(f,g)
:=ic\left(
\overline{\gamma_0f}\,\eta(g)
-\overline{\eta(f)}\,\gamma_0g
\right),
\]

where \(\eta\) denotes the retained incidence-level scalar coordinate.  On the
direct-sum wall/incidence graph,

\[
|\mathfrak L_c(f,g)|
\le2|c|\,\|f\|_{G,\rm wall}\|g\|_{G,\rm wall}
\]

after including \(|\eta|^2\) in the graph norm.

For the first-Adams primitive/square block, the source-derived arithmetic
loadings are \(-\kappa_p^{(k)}/2\).  Their absolute values are uniformly
bounded, so the direct sum of labelled linking forms is bounded on the
retained labelled wall graph.

## Radical compatibility

The positive resolved-plus-wall norm satisfies

\[
\|f\|_{G,\rm wall}^2
\ge(1+M_\Phi^2)\|f\|_2^2+|\gamma_0f|^2.
\]

Hence its radical is zero.  The bounded linking form vanishes automatically on
that zero radical, so it descends without ambiguity.

On each primitive/square two-column block, the previously proved determinant
margin shows that adding the source-oriented linking coefficient preserves
strict positivity, conditional on the completed cut/window mate realizing
that coefficient.  No new local scalar integration is required.

## What this closes

On the retained labelled GNS-plus-wall graph:

- the ordered Stokes functional is continuous;
- reciprocal slot reversal is continuous;
- arithmetic-loaded linking forms are uniformly bounded;
- the positive radical is zero and the linking form descends;
- finite label cutoffs commute with the construction.

## Remaining scope

This does not identify the plain Stokes wall coordinate with the
half-density Wronskian coordinate; that comparison still passes through the
cut-atom/twisted-history mate.  Nor does it authorize codiagonalization or
unlabelled prime pushforward.

The remaining local comparison gate is realization of the explicit
primitive/square mate coefficient on this completed joint graph.  The global
rigged pushout closed-range problem and connected tail remain open.  No RH
conclusion is authorized.
