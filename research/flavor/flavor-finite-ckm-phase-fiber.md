# Finite CKM phase fiber (WP297)

## Lower-sector complement

Add $|V_{cb}|$ to WP296's six masses, complete first row, and signed $J$.
On the generic standard CKM domain, these data determine the three mixing
angles and $\sin\delta$. They do not determine the sign of $\cos\delta$.

## Exact hostile pair

The checker takes

\[
\sin\delta=\frac45,
\qquad
\cos\delta=\frac35
\]

and the companion with cosine $-3/5$. Both exact CKM matrices are unitary.
They have identical masses, first-row moduli, $|V_{cb}|$, and signed $J$.
Four interference-sensitive lower-sector moduli differ.

Thus the admitted readout has a generic twofold
$\delta\leftrightarrow\pi-\delta$ fiber. This is the exact finite-fiber
obstruction: finite fiber is not singleton fiber.

## Classification

The family is a near-faithful physical readout, neither a selector nor a
texture rigidifier. One independently calibrated cosine-sensitive CKM modulus
can separate this hostile pair. Such a measurement repairs readout
faithfulness; it still does not supply source dynamics selecting the measured
value.

Run `uv run --with sympy python
research/flavor/checkers/wp297_finite_ckm_phase_fiber.py` to regenerate the
exact twofold-fiber audit.
