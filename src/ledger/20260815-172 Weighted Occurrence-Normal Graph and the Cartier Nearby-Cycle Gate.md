# Weighted Occurrence-Normal Graph and the Cartier Nearby-Cycle Gate

## Record

Date: 2026-08-15

Status: weighted graph theorem proved on the unit locus; the clean
unlocalized-diagonal claim is falsified by its genuine special fibres. The
result is a finite projective graph, saturation, and excess gate only. It
does not construct the relative-support/nearby-cycle selection required for
entry 143. No graph admission is claimed.

## Weighted occurrence and normal relations

Retain the independent Rees equations

\[
u_5=t_5x_5,
\qquad
U_D=t_DX_D.
\]

Use homogeneous occurrence and normal coordinates

\[
[G:H]=[x_5:X_D],
\qquad
[P:Q]=[u_5:U_D].
\]

Eliminating the affine representatives gives the canonical weighted
projective closure

\[
\boxed{
\mathcal G_w:
t_DHP-t_5GQ=0
\quad\subset\quad
\mathbb P^1_{G,H}\times\mathbb P^1_{P,Q}.
}
\]

This equation is forced by the two Rees relations. It is not a freely chosen
diagonal and uses no inversion in the polynomial base.

## Unit-locus graph theorem

Where both \(t_5\) and \(t_D\) are units, \(\mathcal G_w\) is exactly the
graph of the weighted projective automorphism

\[
\boxed{
[G:H]\longmapsto[t_5G:t_DH].
}
\]

Both coordinate endpoints remain aligned:

\[
[1:0]\longmapsto[1:0],
\qquad
[0:1]\longmapsto[0:1].
\]

Thus the unit-locus graph realizes the desired short/short and long/long
endpoint alignment from entry 171. This positive statement is scoped to the
locus on which both weights are invertible.

## The two single-zero fibres

On the Cartier special fibre \(t_5=0\) with \(t_D\) a unit, the equation is

\[
HP=0.
\]

Therefore

\[
\boxed{
\mathcal G_w|_{t_5=0}
=\{H=0\}\cup\{P=0\},
}
\]

a reducible union of two \(\mathbb P^1\) components meeting in one point.
It is not the graph of a projective automorphism.

Similarly, on \(t_D=0\) with \(t_5\) a unit,

\[
GQ=0,
\]

so

\[
\boxed{
\mathcal G_w|_{t_D=0}
=\{G=0\}\cup\{Q=0\}.
}
\]

This is the reflected reducible fibre. Neither degeneration is an irrelevant
homogeneous-coordinate artifact.

## Double-zero excess

At \(t_5=t_D=0\), the graph equation vanishes identically. Hence

\[
\boxed{
\mathcal G_w|_{t_5=t_D=0}
=\mathbb P^1\times\mathbb P^1.
}
\]

The one-equation Koszul differential is zero on this fibre, leaving a
primitive rank-one excess class

\[
\operatorname{Tor}_1\simeq\mathbf1.
\]

This Tor line is genuine limiting geometry. It is not the positive Tor of
the regular double-Rees product from entry 171; it appears because the graph
equation itself specializes to zero.

## Saturation does not clean the fibres

Projective irrelevant-ideal saturation removes only pairs with a zero
homogeneous coordinate vector. Every point in the two reducible single-zero
fibres and in the double-zero \(\mathbb P^1\times\mathbb P^1\) has honest
projective coordinates. Consequently saturation removes none of these
components.

Thus the clean-diagonal claim is falsified over the unlocalized base:

\[
\boxed{
\mathcal G_w\text{ is a weighted graph on the unit locus but not a clean
flat diagonal across }t_5t_D=0.
}
\]

The failure cannot be repaired by projective saturation.

## Completion and Cartier restrictions

The long coefficient \(t_D\) may be a unit only inside the named completed
long-graph scope. This completion-scoped statement must not be promoted to a
universal integral inversion.

