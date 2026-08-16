# Projective SNC Tate Can--Var Bridge and the Literal Realization Gate

Date: 2026-08-15  
Status: proved for the normalization-provenanced augmented coefficient/log
carrier. The nearby-cycle six-functor lift, multiplicity-sensitive target
assignments, and literal entry-143 rows remain unconstructed. No graph
admission is claimed.

## Result

The coordinate SNC divisor of
\[
\mathbf P(J_+/J_+^2)
\]
has the augmented oriented incidence complex
\[
\mathbb Z_{\rm or}
\xrightarrow{N}
P_{\rm facet}
\xrightarrow{R-I}
P_{\rm pair}
\xrightarrow{\epsilon}
\mathbb Z,
\]
where the bases are ordered by the physical roads \((14,03,25)\),
\[
N=(1,1,1)^T,\qquad \epsilon=(1,1,1).
\]

Entry 113's integral Tate carrier is
\[
\mathbb Z_{\rm or}
\xrightarrow{N}
P_{\rm tag}
\xrightarrow{I-R}
P_{\rm road}
\xrightarrow{\epsilon}
\mathbb Z.
\]

The labelled facet/tag and complementary pair/road identifications force the
degreewise signs
\[
\boxed{F=(+1,+I,-I,-1).}
\]
They give a strict chain isomorphism because
\[
I(R-I)=-(I-R),\qquad
(-1)\epsilon=\epsilon(-I),
\]
while the top norm square is the identity.

Both complexes are exact and saturated:

- \(N\) is primitive;
- \(R-I\) has rank two and Smith factors \((1,1)\);
- \(\epsilon\) is primitive;
- \(\ker(R-I)=\mathbb ZN\);
- \(\operatorname{im}(R-I)=\ker\epsilon\).

The bridge components are all unimodular. Rotation and the signed reflection
actions commute with \(F\) in every degree. In particular, the top norm is
reflection-odd, the road norm is reflection-even before the separate physical
orientation twist, and
\[
\epsilon N=3
\]
is retained integrally. No \(1/3\) projector or equivariant contraction is
introduced.

This identifies entry 205's two endpoint weight lines and \(A_2\) middle
weight with the already admitted \(N/(1-r)/\epsilon\) Tate architecture. It
is the canonical coefficient/log can--var carrier bridge that was previously
missing.

## What remains spatial

The checker does not turn this chain isomorphism into a morphism of
normalization/conductor nearby-cycle objects. In particular, it does not yet
prove that:

1. the source top reaches the primitive \(K_6\) coherence top with the
   discrepancy multiplicity two;
2. the opposite endpoint reaches the physical
   \(dH_\Sigma=q_\Sigma-\sum_Dx_D\widetilde\xi_D\) block with coefficient
   one;
3. a pair basis vector reaches the complementary literal corridor \(q_k\);
4. its two facet restrictions are the adjacent long-facet excess-Gysin maps;
5. the induced Boolean normal/Tor/Cech maps are the 24 entry-143 rows.

The next required construction is therefore a lift
\[
\operatorname{BC}^{!,\log}_{\rm SNC/Tate}:
\Psi^{\log}_{\rm cond}
\longrightarrow
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\]
whose associated augmented carrier is \(F\), whose top and bottom grades have
the independently fixed multiplicities \(2\) and \(1\), and whose middle
pair grades are the three
\[
\Gamma_{ij}^{!,\log}\longrightarrow C_\bullet(q_k).
\]

Until this lift exists, the endpoint/Q mapping fiber,
\(p_{\partial,Q}\), its Bockstein, \(D_8\), and Jordan coherence remain
undefined.

## Certificate

- \`research/voevodsky/check_p2_snc_tate_can_var_bridge.rs\`
- SHA-256:
  \`f5517afb07dace5c1eb83e76c277fe42413f0703d7bf3439ce9442f403bc183b\`

Validation:

- \`rustfmt --edition 2021\`: passed;
- \`rustc --edition=2021 -D warnings -O\`: passed;
- linked runtime assertions: passed;
- runtime JSON parse and scoped status assertion: passed;
- temporary executable: removed;
- \`git diff --check\`: required before commit.

## Outcome contract

~~~json
{
  "claim": "The canonical augmented projective-conductor SNC complex is integrally and D3-equivariantly chain-isomorphic to entry113's N/(1-r)/epsilon Tate carrier through the forced unimodular signs (+1,+I,-I,-1). The exact bridge retains epsilon*N=3 without division by three.",
  "status": "proved_scoped_augmented_snc_tate_can_var_carrier_bridge",
  "scope": "normalization-provenanced augmented coefficient/log carrier only; nearby-cycle six-functor realization, discrepancy-two and primitive-qSigma target assignments, pairwise log-Gysin maps, 24 literal entry143 rows, endpoint/Q mapping fiber, parity, D8, Jordan, and graph admission remain open",
  "evidence": {
    "source_differentials": ["N", "R-I", "epsilon"],
    "target_differentials": ["N", "I-R", "epsilon"],
    "bridge_signs": [1, 1, -1, -1],
    "bridge_component_smith": [1, 1, 1, 1],
    "middle_rank": 2,
    "middle_smith": [1, 1],
    "complex_exact": true,
    "D3_equivariant": true,
    "reflection_equivariant": true,
    "epsilon_times_norm": 3,
    "division_by_three": false,
    "literal_entry143_rows_constructed": 0,
    "physical_mapping_fiber": "unconstructed"
  },
  "checker_sha256": "f5517afb07dace5c1eb83e76c277fe42413f0703d7bf3439ce9442f403bc183b",
  "next_required_map": "Lift the forced augmented-chain bridge to a normalization/conductor nearby-cycle and excess-Gysin morphism, with top multiplicity two, primitive H_Sigma/q_Sigma bottom, and three literal pair-overlap restrictions."
}
~~~
