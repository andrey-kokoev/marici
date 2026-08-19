# 998 — The Normal Gysin Shift Does Not Supply the Missing Edge Support Map

## Question

Entry 997 proposed comparing the rank-one recombination modification with Entry 979's exceptional chamber-edge complex after a normal Gysin shift.  Audit whether that shift alone types the comparison.

## The two objects

For either signed recombination character, Entry 997 gives a rank-one elementary-modification costalk

\[
E_{\chi,s,t}
=
\frac{K_\chi}{\delta U+st\,\delta V}
\]

supported on a codimension-two intersection of labelled source walls.  A normal Gysin shift changes its cohomological degree by one.

Entry 979 instead gives the twisted chamber cochain

\[
\delta_{\rm KN}\lambda
\in
C^1_{\rm chamber}(\mathcal K_{\rm KN}),
\]

whose six components are supported on the six oriented codimension-one chamber edges and whose transported two-cell boundary vanishes.

## Support and variance audit

After the normal Gysin shift, both objects have cohomological degree one.  Their support and variance remain different:

\[
\begin{array}{c|c|c}
&\text{support}&\text{variance}\\
\hline
E_{\chi,s,t}[1]
&\text{codimension-two signed wall intersection}
&\text{normal costalk}\\
\delta_{\rm KN}\lambda
&\text{codimension-one oriented chamber edge}
&\text{edge cochain}.
\end{array}
\]

The frozen packets provide no labelled Cousin boundary, restriction, or chain/cochain pairing

\[
\partial_{Z\to e}:
i_Z^!\mathcal E[1]
\longrightarrow
\bigoplus_{e\supset Z}i_e^!\mathcal K_{\rm KN}
\]

from a signed wall intersection \(Z\) to its incident chamber edges.  A degree shift does not construct this support-changing morphism.

## Result

\[
\boxed{
\text{the normal Gysin shift aligns degree, but the comparison with Entry 979 remains untyped.}
}
\]

Therefore rank-one status, cyclic holonomy, reflection character, and cohomological degree cannot identify the two lines.  Entry 997's descent theorem is unchanged; only its proposed comparison frontier is narrowed.

No new carrier cell is indicated.  The existing codimension-two wall intersections and codimension-one chamber edges are sufficient as supports.  What is absent is the source-derived support morphism and its orientation/unit packet.

## Next finite test

For each labelled signed wall intersection, derive from the source regularized intersection calculus the two incidence maps to its oriented incident chamber edges.  Verify their residue orientations and rational units, assemble the Cousin differential, and only then test whether the image equals Entry 979's edge class.  If no such source map exists, retain the modification and edge cochain as separate terms of a total complex.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_normal_gysin_edge_support_gate.rs`
- `research/benincasa/string-six-point-normal-gysin-edge-support-gate.json`

The checker verifies the two frozen objects, their degree data, their distinct supports and variances, and the absence of a support-changing map from the audited packets.

Epistemic graph event: `ev-000000000616-bfd6a30c-67a0-40bf-b919-8ad4a356954a`.
