# Joint-tail selector bound (WP291)

## Marginals do not determine global failure

Take three local selector margins. Two exact joint packets can give every
margin the same law from WP289—mean 2, variance 1, and local failure probability
$1/12$—while coupling the failures differently.

In the aligned packet, all three margins fail together, so the global failure
probability is $1/12$. In the disjoint packet, exactly one margin fails in
each of three distinct atoms, so global failure is $1/4$. The latter exactly
saturates the union bound

\[
P(\exists i:m_i\leq0)\leq\sum_iP(m_i\leq0).
\]

All marginal moment and tail probes place these packets in the same contextual
class. A coincidence-sensitive joint probe separates them.

## One-percent gate

Without dependence information, a three-vertex global failure target of one
percent requires each local Cantelli bound to be at most $1/300$. Therefore

\[
\frac{\mu_i}{\sigma_i}\geq\sqrt{299}
\]

at every vertex. This is sufficient and worst-case sharp under unrestricted
dependence; it is not necessary for a particular source-correlated packet.

## Classification

Marginal calibration authorizes only the union-bound global certificate. A
sharper selector requires a source-derived joint law and a physical instrument
for cross-domain coincidence in a common timing and detector frame. Formal
covariance or assumed independence is not that instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp291_joint_tail_selector_bound.py` to regenerate the
exact joint-packet audit.
