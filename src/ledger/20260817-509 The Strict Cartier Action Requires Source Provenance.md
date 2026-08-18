# Entry 509 — The Strict Cartier Action Requires Source Provenance

Entries 506--508 construct and strictify the corrected operation

\[
M_{a^2}^{\mathrm{corr}}=(a^2,H_{a^2}).
\]

In particular, Entry 508's source action contains the principal component
\(-h(f)\).  The existing finite-cutoff program of Entry 504 cannot yet compute its
induced action.  That program stores only vectors spanning
\(\operatorname{im}d\); it discards the sector, monomial, and \(p/q\) source
labels.  But the correction is defined on those labelled generators:

\[
H(p_f)=0,
\qquad
H(q_f)=\left({a^2m\over2},0,uam\right),
\qquad
m=fL_1^{e_a}L_2^{e_b}.
\]

This loss is substantive.  At (u=0), compare the target matrix (d_D)
with the graph matrix ((d_D,H_D)).  For every tested stable cutoff,

\[
\boxed{\operatorname{rank}(d_D,H_D)>\operatorname{rank}(d_D).}
\]

Thus (H_D) contains source information not recoverable from the span of
target exact columns.  A corrected action cannot be inferred by postprocessing
Entry 504's cokernel matrix.

## Consequence

The next computation must retain the labelled free source module, the exact
differential, and the three gradient rows simultaneously.  Only that chain
complex admits the graph map ((a^2,H_{a^2})) and hence an induced homology
map.  This is a coefficient-complex refinement, not new carrier geometry.

The result neither proves nor disproves Entry 503's reduced-incidence
hypothesis.  It prevents a falsely typed numerical verdict from the old rank
census.

## Next gate

Construct the labelled finite mapping cone with source basis
\((e_a,e_b,f,p/q,a^i b^j)\), append the gradient/Kodaira--Spencer rows, and
compute the corrected (a^2)-map on its stable plus (u)-homology.

The rank-separation audit is
`research/voevodsky/check_soft_axis_a2_homotopy_provenance.py`.
