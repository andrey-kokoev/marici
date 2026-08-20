# Entry 1224 — The Five-Site Physical Sheet Is Equivariant but Does Not Descend

## Question

Entry 1223 established strict deck descent of the intrinsic rank-32 Kummer connection. It is tempting to demand the same invariant descent from the physical Bunch–Davies cycle. That demand is too strong.

On a real chamber where all five physical roots are positive, let

\[
\Gamma_+
\]

denote the locally selected positive-sheet lift of the source integration cycle. The deck group is

\[
G=(\mathbb Z_2)^5.
\]

## Exact orbit statement

Every nontrivial deck element changes at least one root sign. Therefore

\[
\operatorname{Stab}_G(\Gamma_+)=1,
\]

and

\[
\boxed{
\{g\Gamma_+:g\in G\}
\text{ has 32 elements and spans }\mathbb Q[G].
}
\]

The physical $u_1,u_2,u_3$ coordinates and the current orientation are fixed by deck transport. Thus the 32 continuations form a coherent regular permutation local system.

At a branch stratum indexed by $B\subseteq\{1,\ldots,5\}$, where $F_i=0$ for $i\in B$, sheets differing only by signs in $B$ have the same restriction. The number of restricted sheet classes is

\[
2^{5-|B|}.
\]

The checker verifies this for all 32 branch subsets, with 1,024 group-action and 7,776 restriction identities.

## Trace versus physical evaluation

The orbit trace

\[
\operatorname{Tr}(\Gamma_+)
=
\sum_{g\in G}g\Gamma_+
\]

is deck-invariant. The source-selected physical chain $\Gamma_+$ is not.

Hence

\[
\boxed{
\text{the physical cycle is equivariant but does not descend to one invariant base cycle.}
}
\]

The physical readout is evaluation on a locally selected chamber vector, not projection to deck invariants. Replacing it by the trace would change the observable.

## Classification

\[
\boxed{
\text{sector-specific Betti local system and chamber readout}
\quad|\quad
\text{existing Kummer cover}
\quad|\quad
\text{no new carrier datum}.
}
\]

This is not a failure of H2. It identifies the precise layer at which cosmology retains physical sheet information after carrier and connection descent.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_physical_sheet_orbit.rs`
- `research/benincasa/results/five-site-physical-sheet-orbit.json`

## Next falsifier

Construct the pairing between the rank-32 Kummer coefficient system and the regular Betti orbit. Test whether its deck covariance makes the scalar chamber evaluation independent of continuation once the source endpoint and (i\epsilon) data are transported together. A failure there would be physical monodromy or regulator dependence, not a carrier-incidence defect.
