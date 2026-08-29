# The first Adams composition slot has an eleven-witness first-failure chain

## Reason for refinement

The interaction-net contract currently contains one coarse open constructor named type_fiber_adams_composition. That slot hides independent gates, and later scalar projections can conceal earlier failures.

## Witness 1: coefficient wall split

Question: Is the constant–delta wall retained before multiplication representation?

Current state: carrier constructed; residue theorem conditional.

Evidence:

- research/nima/the-multiplication-history-gram-residue-is-the-identity-not-a-rank-one-wall-projector.md
- research/nima/gram-residue-uses-the-quadratic-representation-and-wall-removal-does-not-make-multiplication-compact.md

Failure: the analytic identity is subtracted without proving it is the quadratic image of the coefficient wall projector.

## Witness 2: adjacent scale path

Question: Is there a source-derived continuation from \(\log p\) to \(2\log p\)?

Current state: constructed locally.

\[
W_{2L}-W_L=\int_L^{2L}\partial_tW_t\,dt.
\]

Evidence: research/nima/the-adjacent-window-cell-is-an-exact-scale-path-propagator-before-green-completion.md

Failure: a fitted translation kernel replaces the source scale path.

## Witness 3: local closed history and endpoint traces

Question: Does the window path define a closed history graph with continuous endpoint traces?

Current state: constructed on local \(L^2_q\).

\[
\|W_t\|\le1,\qquad\|\partial_tW_t\|\le2.
\]

Evidence: research/nima/local-window-histories-are-bounded-but-primitive-global-hilbert-summation-diverges.md

Failure: pointwise Stokes holds but the history graph is nonclosable.

## Witness 4: global Laplace-rigged history

Question: Do prime-labelled histories assemble in the correct primitive and square topologies?

Current state: open.

\[
\sum_p\frac{\log p}{p^{1+2\sigma}}\sim\frac1{2\sigma}.
\]

The primitive history is Hilbert only for \(\sigma>0\); the square history reaches the seam in its Hilbert grade.

Evidence: research/nima/the-primitive-history-has-an-exact-square-root-seam-blowup.md

Failure: a common Hilbert space silently inserts an unauthorized primitive weight.

## Witness 5: independently typed endpoint incidence

Question: Are the primitive and square factors constructed before the mixed block?

Current state: constructed as source incidences; their Green coupling remains open.

\[
I_1(p,1)=p^{-1/2}\delta_{\log p},
\qquad
I_2(p,2)=\frac12p^{-1}\delta_{2\log p}.
\]

Evidence: research/nima/the-independent-boundary-factors-are-incidence-lifts-not-rank-one-decompositions.md

Failure: rank-one factors are fitted after \(B\) is known or rescaled against each other.

## Witness 6: relative Green/Stokes pairing

Question: Does the source history produce the mixed form from the frozen endpoint factors?

Current state: first live formula; undefined.

\[
b_{\alpha,p}(x,y)
=
\left\langle
L_{Q,p}^*y,
\partial\mathscr C_pL_{P,p}^*x
\right\rangle_{\mathrm{rel}}.
\]

Evidence:

- research/nima/the-first-adams-type-edge-reduces-to-a-bulk-cell-form-factorization.md
- research/nima/oriented-boundary-factorization-is-the-source-route-to-rank-one-odd-support.md

Failure: correct endpoint scalars but no source pairing across disjoint Mellin locations.

## Witness 7: radical descent and bounded defect factor

Question: Does the mixed form annihilate both Green radicals and satisfy energy domination?

Current state: open.

\[
\ker C_1\subseteq\ker K^*,
\qquad
\ker C_2\subseteq\ker K,
\]

and

\[
\left\|C_1^{\dagger/2}KC_2^{\dagger/2}\right\|\le1.
\]

Evidence: research/nima/two-finite-hostiles-separate-scalar-agreement-from-typed-adams-sewing.md

Failure: scalar agreement coexists with action on a zero-energy direction.

## Witness 8: wall character and odd-port faithfulness

Question: Does the mixed block have rank-one antisymmetric support, or is the conservative rank-two odd observer faithful?

Current state: conditional.

Selection route:

\[
W_QBW_P^*=-B.
\]

Fallback route: constant-wall amplitude plus polarized Wronskian orientation must form a rank-two face observer.

Evidence:

- research/nima/the-complete-local-odd-sector-has-two-face-types-before-mixed-incidence-restriction.md
- research/nima/the-conservative-rank-two-odd-sector-has-a-source-derived-two-port-fallback.md

Failure: every tested odd current sees the Gaussian direction while the odd wall direction remains dark.

## Witness 9: intact typed block pushforward

Question: Does prime pushforward preserve the complete block and orientation?

Current state: open.

\[
\begin{pmatrix}
G_P&B^*\\
B&G_Q
\end{pmatrix}.
\]

Evidence:

- research/nima/chart-covariance-must-precede-typed-prime-pushforward.md
- research/nima/the-source-already-contains-the-minimal-odd-port-for-mixed-pushforward-faithfulness.md

Failure: \(B\) and \(B^*\) push forward to the same scalar packet.

## Witness 10: closable oriented graph relation

Question: Does the quotient defect operator pull back to a closable primitive-to-square relation with the correct seam character?

Current state: open.

\[
\Gamma_{2;p,1}
=
\{(x,y):q_1x=C_{2;p,1}q_2y\}.
\]

Failure: the quotient contraction exists but the unreduced relation has nondense adjoint domain.

## Witness 11: typed grade-six filler

Question: Do the four typed Adams edge maps fill the geometric grade-six diamond?

Current state: geometric cell contractible; typed filler undefined.

\[
T_3^{(2\to6)}T_2^{(1\to2)}
\quad\text{versus}\quad
T_2^{(3\to6)}T_3^{(1\to3)}.
\]

Failure: the geometric square closes while typed composites disagree or are ill-typed.

## Determinant side branch

The adelic vacuum gives a canonical trace-class sandwich only after the endpoint block exists and preserves the integral sector.

Evidence:

- research/nima/the-adelic-vacuum-supplies-a-canonical-trace-class-sandwich-after-wall-removal.md
- research/nima/integral-endpoints-do-not-imply-that-the-continuous-scale-history-survives-the-adelic-projector.md

The continuous path cannot be assumed to survive the adelic projector merely because its endpoints are \(p\) and \(p^2\).

## Recommended chain

1. adams_wall_split
2. adams_scale_path
3. adams_local_history_trace
4. adams_global_laplace_history
5. adams_typed_endpoint_incidence
6. adams_relative_green_stokes_pairing
7. adams_radical_descent_and_contraction
8. adams_wall_character_or_odd_frame
9. adams_intact_block_pushforward
10. adams_closable_graph_relation
11. adams_grade_six_typed_filler

At most the first three local witnesses are currently constructed. Endpoint incidence is independently constructed but does not compose with them until the Green/Stokes formula exists.

## First live failure boundary

The earliest unresolved compositional arrow is

\[
\text{global Laplace-rigged history}
\longrightarrow
\text{relative Green/Stokes mixed form}.
\]

This is the correct first-failure location for the current RH interaction net.
