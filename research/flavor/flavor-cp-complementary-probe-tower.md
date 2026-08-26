# CP complementary-probe tower (WP330)

## Formal tower

WP328's calibrated branch log-odds is

\[
L=2\beta\epsilon c_0.
\]

Add two proposed common-history probes: an independent inverse-temperature
readout (T=\beta) and a CP-scale readout (S=c_0). The response Jacobian of
((L,T,S)) with respect to ((\beta,\epsilon,c_0)) has determinant

\[
-2\beta c_0.
\]

It is full rank on the positive domain and reconstructs

\[
\epsilon=\frac{L}{2TS}.
\]

## Minimality

Log-odds alone has rank one. Adding either the thermometer or the CP-scale
probe raises the rank to two but leaves a one-dimensional kernel. Both are
necessary for full identification of this three-parameter source packet.

## Typing gate

This is a formal faithfulness theorem, not yet an executable experiment. The
thermometer and CP-scale readout must be derived and calibrated on the same
freeze-out support, time, and normalization as the domain counts. Combining a
valid thermal model with a separately calibrated low-energy CP magnitude does
not define the missing common-frame constructor.

The tower identifies source parameters if physically realized. It does not
select their values and therefore supplies no new numerical flavor prediction.

Run `uv run --with sympy python
research/flavor/checkers/wp330_cp_complementary_probe_tower.py` to regenerate
the exact rank audit.
