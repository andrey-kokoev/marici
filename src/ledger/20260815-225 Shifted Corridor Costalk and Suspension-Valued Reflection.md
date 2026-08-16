# Shifted Corridor Costalk and Suspension-Valued Reflection

## Record

Date: 2026-08-15

Status: proved in the explicitly enlarged finite dg target. The three
Tor-faithful pair realizations, normal differentials, endpoint rows, integral
matrix, and suspension-valued reflection are constructed. The suspension is
not yet realized as a geometric relative-dualizing line, and the enhanced
costalk is not part of literal entry143. No graph admission is claimed.

## Enhanced target

Let
\[
P(t)=t+2t^2+t^3
\]
be the Boolean normal packet on one literal corridor edge. Entry224 proves
that two unshifted copies \(P\oplus P\) cannot retain the two source Tor
grades under any fixed Gysin shift.

For every unoriented pair, adjoin instead
\[
E_{ij}^{\mathrm{sh}}=P\oplus P[1].
\]
Map the \(W_{ij}\) Tor-zero packet identically to \(P\), and map its Tor-one
packet identically to \(P[1]\). Their graded profiles agree:
\[
P(t)(1+t)=P(t)+tP(t).
\]
Rotation produces the other two pair enhancements.

The full realization has 24 source and 24 target generators. In the labelled
enhanced bases its matrix is the identity, hence rank 24 with 24 nonzero
Smith factors equal to one. No integer torsion or base inversion occurs.

## Normal and endpoint squares

For every pair, Tor grade, and \(H\subset S\), the normal differential is the
oriented two-label exterior differential. All 24 nonzero normal-removal
squares commute under the identity realization.

The empty and top masks supply 12 endpoint states across the three pairs and
two Tor grades. They are retained rather than collapsed.

## Suspension-valued reflection

Ordinary reflection exchanges the two corridor edges. Since their
cohomological placements differ by one, an unadorned exchange is not degree
zero. Introduce the inverse suspension line on the exchange:
\[
P\longleftrightarrow P[1],\qquad
\deg(\mathfrak s)=-\Delta\deg_{\mathrm{edge}}.
\]
The total reflection then has degree zero.

Reversal of the ordered two-label normal basis fixes the empty and singleton
states and multiplies the top exterior state by \(-1\). With these signs,
reflection commutes with every normal differential. Applying reflection
twice cancels the two edge shifts and suspension shifts and squares every
fibre sign, so \(r^2=1\) integrally.

This constructs the reflection-compatible dg enhancement; it does not derive
the suspension line from geometry.

## Remaining geometric gate

The next required object is an actual log/derived correspondence whose
relative dualizing complex restricts to the suspension line above. Its two
proper/extraordinary boundary maps must identify the ordinary and shifted
edge packets with the literal entry143 endpoint/corridor costalks and recover
the established odd endpoint counits.

Until that relative-dualizing realization exists, the enhanced target is a
finite dg model rather than the physical entry143 object. Consequently the
endpoint/\(Q\) mapping fiber, \(p_{\partial,Q}\), its Bockstein, and
\(D_8\)/Jordan coherence remain undefined.

## Executable evidence

Checker:
\`research/voevodsky/check_dp6_shifted_corridor_reflection.rs\`

SHA-256:
\`0a17c0505810a0f9f7c3b76b4b21a0b23e44f65db06ed528f6c90a98f130b70a\`

Fresh rustfmt, warnings-denied optimized compilation, runtime assertions, and
JSON output passed. Native PowerShell was used only because structured-command
MCP was not exposed in this session.

## Outcome contract

~~~json
{
  "claim": "The minimal Tor-faithful target enhancement consists of one ordinary and one shifted Boolean corridor packet P plus P[1] for each pair. It gives a saturated 24-state realization, and reflection becomes a degree-zero involution after tensoring its edge exchange with the inverse suspension line.",
  "status": "proved_scoped_shifted_corridor_dg_enhancement",
  "scope": "finite enhanced dg target; no geometric relative-dualizing realization or literal entry143 identification",
  "matrix": {
    "pairs": 3,
    "source_states": 24,
    "target_states": 24,
    "rank": 24,
    "all_nonzero_smith_factors": 1,
    "torsion": false
  },
  "checks": {
    "normal_chain_squares": 24,
    "endpoint_states": 12,
    "reflection_squares": 24,
    "reflection_total_degree": 0,
    "reflection_uses_suspension_line": true,
    "reflection_squared": 1,
    "base_inversions": false
  },
  "unconstructed": [
    "geometric relative-dualizing/Gysin realization of the suspension",
    "literal entry143 ordinary/shifted costalk comparison",
    "endpoint BC cells in the physical target",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_shifted_corridor_reflection.rs",
  "checker_sha256": "0a17c0505810a0f9f7c3b76b4b21a0b23e44f65db06ed528f6c90a98f130b70a"
}
~~~
