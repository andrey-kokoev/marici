# Entry 1222 — Deck Transport Commutes with the Five-Site Marked Čech Differential

## Question left by Entry 1221

Entry 1221 established a strict deck cocycle on the 32 chamber presentations of the physical five-edge Kummer cover. That did not yet show that deck transport respects the marked-intersection differential.

Freeze the 180 source OFPT terms. Each term has ten ordered denominator sections: the six common sections

\[
(G,g_1,g_2,g_3,g_4,g_5)
\]

followed by its four source-derived term sections. The source order fixes every residue and simplicial orientation.

## Hard-to-vary claim

For chamber $g\in(\mathbb Z_2)^5$, form the complete labelled Čech cube of each ten-section term. The generator $T_i$ changes the sheet $y_i\mapsto-y_i$ and sends chamber $g$ to $g\oplus e_i$, but retains the ordered section labels and every subset indexing a Čech cell.

For an ordered subset $S$ the differential is

\[
d_{\rm Cech}[S]
=
\sum_{r=1}^{|S|}(-1)^{r-1}[S\setminus S_r].
\]

Because $T_i$ neither permutes the labels nor changes their positions,

\[
\boxed{
T_i d_{\rm Cech}=d_{\rm Cech}T_i
}
\]

term by term and chamber by chamber. The corresponding logarithmic forms obey the same statement by pullback of the labelled equations.

## Exhaustive finite test

The Rust checker enumerates every subset in every ten-section cube for all 180 terms and 32 chambers. It verifies:

\[
147{,}456{,}000
\]

deck-transported boundary terms, and independently verifies

\[
2{,}073{,}600
\]

opposite-sign deletion pairs giving $d_{\rm Cech}^2=0$. All 180 terms have ten distinct labels. Every check passes.

Thus

\[
\boxed{
\bigoplus_{g\in(\mathbb Z_2)^5}M_g^\bullet
\text{ is a strict deck-equivariant marked Čech complex.}
}
\]

There is no projective chain cocycle and no new carrier datum at this grade.

## Scope

This establishes equivariance of the source-labelled marked-intersection differential and its logarithmic pullback. It does not derive the five-site Gauss–Manin connection, compute relative de Rham cohomology, or prove Bunch–Davies cycle descent.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_deck_cech_chain_map.rs`
- `research/benincasa/results/five-site-deck-cech-chain-map.json`

## Next falsifier

Derive a source-normalized parameter connection on the induced chamber-relative complex and test

\[
\nabla T_i=T_i\nabla
\]

before taking invariants. A nonzero defect would be coefficient descent data. The present result forbids repairing such a defect by changing the already fixed Čech incidence signs.
