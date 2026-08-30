# Graph-domain coarsening threshold (WP285)

## Topology-dependent theorem

Let a finite undirected graph carry spins (s_i\in\{-1,+1\}) and energy

\[
E=-J\sum_{(i,j)\in E(G)}s_i s_j-h\sum_i s_i,
\qquad J,h>0.
\]

For a minus spin at a vertex of degree (d_i), the largest possible energy
cost of flipping it occurs when all its neighbors are minus:

\[
\Delta E_{-\to+}=2(Jd_i-h).
\]

Consequently, if (\Delta) is the maximum graph degree, (h>J\Delta)
makes every minus-to-plus flip strictly energy lowering in every configuration.
The reverse flip is then strictly energy raising. Repeatedly flipping any
remaining minus spin reaches the favored uniform vacuum in exactly as many
moves as there were initial minus spins.

## Sharp obstruction

The threshold depends on topology. On a regular graph of degree (\Delta),
the wrong uniform vacuum is a strict local minimum when (h<J\Delta) and has
a neutral first move at equality. Thus WP284's (h>2J) is the degree-two ring
case, not a topology-independent flavor law.

The checker exhaustively audits the triangle, five-cycle, and complete
four-vertex graph. Their respective thresholds are $h>2J$, $h>2J$, and
$h>3J$. In every case, the wrong uniform vacuum survives below threshold and
every enumerated state has a strict path to all-plus above threshold.

## Classification and gate

This is a conditional branch selector in a declared finite graph dynamics. It
does not yet select a point of `physical16`: the domain graph or continuum
geometry, (J), (h), update law, temperature, tunneling, expansion, defects,
runtime, and branch-to-flavor map lack source and instrument authority.

Run `uv run --with sympy python
research/flavor/checkers/wp285_graph_domain_coarsening_threshold.py` to
regenerate the exact audit.
