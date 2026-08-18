---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Rank-Twenty-One Top Packet Passes the Mixed-Jet Flatness Test

## Typed second jet

Entry 585 exhibited a rank-two boundary extension of the proper top line.
Flatness cannot be tested by differentiating pointwise row-reduced
coefficients, because the reduction relations themselves vary with the
kinematics.

Instead, the checker now composes the parameter derivatives on unreduced
rational representatives.  For each generator it retains

\[
K_x,\quad K_y,\quad K_{xy}
\]

and the corresponding first and mixed derivatives of the three labelled
source denominators.  Reduction is applied only after forming

\[
[\nabla_x,\nabla_y].
\]

There is one essential depth correction.  A second parameter derivative of
a simple \(q_i^{-1}\) pole reaches \(q_i^{-3}\).  Thus the first-jet depth-two
presentation of Entries 583--585 is insufficient for curvature.  The mixed
test retains depth three on every \(q_i\) axis while leaving the measured
binary-pole space and its rank unchanged.

## Result

Over \(\mathbf F_{32003}\), with \(\gamma=5\), ambient degree nine, measured
numerator degree five, \(K\)-pole depth two, and \(q\)-pole depth three, all
twenty-one deterministic top generators satisfy

\[
\boxed{[\nabla_x,\nabla_y]=0.}
\]

The result holds at both generic points

\[
(x,y,z)=(2,3,4),\qquad(3,5,6).
\]

The exact census is

\[
21/21\text{ zero curvatures at each point}.
\]

The depth-two control is explicitly skipped as untyped rather than silently
truncating the second derivative.

## Meaning

The first flat two-direction physical packet has now been constructed at
finite generic kinematics:

\[
0\longrightarrow B_{20}
\longrightarrow H_{21}
\longrightarrow L_{\mathrm{top}}
\longrightarrow0,
\]

where the deletion boundary is connection-stable, the quotient is generated
by the literal \(\Omega_{111}\), and its two boundary extension components
are independent.  Flatness therefore does not split the extension; it makes
the nontrivial extension coherent.

This is the strongest realization so far of the shared-calculus principle:
the deletion carrier and its localization maps organize the filtration,
while the physical twisted-de-Rham coefficients supply the flat extension.
The source quartic is not needed as carrier support or diagonal transport.

What remains is geometric rather than linear-algebraic: compare this flat
packet with the relative integration-chain/Gysin local system and determine
which boundary subquotient carries the elliptic coefficient block.

## Evidence

- `research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs`;
- `research/benincasa/proper_top_mixed_jet_audit.json`;
- Entries 583--585.

## Outcome contract

~~~json
{
  "claim": "The two-direction connection on the rank-twenty-one top packet has nonzero mixed curvature once the moving presentation and required pole depth are retained.",
  "status": "falsified",
  "field_prime": 32003,
  "generic_points_tested": [[2, 3, 4], [3, 5, 6]],
  "generators_per_point": 21,
  "nonzero_curvatures": 0,
  "k_pole_depth": 2,
  "q_pole_depth": 3,
  "depth_two_second_jet_admissible": false,
  "next_experiment": "Construct the comparison from the flat deletion-filtered packet to the physical relative-chain and infinity-Gysin local systems."
}
~~~
