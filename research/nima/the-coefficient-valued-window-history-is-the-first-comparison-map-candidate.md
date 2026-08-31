# The coefficient-valued window history is the first comparison-map candidate

## Question

Where should arithmetic window incidence land before analytic multiplication?

## Claim boundary

It should first land in the coefficient-valued cell feature space. This gives an exact finite labelled comparison map, but not yet its Green metric or completion theorem.

## Carrier order

The source distinguishes the coefficient-valued history

\[
\mathfrak h_p:t\longmapsto[W_t]\in\mathcal F_{\rm cell}
\]

from its multiplication representation

\[
\operatorname{Mult}([W_t])=M_{W_t}.
\]

Constructing incidence in \(\mathcal F_{\rm cell}\) preserves the one-dimensional wall direction instead of prematurely representing it by an infinite-rank identity.

## Finite candidate

For labelled primitive and square atoms, define

\[
J_p^{\rm cell}e_{p,1}=[W_{\log p}],
\qquad
J_p^{\rm cell}e_{p,2}=[W_{2\log p}].
\]

Then

\[
J_p^{\rm cell}(e_{p,2}-e_{p,1})
=[W_{2\log p}-W_{\log p}],
\]

and

\[
\operatorname{Mult}J_p^{\rm cell}(e_{p,2}-e_{p,1})=D_p.
\]

Thus the map has the correct prime label, grade orientation, adjacent-window defect, and wall typing.

## Arithmetic weights remain external

The source coefficients act on the labelled atoms:

\[
e_{p,1}\longmapsto p^{-1/2-\sigma-it}e_{p,1},
\qquad
e_{p,2}\longmapsto\frac12p^{-1-2it}e_{p,2}.
\]

They are not rescalings of \([W_t]\). Keeping weights separate preserves Adams naturality and permits an independent Euler half-density audit.

## Exact scope

At finite cutoff the candidate supplies prime diagonality and the correct oriented endpoint difference. It does not supply a Green lift. That requires a polarized cell-feature form \(g_p^{\rm cell}\) whose represented image equals the analytic relative Green boundary form with the frozen adjoint orientation.

The required representation square includes

\[
\operatorname{Mult}(\partial_t\mathfrak h_p)
=\partial_t\operatorname{Mult}(\mathfrak h_p)
\]

on a common Green core. Endpoint representation alone is formal; derivative compatibility depends on the Green topology.

## Hostile

Choose a feature metric making \([W_{\log p}]\) and \([W_{2\log p}]\) orthogonal while retaining their correct multiplication representations. The feature assignment and scalar window identity pass, but the mixed Green block vanishes. Hence the feature form, not the vector-space assignment alone, carries the remaining content.

## Disposition

The first finite comparison map is explicit:

\[
e_{p,k}\longmapsto[W_{k\log p}],\qquad k=1,2.
\]

The remaining theorem is to construct the polarized cell-feature Green form making this map cutoff-natural, radical-compatible, oriented, and correctly represented by multiplication. No RH conclusion is authorized.
