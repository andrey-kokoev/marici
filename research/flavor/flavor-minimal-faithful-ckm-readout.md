# Compact faithful CKM readout (WP298)

## Reconstruction domain

Work on the standard CKM chart with ordered nondegenerate masses, all three
mixing angles in the open first quadrant, and nonzero Jarlskog normalization.
Admit the six masses and

\[
|V_{us}|^2,\quad |V_{ub}|^2,\quad |V_{cb}|^2,\quad |V_{cd}|^2,\quad J.
\]

The first three moduli reconstruct $s_{13},s_{12},s_{23}$ in the declared
quadrant. Signed $J$ reconstructs $\sin\delta$. The interference term in
$|V_{cd}|^2$ reconstructs $\cos\delta$. Standard CKM formulas then recover
all nine moduli and signed $J$, hence `physical16`.

## Exact closure of the hostile fiber

The checker applies the inverse formulas to both WP297 packets. Every one of
the nine reconstructed squared moduli and signed $J$ agrees exactly with its
source packet. The added readout separates the hostile pair: its two values
are $|V_{cd}|^2=285184/714025$ and $|V_{cd}|^2=172864/714025$.

The faithfulness claim is restricted to the stated standard chart. Degenerate
masses, vanishing angles, and zero Jarlskog normalization require separate
charts and cannot inherit this inverse formula.

## Classification

This is a compact faithful physical readout and separator, neither a selector
nor a texture rigidifier. It reconstructs the point presented by nature; it
does not supply a source operation selecting that point. Instrument admission
still requires calibrated decay channels and their common-fit correlations.

Run `uv run --with sympy python
research/flavor/checkers/wp298_minimal_faithful_ckm_readout.py` to regenerate
the exact reconstruction audit.
