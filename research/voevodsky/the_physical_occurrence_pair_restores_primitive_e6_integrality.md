# The physical occurrence pair restores primitive e6 integrality

The local source-normalized class satisfies

\[
\rho_{e_6}=\frac14\eta,
\]

where \(\eta\) is the primitive integral Betti covector. Thus a single displayed de Rham \(e_6\) coefficient carries index four.

The physical \(q_{\mathcal G_{12}}\) residue contains two labelled lower-denominator occurrences,

\[
(12|23)+(12|31).
\]

In the six-occurrence basis this is

\[
p_{12}=(1,1,0,0,0,0).
\]

The source-derived sheet-difference map contributes a factor \(-2\) to each occurrence:

\[
p_{12}\longmapsto(-2,-2,0,0,0,0).
\]

Occurrence forgetting then adds the two entries belonging to the same marked Cut:

\[
(-2,-2,0,0,0,0)
\longmapsto(-4,0,0).
\]

Since

\[
\eta_j=4g_j=4\rho_{e_6,j},
\]

the primitive Betti output is

\[
(-1,0,0).
\]

Therefore the complete sourced physical Cut pair supplies one primitive \(e_6\) unit. The tail in \((e_7,e_8,e_9)\) vanishes, giving zero \(v_{\rm alg}\) coordinate. Modulo two the physical readout is

\[
\boxed{(1,0)}.
\]

This resolves the apparent conflict with the C2 rejection. A single de Rham coordinate has index four; the physical observable contains the canonical factor four as

\[
2\ \text{(sheet difference)}
\times
2\ \text{(lower occurrences per Cut)}.
\]

The original C1 statement identifying the physical current with the four-mark global Cech checkerboard remains rejected. Its correct replacement is now confirmed:

> The sourced single-Cut occurrence pair maps with multiplicity one to the primitive \(e_6\) Betti generator.

Certificate:

- `research/voevodsky/checkers/replay_C1_in_integral_e6_basis.py`;
- `research/voevodsky/results/C1_integral_e6_replay.json`.
