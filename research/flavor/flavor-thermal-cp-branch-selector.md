# Thermal CP-branch selector (WP282)

## Finite thermal history

Add the WP281 CP-odd bias \(-ha\) on one thermal correlation volume
\(V_{\mathrm{corr}}\). The two vacuum energies differ by
\(2hvV_{\mathrm{corr}}\). At temperature \(T\), the branch odds are

\[
\frac{p_+}{p_-}
=\exp\left(\frac{2hvV_{\mathrm{corr}}}{T}\right),
\]

and the favored probability is

\[
p_+=\frac{exp(2hvV_{\mathrm{corr}}/T)}
{1+\exp(2hvV_{\mathrm{corr}}/T)}.
\]

With zero bias the action prepares the symmetric half–half distribution. Any
finite bias favors a sign but leaves nonzero probability for the other branch.

## Exact error contract

To bound the wrong-branch probability by \(1/100\), the required condition is

\[
\frac{2hvV_{\mathrm{corr}}}{T}\geq\log99.
\]

At equality, the favored probability is exactly \(99/100\). By contrast,
finite odds three give favored probability \(3/4\) and exact error \(1/4\).

## Classification

A biased thermal history is a conditional probabilistic branch selector, not a
deterministic signed selector or texture rigidifier. Its prediction depends on
the source-derived bias, vacuum magnitude, correlation volume, and temperature
history. A readout of the realized sign does not derive those fields.

The physical instrument gate includes the quench rate, domain-wall evolution,
stabilization, and declared acceptable error. Infinite volume, multiple
domains, tunneling, and nonequilibrium histories define different experiments.

Run `uv run --with sympy python
research/flavor/checkers/wp282_thermal_cp_branch_selector.py` for exact odds,
normalization, error threshold, and hostile finite-bias checks.
