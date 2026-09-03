# Probe-configuration Segal defects as Interaction Net semantics

## Question

Can instrument placements on a finite coherence diagram be assigned categorical constraint objects so that Interaction Net cells represent the failure of jointly probed constraints to factor into their separately probed marginals?

## Claim boundary

This packet constructs a finite-set prototype. It does not prove that an existing SCC net has this semantics, that every proof admits an Interaction Net presentation, or that the construction has physical meaning. Configuration order below is placement and composition order, not physical time.

## Construction

Let \(N\) be a typed set of locations and \(\mathsf{Instr}\) a typed set of instruments. A placement configuration is a finite partial assignment of instruments to locations. Assign each configuration \(c\) a constraint object

\[
\mathcal K(c)\in\mathsf{FinSet}.
\]

For two placements \(P@a\) and \(Q@b\), restriction supplies a comparison

\[
\chi_{P,Q}^{a,b}:\mathcal K(P@a,Q@b)
\longrightarrow
\mathcal K(P@a)\times_{\mathcal K(\varnothing)}\mathcal K(Q@b).
\]

The map compares constraints calculated with both instruments present against constraints assembled from the two one-instrument views. Its failure to be an isomorphism is the two-probe Segal defect. The defect is undefined, rather than zero, if either placement or restriction map is untyped.

### Minimal two-probe witness

Take \(\mathcal K(\varnothing)=\{*\}\) and

\[
\mathcal K(P@a)=\mathcal K(Q@b)=\{0,1\}.
\]

The pullback of the unary views is the four-element product. Define the actual joint constraint object by

\[
\mathcal K(P@a,Q@b)=\{(0,0),(1,1)\}.
\]

Then \(\chi\) is injective but not surjective. Each marginal remains the full set \(\{0,1\}\), so neither unary probe detects the equality constraint. Joint placement excludes \((0,1)\) and \((1,0)\). The resulting defect is irreducibly relational rather than additional unary information.

### Three-probe witness

Let every unary and pairwise projection be the full binary set or full binary pair set, while

\[
\mathcal K(P@a,Q@b,R@c)
=
\{(x,y,z)\in\{0,1\}^3:x+y+z=0\pmod 2\}.
\]

Every pairwise projection is surjective, but the ternary object has four rather than eight elements. Hence pairwise compatibility does not fill the three-placement configuration. A higher Interaction Net cell is required to carry the parity obstruction.

## Proposed semantic dictionary

| Interaction Net datum | Constraint semantics | Proof obligation |
|---|---|---|
| typed port | admissible instrument placement | placement map exists |
| wire | shared restriction interface | endpoint types agree |
| binary interaction cell | two-probe Segal defect | construct \(\chi\) and classify its failure |
| rewrite | comparison of joint constructions | commuting or explicitly residual square |
| higher cell | non-pairwise configuration constraint | horn-filling or obstruction witness |
| erased wire/cell | quotient of constraint information | prove the erased coordinate is inessential |

This dictionary makes the mathematical proof a witness for the net's semantics, rather than treating the net as an illustration of a proof.

## Falsifiers

1. A claimed binary interaction is rejected if \(\chi\) is an isomorphism.
2. A claimed independent pair is rejected if the joint object is not the unary pullback.
3. A claimed pairwise-complete net is rejected by a higher configuration whose proper projections all factor while the full configuration does not.
4. A rewrite is rejected if its two routes induce different restriction maps without an admitted residual cell.
5. Reconstruction of the coherence pyramid is rejected if distinct incidence structures induce the same complete family of typed configuration constraints.

## Finite diagnostic

`checkers/check_probe_configuration_segal_defect.py` enumerates the binary examples exactly. It verifies full unary marginals, the non-surjective binary comparison, full pairwise projections of the even-parity ternary object, and the remaining ternary defect. A deliberately factorized binary fixture must exhibit zero defect and is therefore rejected as evidence for an interaction cell.

## Disposition

The finite construction succeeds: joint probe configurations can carry constraints absent from all unary views, and three-probe constraints can remain invisible to every pairwise view. This establishes a precise candidate semantics for finite Interaction Nets. The next scientific gate is to instantiate \(\mathcal K\) from one existing SCC cell and prove that its net restrictions coincide with the source mathematical maps; no such SCC instantiation is claimed here.
