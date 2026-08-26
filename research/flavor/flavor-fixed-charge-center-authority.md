# Fixed-charge center authority (WP319)

## Candidate repair

A natural attempt to repair WP318 is to replace the quadratic energy by

\[
E_N(m)=(m-N)^2,
\qquad m\in\mathbb Z_{>0}.
\]

For every admitted integer (N), this energy uniquely selects (m=N). In
particular, (N=64) reproduces the lattice value close to the fitted hierarchy.

## Authority audit

The construction selects sharply but does not explain its center. The same
grammar permits every positive integer center, and changing (N) changes the
selected hierarchy ratio. In the continuous extension its response is

\[
\frac{d}{dN}\left(\sqrt{N^2+1}+N\right)
=1+\frac{N}{\sqrt{N^2+1}}>0.
\]

Thus the source response is nonzero: numerical authority has moved from a soft
coefficient into a discrete boundary label. Calling that label topological
does not determine its value.

## Disposition

The centered energy is a conditional selector and not a presentation
rigidifier. It becomes predictive only if an independently admitted topology,
conservation law, or preparation theorem forces (N=64) before flavor data are
read. Preparing a charge-64 sector is a new source operation, not an instrument
that discovers why the original source chose 64.

Run `uv run --with sympy python
research/flavor/checkers/wp319_fixed_charge_center_authority.py` to regenerate
the exact audit.
