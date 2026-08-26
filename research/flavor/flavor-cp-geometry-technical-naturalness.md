# CP-geometry technical naturalness (WP354)

## Symmetry-protected transport

Let the CP-odd geometry coordinate obey multiplicative transport

\[
\frac{dt}{d\ell}=a t.
\]

The exact solution is

\[
t(\ell)=t_0e^{a\ell}.
\]

CP symmetry makes (t=0) an exact fixed locus. A small nonzero seed remains
multiplicatively small over a bounded transport interval, and its sign is
preserved for real (a,\ell).

## Authority audit

The logarithmic response to the boundary seed is

\[
\frac{\partial\log|t(\ell)|}{\partial\log|t_0|}=1.
\]

Thus technical naturalness protects smallness but does not select its magnitude.
The anomalous dimension and scale interval also remain transport inputs. RG
flow is an equivariant carrier of the seed, not a numerical source selector.

This distinction matters for WP353: a value near (10^{-4}) can be stable
without being predicted.

## Successor gate

A progressive model must derive a nonzero boundary seed or threshold kick
independently of flavor readout, freeze its scheme and scales, and test the
transported (J) without retuning. An exactly CP-symmetric source instead
predicts (t=0), already incompatible with nonzero fitted CP violation.

Run `uv run --with sympy python
research/flavor/checkers/wp354_cp_geometry_technical_naturalness.py` to
regenerate the exact transport audit.
