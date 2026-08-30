# Joint block and comparison faults form an anchored graph code

Owner: `marici.Kitaev`

## Bounded question

Given trusted anchors, can one Bell-comparison record distinguish faults on
logical blocks from faults in the comparison measurements themselves?

## Joint fault map

Fix one trusted anchor in each connected component and let \(\delta_A\) be
the comparison coboundary restricted to unanchored block labels. For one Pauli
coordinate, the observed record is

\[
y=\delta_A e+f,
\]

where \(e\) is the block-fault pattern and \(f\) is the edge-measurement-fault
pattern.

The joint map is

\[
M=[\,\delta_A\ I\,].
\]

Although \(\delta_A\) is injective, \(M\) is never injective when an
unanchored vertex exists. Its kernel is

\[
\ker M=\{(e,\delta_Ae):e\in C^0(G,A;\mathbf F_2)\}.
\]

Thus a block-fault pattern and its induced edge boundary can be exchanged
without changing the record. An anchor removes common mode but does not by
itself distinguish data faults from measurement faults.

## Ambiguity distance

The binary code of invisible joint differences has minimum distance

\[
d_{\mathrm{mix}}(G,A)
=
\min_{\varnothing\ne S\subseteq V_G\setminus A}
\bigl(|S|+|\partial S|\bigr).
\]

For logical Pauli coefficient space \(\mathbf F_2^{2k}\), independent
coordinate copies have the same minimum distance. Joint faults of total weight
at most \(t\) are uniquely correctable exactly under the standard sufficient
bound

\[
2t<d_{\mathrm{mix}}.
\]

Beyond the unique-radius regime, choosing between block and measurement
attributions requires a cost model, likelihood, temporal history, or other
decoder data.

## Graph witnesses

An anchored tree always has an unanchored leaf. Choosing that leaf gives

\[
d_{\mathrm{mix}}=2.
\]

One block fault at the leaf and one fault on its incident comparison edge have
the same syndrome. A tree therefore cannot correct one arbitrary joint fault.

An anchored simple cycle has

\[
d_{\mathrm{mix}}=3.
\]

It corrects one arbitrary joint fault. The extra cycle edge is precisely the
redundancy that separates a single vertex fault from a single edge fault.

For the complete graph \(K_n\) with one anchor,

\[
d_{\mathrm{mix}}=n.
\]

Dense comparison raises the joint-fault distance, although it does not alter
the absolute-anchor requirement.

## Weighted decoding

If block and comparison faults have unequal costs, the relevant decoder
minimizes

\[
\alpha|e|+\beta|f|
\]

subject to \(\delta_Ae+f=y\). The graph supplies the constraint, not
\(\alpha,\beta\). Equal syndrome therefore still does not select a preferred
physical recovery instrument.

## Mixed-boundary typing

Every handle, loop, and relative-arc Pauli coordinate carries a copy of this
anchored graph code. Geometry determines which parity coupling realizes each
coordinate. The quantum coefficient and apparatus lenses determine whether a
vertex or edge fault occurred and what recovery is physically legal.

## Falsifiers

- a nonzero unanchored vertex module with injective \([\delta_A\ I]\);
- kernel not equal to the graph of \(\delta_A\);
- anchored-tree distance above two;
- anchored-cycle distance different from three;
- complete-graph distance different from \(n\);
- unique correction claimed when \(2t\ge d_{\mathrm{mix}}\);
- a preferred attribution inferred without a cost or noise model.

## Disposition

Joint block and comparison faults are an ordinary binary graph code whose
distance is anchored vertex-plus-cut expansion. Cycles buy fault distance;
anchors buy absolute orientation. Decoder preference remains external to the
syndrome complex.

## Claim strength

Exact finite joint-fault code theorem.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_bell_reference_joint_fault_distance.py`.
The result is written to
`research/kitaev/results/bell-reference-joint-fault-distance.json`.

