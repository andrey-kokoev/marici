# Six-domain parity obstruction (WP342)

## Exact hostile law

Compare six iid fair binary domains with the uniform law on the 32 odd-parity
words. The parity law is five-wise independent: for every subset of size
(j<6), both laws have coincidence moment

\[
2^{-j}.
\]

Consequently every labelled coincidence probe through order five gives the
same result on both laws. At sixth order,

\[
u_6^{\mathrm{iid}}=\frac1{64},
\qquad
u_6^{\mathrm{parity}}=0.
\]

## Consequence

No tower truncated below order six can certify independence on the unrestricted
six-bit law family. This is stronger than WP341's three-bit example and shows
that arbitrarily high lower-order agreement need not imply the missing top
interaction is absent.

The result does not say sixth order is always necessary. WP340 remains correct
on a source family independently restricted to iid laws. It says that the
restriction cannot be inferred from any order-five coincidence record.

## Instrument tradeoff

One must either execute calibrated sixth-order labelled coincidences, accepting
the (gamma^{-6}) conditioning cost from WP339, or supply a source theorem that
excludes global parity constraints before truncating the probe tower.

Run `uv run --with sympy python
research/flavor/checkers/wp342_six_domain_parity_obstruction.py` to regenerate
the exact obstruction.
