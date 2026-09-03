# `q_G12` quotient-level factorization audit

## Question

Can the sewn physical residue be compared canonically with a lower-graph object in the wall quotient, without choosing an absolute `T7` lift?

## Claim boundary

The source supplies a canonical relative/open class `rho_phys`; its absolute decomposition is noncanonical. A quotient-level comparison is therefore the correct place to seek a lift-independent factorization statement.

There is an exact algebraic descent result at the principal `q_G12` wall. The parity-even tensor interaction has ambient rank seven, restricted rank six, principal kernel `D3-E^2 U=(c-E)(c+E)`, no additional tensor kernel, and equal ambient/restricted quotient coordinates. Its residue satisfies

\[
\operatorname{Res}_{q_{G12}}(Q_{\rm even}\omega)
=Q_{\rm even}|_{q_{G12}}\operatorname{Res}_{q_{G12}}(\omega).
\]

Thus residue commutes with the declared source-module quotient at `q_G12`; no absolute `T7` lift is required for this algebraic descent.

## Interface obstruction

This rank-six tensor quotient is not yet identified with the rank-six three-wall localization quotient carrying the sewn physical Čech class. Their equal dimensions do not construct an isomorphism:

- the tensor quotient is presented by interaction coordinates `U,L1,L2,L3,D1,D2` modulo the principal wall kernel;
- the sewn boundary is presented by oriented shared-wall residues in the localization quotient of the rank-fifteen relative system by the rank-nine absolute system;
- no common ordered basis, comparison matrix, or proof that the tensor restriction annihilates exactly the absolute `M9` subspace is supplied.

The independently normalized lower-graph target is also absent. Consequently the known residue identity proves quotient compatibility inside one source module, not physical lower-graph factorization of `rho_phys`.

## Universal descent test

A candidate lower-graph map

\[
F:M_{15}\longrightarrow \mathcal A_{\rm lower}
\]

descends to the canonical quotient `Q6=M15/M9` exactly when `F(M9)=0`. The descended map is physically usable only if it also preserves the source normalization, Čech orientation, occurrence-unsplit numerator, conductor grade, and endpoint trivialization.

No frozen artifact supplies `F`, an independently normalized `A_lower`, or the annihilation check on a labelled basis of `M9`.

## Strongest falsification attempt

Use the verified rank-six tensor quotient as the lower-graph comparison solely because its dimension matches `Q6`. This fails the packet pullback: the basis labels, source map, quotient kernel, normalization, and target convention are not identified. The shared number six is not a comparison arrow.

## Acceptance test

1. freeze labelled bases for `M15`, `M9`, the sewn `Q6`, and the tensor rank-six quotient;
2. provide the source-derived comparison matrix and prove that its kernel is exactly `M9`;
3. transport `rho_phys` and all three oriented shared-wall residues;
4. verify Čech closure and occurrence-unsplit sewing after transport;
5. define the normalized lower-graph object and compare the transported class;
6. include a vector in `M9` as a deliberate-failure test for descent.

## Disposition

Lift-independent factorization is structurally possible and residue already descends through a declared principal `q_G12` source quotient. The physical factorization square remains unconstructed because the tensor quotient, the sewn localization quotient, and the normalized lower-graph target have no source-derived comparison maps between them.

## Evidence

- `research/benincasa/tensor-marked-wall-localization.json`
- `research/benincasa/source-bases-localization-fiber.json`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
- `research/benincasa/physical_shared_wall_no_canonical_t7_lift.py`
