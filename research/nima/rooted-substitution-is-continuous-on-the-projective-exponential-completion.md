# Rooted substitution is continuous on the projective exponential completion

## Scope

This closes the generic `R x H` face on the already declared typed valuation carrier

\[
\mathcal A_{\exp}=\bigcap_{\delta>0}\ell^1(\mathcal M,e^{\delta\ell};T),
\]

for scalar/rooted-subtree substitutions represented by typed convolution. It does not extend the theorem to nontransverse loaded physical divisors.

## Multilinear estimate

For every `delta > 0`, the source supplies

\[
q_\delta(c*d)\le q_\delta(c)q_\delta(d),
\qquad
q_\delta(c)=\sum_\nu e^{\delta\ell(\nu)}\|c_\nu\|.
\]

Let `tau` be a finite rooted tree and label its vertices by packets `c_v`. Evaluate the tree by convolution along its internal edges. Induction on the number of vertices gives

\[
q_\delta(\operatorname{ev}_\tau((c_v)))
\le
\prod_{v\in V(\tau)}q_\delta(c_v).
\]

Hence every finite rooted-substitution map is jointly continuous for every projective seminorm. Associativity of typed convolution makes the value independent of binary parenthesization, and grafting trees becomes composition of these continuous multilinear maps.

By the universal property of completion, every such map extends uniquely to the projective completion. If

\[
\kappa:\mathcal A_{\mathrm{fin}}\to\widehat{\mathcal A}_{\exp}
\]

is the dense completion map, uniqueness gives the strict naturality square

\[
\kappa\,H_\tau
=
\widehat H_\tau\,\kappa^{\times V(\tau)}.
\]

Thus the generic `R x H` face is strict on this carrier.

## Finite cutoff compatibility

For a downward-closed valuation cutoff `M_X`, positivity of the valuation monoid implies that an output coefficient with `ell(nu) <= X` can only receive convolution contributions from inputs satisfying the same cutoff. Therefore

\[
P_X(c*d)=P_X(P_Xc*P_Xd).
\]

This is stronger than Fourier cutoff behavior: rooted convolution has no omitted-to-visible leakage on downward valuation cutoffs. Iteration gives the same identity for every rooted tree.

## Coherence

The extension is not one map chosen separately at each of 64 `R x H` square instances. One continuous rooted operad action extends to completion. Operadic grafting, units, and associahedral identifications survive because continuous maps agreeing on the dense finite-packet subspace agree on the completion.

Consequently all 64 local `R x H` squares are instances of one theorem.

## Boundary

The result assumes the typed fiber multiplications used in the established inequality for `q_delta`. It proves continuity for the projective exponential coefficient completion. It does not prove continuity on an unrelated Hilbert completion, nor compatibility with nontransverse physical cuts; those belong to `R x V` and the common graph-domain gate.
