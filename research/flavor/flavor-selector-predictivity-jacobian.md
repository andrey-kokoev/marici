# Selector predictivity Jacobian (WP305)

## Local ambiguity criterion

Let a candidate source family have admitted parameters $\theta$ after genuine
source redundancies are quotiented, and let its selected flavor image be
$x_*(\theta)$. The local response

\[
J_{\mathrm{src}}=\frac{\partial x_*}{\partial\theta}
\]

measures how many source-modulus directions change the alleged prediction. A
parameter-independent point prediction requires rank zero on the admitted
source family.

This condition is necessary, not sufficient. Rank zero does not establish
global uniqueness, coefficient provenance, descent, executable dynamics, or a
physical instrument.

## Exact rank ladder

The checker unifies the preceding route:

- WP301's two free linear sources give physical response rank two.
- WP302's swap symmetry reduces the physical response rank to one.
- WP303's projective quotient removes the amplitude response and gives rank
  zero for the ratio.
- Lifting the ray with a free physical radius restores rank one.
- WP304's transmutation scale has nonzero response to its boundary coupling,
  again giving rank one.

Thus symmetry and quotienting can remove genuine redundancy, but neither can
erase a modulus that changes a physical mass or invariant magnitude.

## Progressive gate

A viable source constructor must enumerate its moduli before flavor fitting,
quotient only declared source equivalences, and compute the complete
source-to-`physical16` response rank. Every surviving responsive direction
needs an independently derived selector operation. Uncertainty can only weaken
a near-zero singular value claim, so robust rank must be assessed in the
calibrated source frame.

Run `uv run --with sympy python
research/flavor/checkers/wp305_selector_predictivity_jacobian.py` to regenerate
the exact rank audit.
