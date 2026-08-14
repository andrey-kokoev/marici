# Partial Energies as Occurrence-Resolved Cut Valuations

## Record

Date: 2026-08-14

Status: proved at the finite graphwise valuation and independent-interface Cut-cube level; global cosmological period realization remains outside scope.

## Claim

For a connected graph \(G\) with vertex energies \(x_v\) and internal interface energies \(y_e\), define for every connected region \(A\subseteq V(G)\)

\[
\mathcal E_A
=
\sum_{v\in A}x_v
+
\sum_{e\in\partial A}y_e.
\]

At coarse level, complementary regions share the same interface energy variable and produce apparent quadratic relations and factors of two.

Resolve each cut interface into its two boundary occurrences

\[
y_{e,+},
\qquad
y_{e,-}.
\]

Then the primitive interface valuation is linear before physical diagonal specialization.

For a single interface \(e\), define

\[
K_e^{\mathcal E}
=
[
Rh_e
\longrightarrow
Re_{e,+}\oplus Re_{e,-}
]
\]

with

\[
dh_e
=
y_{e,-}e_{e,-}
-
y_{e,+}e_{e,+}.
\]

For a compatible set of cut interfaces \(C\),

\[
K_C^{\mathcal E}
=
\bigotimes_{e\in C}K_e^{\mathcal E}.
\]

This is the occurrence-resolved Boolean Cut cube.

After localizing the independent nonzero interface weights, each factor becomes rank one and the whole cube closes tensorially.

Physical diagonal specialization

\[
y_{e,+}=y_{e,-}=y_e
\]

produces the familiar doubled interface coefficient

\[
y_{e,+}+y_{e,-}
\mapsto
2y_e.
\]

Therefore the factor of two is not an additional cosmological coupling. It is the quotient index produced by identifying two previously distinct boundary occurrences.

The nested-history sum on a tree graph,

\[
\mathfrak W_G
=
\sum_{\mathcal H\in\operatorname{Hier}(G)}
\prod_{A\in\mathcal H}\mathcal E_A^{-1},
\]

obeys the graph recursion

\[
\mathfrak W_G
=
\frac1{\mathcal E_V}
\sum_{e\in E(G)}
\mathfrak W_{G_e^L}\,
\mathfrak W_{G_e^R}.
\]

Its hierarchy poset is the maximal-chain or flag structure of the resolved Cut carrier.

Hence

\[
\boxed{
\text{Nest is not required as an additional primitive operation;}
}
\]

the nesting data are already present as flags of compatible resolved cuts.

## Evidence

The one-interface complex is linear in occurrence variables.

Tensoring independent interfaces gives the ordinary cubical differential with the expected alternating signs, so every independent-interface square closes by tensoriality.

The two-edge bubble was explicitly reduced to the tensor product

\[
K_a^{\mathcal E}\otimes K_b^{\mathcal E},
\]

with its four vertices, four edges, and one square matching the cellular \(I^2\) Cut cube.

The factor \(2\) appears only after the diagonal map

\[
(y_{e,+},y_{e,-})\mapsto(y_e,y_e).
\]

The graph recursion follows by conditioning a nested connected-subgraph hierarchy on its first separating edge.

This entry is a retrospective reconstruction. No standalone repository certificate has yet been attached.

## Boundary

This theorem concerns the universal rational/valuation carrier.

It does not establish that:

- the full cosmohedron is determined by the Cut face poset alone;
- Cayley--Menger discriminants arise from polyhedral incidence;
- integrated loop periods are produced by these Koszul cubes;
- every non-independent or nontransverse cut intersection closes without derived corrections.

The cosmohedral face structure is compatible with nested resolved cuts, but metric or valuation data remain necessary to specify the full geometry.

Loop integration can introduce period systems not contained in bare Cut incidence.

## Consequence

The cosmological branch no longer needs an independent `Nest` generator at the carrier level.

The reusable primitive is occurrence-resolved Cut valuation:

\[
\text{Cut occurrence}
+
\text{linear energy loading}
+
\text{flag}.
\]

The next discriminating question is whether the spatial metric and loop discriminants are additional primitives or follow from sourced kinematics.

## Outcome contract

```json
{
  "claim": "Connected-region partial energies become linear valuations after resolving each cut interface into two boundary occurrences. Independent Cut cubes are tensor products of one-interface complexes, the factor two appears only on physical diagonal specialization, and cosmological nesting is maximal-chain/flag structure rather than a new primitive.",
  "status": "proved",
  "assumptions": [
    "The theorem is scoped to finite graphwise Cut incidence and independent compatible interfaces.",
    "Integrated loop periods and nontransverse global comparisons are excluded.",
    "No standalone repository checker has yet been attached."
  ],
  "evidence_refs": [
    "retrospective cosmology derivation",
    "occurrence-resolved Cut formalism"
  ],
  "factorization_test": {
    "one_interface": "passed analytically",
    "two_edge_bubble": "passed analytically",
    "independent_interface_cube": "passed tensorially",
    "physical_diagonal_factor_two": "passed",
    "integrated_loop_period": "outside scope"
  },
  "counterevidence": [
    "The cosmohedral face poset alone does not determine the integrated metric or period package.",
    "Nontransverse intersections may require derived support data."
  ],
  "next_experiment": "Determine whether Cayley-Menger and spatial Gram geometry are derived from sourced Lorentzian kinematics or require an independent scalar pairing primitive."
}
```