The short coefficient \(t_5\) must remain unlocalized. Its zero fibre is the
Cartier grade carrying the short occurrence-normal specialization. Inverting
\(t_5\) would delete \(V(t_5)\), erase the reducible limiting fibre, and
remove precisely the grade that the construction is meant to transport.

Hence the tempting repair

\[
t_5^{-1}\in A
\]

is forbidden. It would prove only the already-understood unit-locus graph by
discarding the physical degeneration.

## Relation to the double-Rees transfer

Entry 171 proves the exact four-corner coefficient correspondence and its
forced double Cech overlap. The weighted equation supplies a canonical
unit-locus alignment of the two physical endpoints. But the special fibres
show that its closure contains more than the aligned interval:

- the \(t_5=0\) fibre has two components;
- the \(t_D=0\) fibre has two reflected components; and
- the double-zero fibre is all \(\mathbb P^1\times\mathbb P^1\) with
  \(\operatorname{Tor}_1\).

Therefore the weighted closure does not by itself select the physical
component or explain the extraordinary transport through the exceptional
fibre. It is a candidate coefficient carrier, not an admitted spatial graph.

## The exact nearby-cycle gate

The next datum must be an independently geometric relative-support or
nearby-cycle selection

\[
\Psi_{t_5}^{\rm rel}(mathcal G_w)
\]

along the short Cartier divisor \(V(t_5)\). It must retain the conormal label

\[
[t_5]
\]

rather than invert or forget it. The selection must distinguish the physical
component of the reducible fibre, retain the double-zero excess line, and
construct an extraordinary proper push--pull across the exceptional fibre:

\[
\operatorname{BC}^{\rm ex}_{\mathcal G_w}:
\mathcal S_{m first\ flip}^{\rm rel}
\longrightarrow
\mathcal E_{03}^{\rm BM,\check C}.
\]

Its required tests are:

1. preserve the aligned endpoints on the unit locus;
2. retain \([t_5]\) on \(V(t_5)\);
3. account for, rather than saturate away, both reducible components;
4. transport the double-zero \(\operatorname{Tor}_1\) class;
5. recover entry 171's complementary residues and forced overlap; and
6. land in actual entry-143 face/circle support states.

No existing checker constructs this nearby-cycle selection or extraordinary
pushforward.

## Global boundary

The weighted closure does not construct the entry-143 spatial support kernel,
attach \(p_{03}\), retain \(q_J\), or map nontrivially to the generic
\(Q03\) leg. It also does not construct the second flip, three-road source
normalization, endpoint comparison cells, or the logarithmic
Beck--Chevalley homotopy.

Accordingly the endpoint-fixed mapping fiber remains uninstantiated and
reflection parity is undefined.

## Anti-circularity controls

- Do not infer a clean unlocalized diagonal from the unit-locus graph.
- Do not remove genuine special-fibre components by calling them irrelevant.
- Do not invert \(t_5\); this erases the Cartier grade.
- Do not treat completion-scoped invertibility of \(t_D\) as a universal
  integral relation.
- Do not discard the double-zero Tor line.
- Do not select a component by prescribing the desired physical endpoint
  values.
- Do not infer spatial descent, generic \(Q\), a mapping fiber, parity, or
  graph admission from the weighted equation.

## Falsifiers and scope

The unit-locus theorem would be falsified if the weighted equation failed to
define the stated automorphism or failed to preserve either coordinate
endpoint. The scoped clean-diagonal no-go would be falsified if a single-zero
fibre were irreducible, saturation removed its extra component, or the
double-zero equation retained nonzero differential and no Tor line.

The geometric boundary would be crossed by an independently constructed
relative-support/nearby-cycle functor that selects the correct \(V(t_5)\)
component while retaining \([t_5]\), transports the excess across the
exceptional fibre, and lands in the literal entry-143 support filtration.

No no-go is claimed for such an enriched nearby-cycle graph.

## Provenance and exact certificate

The exact checker is

- `research/voevodsky/check_d03_weighted_occurrence_normal_graph_gate.rs`.

Its SHA-256 hash is

`98a0cebe2a728b893646c19d38bdf891ef4c6fe4dc9af3d152dd41e788dacc5f`.

It verifies the cross relation, every unit-locus weighted graph and aligned
endpoint, both reducible single-zero fibres, the full double-zero
\(\mathbb P^1\times\mathbb P^1\), its rank-one Tor line, failure of
saturation to remove any limiting point, completion scope of \(t_D\), and
the prohibition on \(t_5\) inversion.

## Next experiment

Construct the relative-support/nearby-cycle selection on \(V(t_5)\), keeping
the conormal class \([t_5]\). Build the extraordinary proper push--pull
across both components and their exceptional intersection, and verify that
the double-zero Tor line maps to the forced entry-171 overlap. Then test
landing in the actual entry-143 \(F03\) collar and attachment to
\(p_{03}/q_J\). Only afterward attempt global gluing, the mapping fiber, or
parity.

## Outcome contract

~~~json
{
  "claim": "The equations u5=t5*x5 and U_D=t_D*X_D define the weighted projective closure t_D*H*P-t5*G*Q=0, which is the aligned weighted P1 graph on the unit locus; over the unlocalized base its single-zero fibres are reducible, its double-zero fibre is P1xP1 with a rank-one Tor1 line, and projective saturation removes none of these components.",
  "status": "falsified",
  "scope": "falsifies only the clean unlocalized-diagonal interpretation; the unit-locus graph, special-fibre census, saturation, and excess theorem are proved, with no graph admission or spatial entry143 map",
  "assumptions": [
    "The occurrence and normal Rees equations retain independent weights t5 and t_D.",
    "t_D is a unit only in its named completed graph scope.",
    "t5 remains unlocalized so its Cartier zero grade survives.",
    "Projective saturation removes only irrelevant zero coordinate vectors."
  ],
  "factorization": {
    "cross_relation": "t_D*H*P-t5*G*Q=0",
    "unit_locus": "graph [G:H] -> [t5*G:t_D*H]",
    "aligned_endpoints": [["[1:0]", "[1:0]"], ["[0:1]", "[0:1]"]],
    "t5_zero_tD_unit": "{H=0} union {P=0}",
    "tD_zero_t5_unit": "{G=0} union {Q=0}",
    "double_zero": "P1xP1",
    "double_zero_Tor1": "primitive rank one",
    "saturation": "removes no genuine special-fibre point",
    "tD_scope": "unit only in named completion",
    "t5_inversion": "forbidden; erases Cartier zero grade",
    "relative_support_nearby_cycle_selection": "unconstructed",
    "retained_conormal_t5": "required",
    "extraordinary_exceptional_pushforward": "unconstructed",
    "entry143_spatial_support": "unconstructed",
    "generic_Q": "unconstructed",
    "mapping_fiber": "uninstantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_weighted_occurrence_normal_graph_gate.rs",
    "src/ledger/20260814-115 Central Multi-Rees Fibre and the Missing Spatial Extension.md",
    "src/ledger/20260814-129 Cox Principal-Line Trace and the Extraordinary Cousin Boundary.md",
    "src/ledger/20260814-130 Simultaneous D03 Endpoint Cousin Map and the PC Purity Boundary.md",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-171 Double-Rees First-Flip Transfer and the Aligned-Corner Spatial Gate.md"
  ],
  "checker_sha256": "98a0cebe2a728b893646c19d38bdf891ef4c6fe4dc9af3d152dd41e788dacc5f",
  "counterevidence": [
    "At t5=0 the closure is a reducible union of two P1 components.",
    "At t_D=0 the reflected reducible fibre persists.",
    "At the double zero the full P1xP1 and rank-one Tor1 survive saturation.",
    "Inverting t5 would delete the Cartier grade rather than resolve it."
  ],
  "next_experiment": "Construct the relative-support/nearby-cycle selection on V(t5) retaining [t5], then define the extraordinary pushforward across the reducible exceptional fibre and transport its Tor1 class to the forced double-Rees overlap before testing entry143 support and p03/q_J attachment."
}
~~~
